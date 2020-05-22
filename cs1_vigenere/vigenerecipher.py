# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import Slot
from form_ui import Ui_Form

class VigenereCipher(QWidget):
    def __init__(self):
        super(VigenereCipher, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.encryptButton.clicked.connect(self.encryptSignal)
        self.ui.decryptButton.clicked.connect(self.decryptSignal)

    @Slot()
    def encryptSignal(self):
        plaintext = self.ui.plaintextEncrypt.toPlainText()
        key = self.ui.keyword.text()
        ciphertext = VigenereCore.encrypt(plaintext, key)
        self.ui.ciphertextEncrypt.setPlainText(ciphertext)

    @Slot()
    def decryptSignal(self):
        ciphertext = self.ui.ciphertextDecrypt.toPlainText()
        key = self.ui.keyword.text()
        plaintext = VigenereCore.decrypt(ciphertext, key)
        self.ui.plaintextDecrypt.setPlainText(plaintext)

class VigenereCore:
    @staticmethod
    def encrypt(plaintext, key):
        ciphertext = ""
        key = key.lower()
        for chIndex, ch in enumerate(plaintext):
            if 'A' <= ch <= 'Z':
                ch = ch.lower()
                offset = ord(key[chIndex % len(key)])
                offset -= ord('a')
                chCode = ord(ch) + offset
                if chCode > ord('z'):
                    chCode -= 26
                ciphertext += (chr(chCode)).upper()
            elif 'a' <= ch <= 'z':
                offset = ord(key[chIndex % len(key)])
                offset -= ord('a')
                chCode = ord(ch) + offset
                if chCode > ord('z'):
                    chCode -= 26
                ciphertext += chr(chCode)
            else:
                ciphertext += ch
        return ciphertext[::-1]

    @staticmethod
    def decrypt(ciphertext, key):
        ciphertext = ciphertext[::-1]
        plaintext = ""
        key = key.lower()
        for chIndex, ch in enumerate(ciphertext):
            if 'A' <= ch <= 'Z':
                ch = ch.lower()
                offset = ord(key[chIndex % len(key)])
                offset -= ord('a')
                chCode = ord(ch) - offset
                if chCode < ord('a'):
                    chCode += 26
                plaintext += (chr(chCode)).upper()
            elif 'a' <= ch <= 'z':
                offset = ord(key[chIndex % len(key)])
                offset -= ord('a')
                chCode = ord(ch) - offset
                if chCode < ord('a'):
                    chCode += 26
                plaintext += chr(chCode)
            else:
                plaintext += ch
        return plaintext

if __name__ == "__main__":
    app = QApplication([])
    window = VigenereCipher()
    window.show()
    sys.exit(app.exec_())
