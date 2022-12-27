from django.shortcuts import get_object_or_404, redirect, render

from users.models import User
from .forms import PrinterForm
from .models import Printer


# name="", description="",  serial_number="", brand="", is_wifi=False, price=0, stock=0,created_at=None
# p1 = Printer(1, 'Deskjet 3000', 'impresora de excelente calidad', 'UK28903K', 'hp', False, 20000, 10, '2022-09-27', None).save()
# p2 = Printer(2, 'Lasetjet 1600', 'impresora laser', 'HU435345', 'hp', True, 135000, 11, '2022-09-27', None).save()
# p3 = Printer(3, 'SmartTank 515', 'impresora multifuncional', 'ST40', 'hp', True, 76000, 6, '2022-09-27', None).save()
# p4 = Printer(4, 'EcoTank B4', 'IMpresora de larga duracion', 'BR78ET', 'brother', True, 67099, 10, '2022-09-29', None).save()
# p5 = Printer(5, 'Multi Func 12', 'para todo tipo de impresiones', 'MT45b', 'brother', True, 120999, 14, '2022-09-30', None).save()
# p6 = Printer(6, 'Laser Br', 'imprime como ningun otro', 'LS490', 'brother', True, 99999, 17, '2022-09-29', None).save()
# p7 = Printer(7, 'LG Printer', 'impresora laser', 'KLG69784', 'lg', True, 135000, 11, '2022-09-27', None).save()
# p8 = Printer(8, 'LG MultiFunc', ' multifuncional LG capable', 'LG69784', 'lg', True, 76000, 6, '2022-09-10', None).save()
# p9 = Printer(9, 'Laser Print', 'Innovacion de LG en impresoras', 'LPSM445', 'lg', True, 345700, 87, '2022-09-22', None).save()
# p10 = Printer(10, 'SM Multi Laser', 'impresora laser excelente', 'SML435', 'samsung', True, 120999, 11, '2022-09-22', None).save()
# Create your views here.
def index(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))

    printers = Printer.objects.all()
    context = { 'printers': printers, 'user': user}
    return render(req, 'printers/index.html', context)

def home(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    printers = Printer.objects.all()

    context = { 'printers': printers, 'user': user}
    return render(req, 'home.html', context)


def new(req):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    form = PrinterForm()
    printers = Printer.objects.all()

    context = { 'form': form, 'printers': printers, 'user': user}

    return render(req, 'printers/new.html', context)

def edit(req, printer_id):
    printer = None
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    printer = Printer.objects.get(pk=printer_id)
    form = PrinterForm(instance=printer)

    return render(req, 'printers/edit.html', {'form': form, 'id': printer_id, 'user': user})

def show(req, printer_id):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))

    printer = Printer.objects.get(pk=printer_id)
    context = { 'printer': printer, 'user': user }
    return render(req, 'printers/show.html', context)

def create(req):
    form = PrinterForm(req.POST, req.FILES)
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))

    if form.is_valid():
        form.save()
        printer = form.cleaned_data['printer']
        return render(req, 'printers/show.html', {'form': form, 'printer': printer, 'user': user})
    else:
        return render(req, 'printers/new.html', {'form': form, 'user': user})

def update(req, printer_id):
    user = None
    if req.session.get('_auth_user_id'):
        user = User.objects.get(pk=req.session.get('_auth_user_id'))
    printer = Printer.objects.get(pk=printer_id)
    form = PrinterForm(req.POST, req.FILES, instance=printer)
    context = {'form': form, 'id': printer_id, 'printer': printer, 'user': user}
    if form.is_valid():
        form.save()
        return render(req, 'printers/show.html', context)
    else:
        return render(req, 'printers/edit.html', context)

def destroy(req, printer_id):
    printers = Printer.objects.all()
    Printer.objects.get(pk=printer_id).delete()
    context = { 'printers': printers }
    return redirect('printers')
    