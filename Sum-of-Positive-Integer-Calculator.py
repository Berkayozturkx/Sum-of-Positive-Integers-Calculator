#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class GaussSum(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Pozitif Tamsayı Toplamı Hesaplayıcısı")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Başlangıç Sayısını Giriniz:"),1,1)
        grid.addWidget(QLabel("Bitiş Sayısını Giriniz:"),2,1)
        
        self.baslangic = QLineEdit()
        grid.addWidget(self.baslangic,1,2)
        
        self.bitis = QLineEdit()
        grid.addWidget(self.bitis,2,2)
        
        
        self.buton = QPushButton("Hesapla")
        grid.addWidget(self.buton,3,2)
        self.buton.clicked.connect(self.hesapla)
        
        self.yazi = QLabel("")
        grid.addWidget(self.yazi,5,1)
        
        
        self.setLayout(grid)
        self.resize(350,140)
        self.show()
        
    def hesapla(self):
        baslangic = 0
        try: baslangic = int(self.baslangic.text())
        except: pass
        
        bitis = 0
        try: bitis = int(self.bitis.text())
        except: pass
        
        asilToplam = 0
        cikarilacakToplam = 0
            
        if(baslangic > 0 and bitis > 0):
            if(baslangic == 1):
                for i in range(baslangic,bitis+1):
                    asilToplam += i

                sonuc = asilToplam
                self.yazi.setText("Toplam: {}".format(sonuc))

            else:
                for i in range(1,bitis+1):
                    asilToplam += i

                for i in range(1,baslangic):
                    cikarilacakToplam += i

                sonuc = asilToplam-cikarilacakToplam
                self.yazi.setText("Toplam: {}".format(sonuc))
        elif (baslangic < 0 or bitis < 0):
            self.yazi.setText("Hatalı veri girişi, lütfen pozitif sayı giriniz.")
        else:
            self.yazi.setText("Hatalı veri girişi, lütfen pozitif sayı giriniz.")
            
uygulama = QApplication(sys.argv)
pencere = GaussSum()
sys.exit(uygulama.exec_())


# In[ ]:




