#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QMessageBox>
#include "keyword.h"
#include "cryptodata.h"

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT

public:
    explicit Widget(QWidget *parent = nullptr);
    ~Widget();

private:
    CryptoData cryptoData;
    KeyWord key;

private slots:
    void on_affButton_clicked();

    void on_findKeyButton_clicked();

    void on_decryptButton_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
