#ifndef CRYPTOTEXT_H
#define CRYPTOTEXT_H

#include <QtCore>

class CryptoData
{

private:
    QString encryptedText;
    QString decryptedText;
    QMultiMap<QChar, int> mapOfDelimiters;

public:
    CryptoData()
    {

    }
    void findDelimiters(QString text)
    {
        mapOfDelimiters.clear();
        for (int i = 0; i < text.length(); ++i)
        {
            if (text.at(i).unicode() < 1040 || text.at(i).unicode() > 1071)
            {
                mapOfDelimiters.insert(text.at(i),i);
            }
        }
    }
    void parsingText(QString text)
    {
        QMultiMap<QChar, int>::iterator it = mapOfDelimiters.begin();
        for (; it != mapOfDelimiters.end(); ++it)
        {
            text = text.remove(it.key());
        }
        encryptedText = text;
    }
    QString getEncryptedText() const
    {
        return encryptedText;
    }
    void setEncryptedText(const QString text)
    {
        findDelimiters(text);
        parsingText(text);
    }
    QString getDecryptedText() const
    {
        return decryptedText;
    }
    void setDecryptedText(QString text)
    {
        decryptedText = text;
    }
};

#endif // CRYPTOTEXT_H
