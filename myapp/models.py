from django.db import models

class student(models.Model):
    cName = models.CharField(max_length=20, null=True)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=255, blank=True, default='')
    cLine1 = models.CharField(max_length=255, blank=True, default='')

    #新增資料欄先刪_pycache_
    #於db 執行SQL輸入CREATE TABLE "myApp_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cName" varchar(20) NULL, "cAddr" varchar(255) NOT NULL, "cBirthday" date NOT NULL, "cEmail" varchar(100) NOT NULL, "cPhone" varchar(50) NOT NULL, "cSex" varchar(2) NOT NULL)
    

    def __str__(self):
        return self.cName
# Create your models here.
