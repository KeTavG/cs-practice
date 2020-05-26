# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1039, 574)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.keyword = QLineEdit(Form)
        self.keyword.setObjectName(u"keyword")

        self.verticalLayout.addWidget(self.keyword)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plaintextEncrypt = QPlainTextEdit(Form)
        self.plaintextEncrypt.setObjectName(u"plaintextEncrypt")

        self.horizontalLayout_2.addWidget(self.plaintextEncrypt)

        self.ciphertextEncrypt = QPlainTextEdit(Form)
        self.ciphertextEncrypt.setObjectName(u"ciphertextEncrypt")
        self.ciphertextEncrypt.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.ciphertextEncrypt)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.encryptButton = QPushButton(Form)
        self.encryptButton.setObjectName(u"encryptButton")

        self.verticalLayout.addWidget(self.encryptButton)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.ciphertextDecrypt = QPlainTextEdit(Form)
        self.ciphertextDecrypt.setObjectName(u"ciphertextDecrypt")
        self.ciphertextDecrypt.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.ciphertextDecrypt)

        self.plaintextDecrypt = QPlainTextEdit(Form)
        self.plaintextDecrypt.setObjectName(u"plaintextDecrypt")
        self.plaintextDecrypt.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.plaintextDecrypt)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.decryptButton = QPushButton(Form)
        self.decryptButton.setObjectName(u"decryptButton")

        self.verticalLayout.addWidget(self.decryptButton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"VigenereCipher", None))
        self.label.setText(QCoreApplication.translate("Form", u"Keyword", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Plaintext", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Ciphertext", None))
        self.encryptButton.setText(QCoreApplication.translate("Form", u"Encrypt", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Plaintext", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ciphertext", None))
        self.decryptButton.setText(QCoreApplication.translate("Form", u"Decrypt", None))
    # retranslateUi

