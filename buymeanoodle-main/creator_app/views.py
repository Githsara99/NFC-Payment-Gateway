from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from cryptomus import Client
from .forms import PassengerForm, PassengerRegForm, AdminPassengerRegForm, ChildrenRegForm, ChildCardForm, AdultsRegForm, AdultsCardForm
from .models import Passenger, Passenger_Reg, Admin_Passenger_Reg, Children_form, ChildCard_form, Adults_form, AdultsCard_form
import pyrebase
import uuid
import logging

# Logging configuration
logger = logging.getLogger(__name__)

MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

payment_client = Client.payment(PAYMENT_KEY, MERCHANT_UUID)

config = {
    "apiKey": "AIzaSyDB0fpsVB3K54VG56VNY1oNaGvCopY-yuc",
    "authDomain": "nfcdetails.firebaseapp.com",
    "databaseURL": "https://nfcdetails-default-rtdb.firebaseio.com",
    "projectId": "nfcdetails",
    "storageBucket": "nfcdetails.firebasestorage.app",
    "messagingSenderId": "1024977911201",
    "appId": "1:1024977911201:web:266a0f80919b3b07325fe0",
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Generic form handler
def handle_form(request, model, form_class, template_name, instance_id=0, redirect_url=None):
    if request.method == 'GET':
        if instance_id == 0:
            form = form_class()
        else:
            instance = get_object_or_404(model, pk=instance_id)
            form = form_class(instance=instance)
        return render(request, template_name, {"form": form})
    else:
        if instance_id == 0:
            form = form_class(request.POST)
        else:
            instance = get_object_or_404(model, pk=instance_id)
            form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if redirect_url:
                return redirect(redirect_url)
        return render(request, template_name, {"form": form})



def passenger_form(request, id=0):
    return handle_form(
        request, Passenger, PassengerForm, 'creator_app/passenger_form.html', instance_id=id,
        redirect_url='creator_app:passenger_list'
    )


def passenger_list(request):
    passengers = Passenger.objects.all()
    return render(request, 'creator_app/passenger_list.html', {'passenger_list': passengers})


def passenger_delete(request, id):
    passenger = get_object_or_404(Passenger, pk=id)
    passenger.delete()
    return redirect('creator_app:passenger_list')


def reg_passenger_form(request, id=0):
    return handle_form(
        request, Passenger_Reg, PassengerRegForm, 'creator_app/passenger_reg.html', instance_id=id,
        redirect_url='creator_app:reg_passenger_list'
    )


def reg_passenger_list(request):
    passengers1 = Passenger_Reg.objects.all()
    return render(request, 'creator_app/reg_passenger_list.html', {'reg_passenger_list': passengers1})


def reg_passenger_delete(request, id):
    passenger1 = get_object_or_404(Passenger_Reg, pk=id)
    passenger1.delete()
    return redirect('creator_app:reg_passenger_list')


def admin_passenger_form(request, id=0):
    return handle_form(
        request, Admin_Passenger_Reg, AdminPassengerRegForm, 'creator_app/admin_add_passenger.html',
        instance_id=id, redirect_url='creator_app:admin_passenger_list'
    )


def admin_passenger_list(request):
    passengers2 = Admin_Passenger_Reg.objects.all()
    return render(request, 'creator_app/admin_passenger_list.html', {'admin_passenger_list': passengers2})


def admin_passenger_delete(request, id):
    passenger2 = get_object_or_404(Admin_Passenger_Reg, pk=id)
    passenger2.delete()
    return redirect('creator_app:admin_passenger_list')

def passenger_home(request):
    return render(request, 'creator_app/passenger_home.html') 

def select_cat(request):
    return render(request, 'creator_app/select_cat.html')


ROUTE_PRICES = {
    ('Kaduwela', 'Kothalawala'): 50,
    ('Kothalawala', 'Malabe'): 40,
    ('Malabe', 'Thalangama'): 30,
    ('Thalangama', 'Koswatta'): 60,
    ('Koswatta', 'Battaramulla'): 70,
    ('Battaramulla', 'Welikada'): 80,
    ('Welikada', 'Rajagiriya'): 90,
    ('Rajagiriya', 'Ayurveda Junction'): 100,
    ('Ayurveda Junction', 'Castle Street'): 120,
    ('Castle Street', 'Devi Balika Junction'): 140,
    ('Devi Balika Junction', 'Senanayake Junction (Borella)'): 160,
    ('Senanayake Junction (Borella)', 'Horton Place'): 180,
    ('Horton Place', 'Liberty Junction'): 200,
    ('Liberty Junction', 'Kollupitiya (Station Road)'): 220,
}

def children_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = ChildrenRegForm(request.POST)
        else:
            child = get_object_or_404(Children_form, pk=id)
            form = ChildrenRegForm(request.POST, instance=child)
        
        if form.is_valid():
            # Save the form instance
            child = form.save(commit=False)

            # Calculate ticket price
            route = (child.c_from, child.c_to)
            child.price = ROUTE_PRICES.get(route, 0)  # Assign price or default to 0

            # Save the object to the database
            child.save()
            return redirect('creator_app:children_list')
    else:
        if id == 0:
            form = ChildrenRegForm()
        else:
            child = get_object_or_404(Children_form, pk=id)
            form = ChildrenRegForm(instance=child)

    return render(request, 'creator_app/children_form.html', {'form': form})


def children_list(request):
    children = Children_form.objects.all()
    return render(request, 'creator_app/children_list.html', {'children_list': children})


def children_delete(request, id):
    child = get_object_or_404(Children_form, pk=id)
    child.delete()
    return redirect('creator_app:children_list')



def childrenCard_form(request, id=0):
    return handle_form(
        request, ChildCard_form, ChildCardForm, 'creator_app/childCard_form.html', instance_id=id,
        redirect_url='creator_app:childCard_list'
    )

def childrCard_list(request):
    childCards = ChildCard_form.objects.all()
    return render(request, 'creator_app/childCard_list.html', {'childCard_list': childCards})



def childrenCard_delete(request, id):
    childCard = get_object_or_404(ChildCard_form, pk=id)
    childCard.delete()
    return redirect('creator_app:childCard_list')



def adults_form(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = AdultsRegForm(request.POST)
        else:
            adult = get_object_or_404(Adults_form, pk=id)
            form = AdultsRegForm(request.POST, instance=adult)
        
        if form.is_valid():
            # Save the form instance
            adult = form.save(commit=False)

            # Calculate ticket price
            route = (adult.a_from, adult.a_to)
            adult.price = ROUTE_PRICES.get(route, 0)  # Assign price or default to 0

            # Save the object to the database
            adult.save()
            return redirect('creator_app:adults_list')
    else:
        if id == 0:
            form = AdultsRegForm()
        else:
            adult = get_object_or_404(Adults_form, pk=id)
            form = AdultsRegForm(instance=adult)

    return render(request, 'creator_app/adults_form.html', {'form': form})


def adults_list(request):
    adults = Adults_form.objects.all()
    return render(request, 'creator_app/adults_list.html', {'adults_list': adults})


def adults_delete(request, id):
    adult = get_object_or_404(Adults_form, pk=id)
    adult.delete()
    return redirect('creator_app:adults_list')



def adultsCard_form(request, id=0):
    return handle_form(
        request, AdultsCard_form, AdultsCardForm, 'creator_app/adultsCard_form.html', instance_id=id,
        redirect_url='creator_app:adultsCard_list'
    )

def adultsCard_list(request):
    adultsCards = AdultsCard_form.objects.all()
    return render(request, 'creator_app/adultsCard_list.html', {'adultsCard_list': adultsCards})



def adultsCard_delete(request, id):
    adultCard = get_object_or_404(AdultsCard_form, pk=id)
    adultCard.delete()
    return redirect('creator_app:adultsCard_list')