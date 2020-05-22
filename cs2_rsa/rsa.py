# This Python file uses the following encoding: utf-8
import sys
from random import randint, randrange
from collections import namedtuple
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Slot
from form_ui import Ui_Form

N_LENGTH = 44
NORMALIZE_LENGTH = 4
AMOUNT_OF_TESTS = 1024
MILLER_RABIN = 0

class RSA(QWidget):
    def __init__(self):
        super(RSA, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.generateKeysButton.clicked.connect(self.generateKeysSignal)
        self.ui.encryptButton.clicked.connect(self.encryptSignal)
        self.ui.decryptButton.clicked.connect(self.decryptSignal)

    @Slot()
    def generateKeysSignal(self):
        self.publicKey, self.privateKey = RSACore.generateKeys(N_LENGTH)
        self.publicKey = str(self.publicKey[0]), str(self.publicKey[1])
        self.privateKey = str(self.privateKey[0]), str(self.privateKey[1])
        ciphertext = RSACore.encrypt("test", self.publicKey)
        plaintext = RSACore.decrypt(ciphertext, self.privateKey)
        while not plaintext == "test":
            self.publicKey, self.privateKey = RSACore.generateKeys(N_LENGTH)
            self.publicKey = str(self.publicKey[0]), str(self.publicKey[1])
            self.privateKey = str(self.privateKey[0]), str(self.privateKey[1])
            ciphertext = RSACore.encrypt("test", self.publicKey)
            plaintext = RSACore.decrypt(ciphertext, self.privateKey)
        self.ui.publicKeywordS.setText(self.publicKey[0])
        self.ui.publicKeywordN.setText(self.publicKey[1])
        self.ui.privateKeywordE.setText(self.privateKey[0])

    @Slot()
    def encryptSignal(self):
        plaintext = self.ui.plaintextEncrypt.toPlainText()
        publicKey = self.ui.publicKeywordS.text(), self.ui.publicKeywordN.text()
        ciphertext = RSACore.encrypt(plaintext, publicKey)
        self.ui.ciphertextEncrypt.setPlainText(ciphertext)
        self.ui.ciphertextDecrypt.setPlainText(ciphertext)

    @Slot()
    def decryptSignal(self):
        ciphertext = self.ui.ciphertextDecrypt.toPlainText()
        privateKey = self.ui.privateKeywordE.text(), self.ui.publicKeywordN.text()
        plaintext = RSACore.decrypt(ciphertext, privateKey)
        self.ui.plaintextDecrypt.setPlainText(plaintext)

class RSACore:
    @staticmethod
    def encrypt(plaintext, publicKey):
        s, n = publicKey 
        blockSize = len(n) // NORMALIZE_LENGTH - 1
        plaintextBlock = [plaintext[i:i + blockSize] for i in range(0, len(plaintext), blockSize)]
        plaintextCode = []
        for block in plaintextBlock:
            normBlockCode = ''
            for char in block:
                charCode = str(ord(char))
                normBlockCode += '0' * (NORMALIZE_LENGTH - len(charCode)) + charCode
            plaintextCode.append(int(normBlockCode))
        ciphertextCode = [str(pow(block, int(s), int(n))) for block in plaintextCode]
        normCiphertext = ['0' * (len(n) - len(str(code))) + str(code) for code in ciphertextCode]
        return ''.join(normCiphertext)

    @staticmethod
    def decrypt(ciphertext, privateKey):
        e, n = privateKey
        blockSize = len(n) // NORMALIZE_LENGTH - 1
        ciphertextBlock = [int(ciphertext[i:i + len(n)]) for i in range(0, len(ciphertext), len(n))]
        plaintextBlock = [str(pow(block, int(e), int(n))) for block in ciphertextBlock]
        normBlockCode = ['0' * (blockSize * NORMALIZE_LENGTH - len(block)) + block
                         for block in plaintextBlock]
        plaintext = []
        for block in normBlockCode:
            plaintext += [block[i:i + NORMALIZE_LENGTH]
                          for i in range(0, len(block), NORMALIZE_LENGTH)]
        plaintext = [chr(int(code)) for code in plaintext
                     if not code == "0000"]
        return ''.join(plaintext)

    @staticmethod
    def generateKeys(length, test = MILLER_RABIN, amountOfTests = AMOUNT_OF_TESTS):
        ## Generate prime number
        def generatePrime(length, test, amountOfTests):
            ## Check on primes
            def isPrime(number, test, amountOfTests):
                ## Miller–Rabin primality test
                def testMillerRabin(number, amountOfTests):
                    if number == 2 or number == 3:
                        return True
                    if number <= 1 or number % 2 == 0:
                        return False

                    # Find s, t
                    # N - 1 = 2^s * t
                    s = 0
                    t = number - 1
                    while t & 1 == 0:
                        s += 1
                        t //= 2

                    # Tests
                    for _ in range(amountOfTests):
                        a = randrange(2, number - 1)
                        x = pow(a, t, number)
                        if x != 1 and x != number - 1:
                            j = 1
                            while j < s and x != number - 1:
                                x = pow(x, 2, number)
                                if x == 1:
                                    return False
                                j += 1
                            if x != number - 1:
                                return False
                    return True

                ## isPrime
                if test == MILLER_RABIN:
                    return testMillerRabin(number, amountOfTests)

            ## generatePrime
            primeCandidate = 4
            generatePrimeCandidate = lambda length: randint((10**(length - 1)), 10**length)
            while not isPrime(primeCandidate, test, amountOfTests):
                primeCandidate = generatePrimeCandidate(length)
            return primeCandidate

        ## Generate relatively prime number
        def generateRelPrime(relNumber):
            ## Check on relatively primes
            def isRelPrimes(a, b):
                for n in range(2, min(a, b) + 1):
                    if a % n == 0 and b % n == 0:
                        return False
                    return True

            ## generateRelPrime
            generateRelPrimeCandidate = lambda relNumber: randrange(4, relNumber - 1)
            relPrimeCandidate = generateRelPrimeCandidate(relNumber)
            while not isRelPrimes(relPrimeCandidate, relNumber):
                relPrimeCandidate = generateRelPrimeCandidate(relNumber)
            return relPrimeCandidate

        ## Generate e, such that (e * s) mod d = 1
        def generateE(s, d):
            ## Extended Euclidean algorithm
            def extGCD(s, d):
                if s == 0:
                    return (d, 0, 1)
                else:
                    gcd, x, y = extGCD(d % s, s)
                return (gcd, y - (d // s) * x, x)

            ## generateE
            if s < 0:
                s = s % d

            # s * x + d * y = gcd
            _, x, _ = extGCD(s, d)
            e = x % d
            return e

        ## generateKeys
        # 1. Select two large and prime numbers P, Q
        # 2. Calculate the number N = P * Q
        # 3. Calculate the value of Euler's function d = (P - 1)(Q - 1)
        # 4. Select a random number s < d and relatively prime with d
        # 5. Calculate the number e, such that (e * s) mod d = 1
        lengthN = length
        length = length // 2
        n = pow(10, lengthN + 1)
        while not ((n // pow(10, lengthN) == 0) and (n // pow(10, lengthN - 1) > 0)):
            p = generatePrime(length, test, amountOfTests) # 1
            q = generatePrime(length, test, amountOfTests)
            n = p * q                                      # 2
        d = (p - 1) * (q - 1)                              # 3
        s = generateRelPrime(d)                            # 4
        e = generateE(s, d)                                # 5
        return (s, n), (e, n)

if __name__ == "__main__":
    app = QApplication([])
    window = RSA()
    window.show()
    sys.exit(app.exec_())
