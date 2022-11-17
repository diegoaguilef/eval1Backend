from django.shortcuts import render
from .forms import PrinterForm
from .models import Printer

# name="", description="",  serial_number="", brand="", is_wifi=False, price=0, stock=0,created_at=None
p1 = Printer(1, 'Deskjet 3000', 'impresora de excelente calidad', 'UK28903K', 'hp', False, 20000, 10, '2022-09-27')
p2 = Printer(2, 'Lasetjet 1600', 'impresora laser', 'HU435345', 'hp', True, 135000, 11, '2022-09-27')
p3 = Printer(3, 'SmartTank 515', 'impresora multifuncional', 'ST40', 'hp', True, 76000, 6, '2022-09-27')
p4 = Printer(4, 'EcoTank B4', 'IMpresora de larga duracion', 'BR78ET', 'brother', True, 67099, 10, '2022-09-29')
p5 = Printer(5, 'Multi Func 12', 'para todo tipo de impresiones', 'MT45b', 'brother', True, 120999, 14, '2022-09-30')
p6 = Printer(6, 'Laser Br', 'imprime como ningun otro', 'LS490', 'brother', True, 99999, 17, '2022-09-29')
p7 = Printer(7, 'LG Printer', 'impresora laser', 'KLG69784', 'lg', True, 135000, 11, '2022-09-27')
p8 = Printer(8, 'LG MultiFunc', ' multifuncional LG capable', 'LG69784', 'lg', True, 76000, 6, '2022-09-10')
p9 = Printer(9, 'Laser Print', 'Innovacion de LG en impresoras', 'LPSM445', 'lg', True, 345700, 87, '2022-09-22')
p10 = Printer(10, 'SM Multi Laser', 'impresora laser excelente', 'SML435', 'samsung', True, 120999, 11, '2022-09-22')

printers = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
# Create your views here.
def index(req):
    context = { 'printers': printers }
    return render(req, 'printers/index.html', context)

def home(req):
    context = { 'printers': printers }
    return render(req, 'home.html', context)

def whoweare(req):
    return render(req, 'whoweare.html')

def new(req):
    form = PrinterForm()
    printer = req.POST
    return render(req, 'printers/new.html', {'form': form})

def edit(req, printer_id):
    printer = None
    for p in printers:
        if str(p.id) == str(printer_id):
            printer = p

    form = PrinterForm(initial={
        'name': printer.name, 
        'description': printer.description, 
        'brand': printer.brand,
        'is_wifi': printer.is_wifi, 
        'stock': printer.stock, 
        'price': printer.price, 
        'serial_number': printer.serial_number, 'created_at': printer.created_at})

    return render(req, 'printers/edit.html', {'form': form, 'id': printer_id})

def show(req, printer_id):
    printer = None
    for p in printers:
        if str(p.id) == str(printer_id):
            printer = p
    
    context = { 'printer': printer }
    return render(req, 'printers/show.html', context)

def create(req):
    form = PrinterForm(req.POST)
    
    name = req.POST.get('name')
    description = req.POST.get('description')
    is_wifi = req.POST.get('is_wifi')
    brand = req.POST.get('brand')
    serial_number = req.POST.get('serial_number')
    price = req.POST.get('price')
    stock = req.POST.get('stock')
    created_at = req.POST.get('created_at')

    if form.is_valid():
        printer = Printer(len(printers) + 1, name, description,serial_number, brand,is_wifi, price, stock, created_at)
        printers.append(printer)
        return render(req, 'printers/show.html', {'form': form, 'printer': printer})
    else:
        return render(req, 'printers/new.html', {'form': form})

def update(req, printer_id):
    form = PrinterForm(req.POST)
    
    name = req.POST.get('name')
    description = req.POST.get('description')
    is_wifi = req.POST.get('is_wifi')
    brand = req.POST.get('brand')
    serial_number = req.POST.get('serial_number')
    price = req.POST.get('price')
    stock = req.POST.get('stock')
    created_at = req.POST.get('created_at')
    if form.is_valid():
        printer = Printer(printer_id, name, description,serial_number, brand,is_wifi, price, stock, created_at)
        for i in range(len(printers)):
            if printers[i].id == printer_id:
                printers[i] = printer
        return render(req, 'printers/show.html', {'form': form, 'id': printer_id, 'printer': printer})
    else:
        return render(req, 'printers/edit.html', {'form': form, 'id': printer_id})

def destroy(req, printer_id):
    for printer in printers:
        if printer.id == printer_id:
            printers.remove(printer)

    context = { 'printers': printers }
    return render(req, 'printers/index.html', context)
    