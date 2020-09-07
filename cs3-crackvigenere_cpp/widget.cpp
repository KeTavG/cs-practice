#include "widget.h"
#include "ui_widget.h"

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);
}

Widget::~Widget()
{
    delete ui;
}

void Widget::on_affButton_clicked()
{
    cryptoData.setEncryptedText(ui->ciphertext->toPlainText());
    QVector<double> affIndexArr;
    QString alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    QString cryptoText = cryptoData.getEncryptedText();
    for (int keyLength = 3; keyLength <= 10; ++keyLength) {
        QString textWithInterval("");
        double affIndex = 0;
        for (int i = 0; i < cryptoText.length(); ++i) {
            if (i % keyLength == 0)
                textWithInterval.append(cryptoText.at(i));
        }
        for (int i = 0; i < 32; ++i) {
            double a = textWithInterval.count(alphabet[i]);
            double b = textWithInterval.count(alphabet[i]) - 1;
            double c = textWithInterval.length();
            double d = textWithInterval.length() - 1;
            affIndex += (a * b) / (c * d);
        }
        affIndexArr.append(affIndex);
    }
    QString out = "        3       |        4       |        5       |        6       |        7       |        8       |        9       |        10       \n";
    for (int i = 0; i < affIndexArr.size(); ++i) {
        out += QString::number(affIndexArr[i]) + '|';
    }
    QMessageBox::information(this, "Affinity Index", out);
    return;
}

void Widget::on_findKeyButton_clicked()
{
    int _keyLength = ui->keyLength->value();
    QString alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    QString keyWord("");
    QVector<QString> shifts(_keyLength);
    for (int i = 0; i < cryptoData.getEncryptedText().length(); ++i) {
        int module = i % _keyLength;
        shifts[module].append(cryptoData.getEncryptedText().at(i));
    }
    for (int i = 0; i < shifts.size(); ++i) {
        int max = -1;
        QChar maxChr;
        for (int j = 0; j < 32; ++j) {
            if (shifts[i].count(alphabet[j]) > max) {
                max = shifts[i].count(alphabet[j]);
                maxChr = alphabet[j];
            }
        }
        keyWord.append(maxChr);
    }
    QString shiftKeyWord("");
    for (int i = 0; i < _keyLength; ++i) {
        for (int j = 0; j < alphabet.length(); ++j) {
            if (keyWord[i] == alphabet[j]) {
                int shift = j - 14;
                if (shift < 0)
                    shift = 31 - abs(shift) + 1;
                shiftKeyWord.append(alphabet[shift]);
            }
        }
    }
    key.setKeyWord(shiftKeyWord);
    ui->keyWord->setText(key.keyWord());
    return;
}

void Widget::on_decryptButton_clicked()
{
    QString result("");
    QString alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ";
    QString keyWord = ui->keyWord->text();
    int keyLength = ui->keyLength->value();
    int symbolCount = 0;
    QVector<int> arrayOfShifts;
    for (int i = 0; i < keyLength; ++i) {
        arrayOfShifts.push_back(alphabet.indexOf(keyWord.at(i)));
    }
    for (int i = 0; i < ui->ciphertext->toPlainText().length(); ++i) {
        if (ui->ciphertext->toPlainText().at(i).unicode() < 1040 || ui->ciphertext->toPlainText().at(i).unicode() > 1071) {
            result.append(ui->ciphertext->toPlainText().at(i));
        }
        else {
            int shift = alphabet.indexOf(ui->ciphertext->toPlainText().at(i)) - arrayOfShifts.at(symbolCount % keyLength);
            if (shift < 0) {
                shift = 31 - abs(shift) + 1;
            }
            result.append(alphabet.at(shift % 32));
            ++symbolCount;
        }
    }
    cryptoData.setDecryptedText(result);
    ui->plaintext->setPlainText(cryptoData.getDecryptedText());
    return;
}
