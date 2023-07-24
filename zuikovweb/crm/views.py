from django.shortcuts import render
from .forms import OrderForm
# Create your views here.
from .models import Order
from telebot.sendmassage import sendTelegram


def main_page(request):
    form = OrderForm()
    dict_obj = {
        'form': form
    }
    return render(request, "./index.html", {'form': form})


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, "./thanks.html", {'name': name,
                                                 'phone': phone})
    else:
        return render(request, "./thanks.html")


def more_page(request):
    return render(request, './more.html')
