#ifndef KEYWORD_H
#define KEYWORD_H

#include <QtCore>

class KeyWord
{

private:
    int m_length;
    QString m_keyWord;

public:
    KeyWord()
    {

    }
    QString keyWord() const
    {
        return m_keyWord;
    }
    void setKeyWord(const QString word)
    {
        m_keyWord = word;
        m_length = word.length();
    }
    int length() const
    {
        return m_length;
    }
};

#endif // KEYWORD_H
