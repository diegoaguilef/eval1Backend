from django.db import models

# Create your models here.
class Printer():
    _name = ""
    def __init__(self, id=None, name="", description="",  serial_number="", brand="", is_wifi=False, price=0, stock=0,created_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.serial_number = serial_number
        self.brand = brand
        self.is_wifi = is_wifi
        self.price = price
        self.stock = stock
        self.created_at = created_at

    def getName():
        return self.name
    
    def setName(name):
        self.name = name

    def getId():
        return self.id
        
    def setId(id):
        self.id = id

    def getDescription():
        return self.description

    def setDescription(description):
        self.description = description

    def getSerialNumber():
        return self.serial_number

    def setSerialNumber(serial_number):
        self.serial_number = serial_number

    def getBrand():
        return self.brand

    def setBrand(brand):
        self.brand = brand

    def getIsWifi():
        return self.is_wifi

    def setIsWifi(is_wifi):
        self.is_wifi = is_wifi
    
    def getPrice():
        return self.price

    def setPrice(price):
        self.price = price

    def getStock():
        return self.stock

    def setStock(stock):
        self.stock = stock

    def getCreatedAt():
        return self.created_at

    def setCreatedAt(created_at):
        self.created_at = created_at

    def __str__(self):
        return 'Impresora: %s, Description: %s, Serial: %s, Brand: %s, is_wifi: %s, Price: %s, Stock: %s, Created: %s'%(
            self.name, self.description, self.serial_number, self.brand, self.is_wifi, self.price, self.stock, self.created_at)

