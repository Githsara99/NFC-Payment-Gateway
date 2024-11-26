# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect
# from cryptomus import Client
# from .forms import CreateForm
# from .models import Creator, Support
# import pyrebase

# MERCHANT_UUID = '621379c1-acca-4252-bd66-2e86bfcff04'
# PAYMENT_KEY = '1P9521ebLUosz8zANZEOlFTNreI6DkI8qKefuQaDWGzug8r3Wz7k3N2CEdIzj5OjgiaqUfVxismOqPND'

# config = {
#   "apiKey": "AIzaSyDB0fpsVB3K54VG56VNY1oNaGvCopY-yuc",
#   "authDomain": "nfcdetails.firebaseapp.com",
#   "databaseURL": "https://nfcdetails-default-rtdb.firebaseio.com",
#   "projectId": "nfcdetails",
#   "storageBucket": "nfcdetails.firebasestorage.app",
#   "messagingSenderId": "1024977911201",
#   "appId": "1:1024977911201:web:266a0f80919b3b07325fe0",
# }

# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()


# @login_required

# def firebase(request):
#     try:
#         # Attempt to fetch data
#         channel_name = database.child('Data').child('Name').get().val()
#         print(f"Retrieved data: {channel_name}")  # Debug log
#     except Exception as e:
#         # Log any errors
#         print(f"Error retrieving data: {e}")
#         channel_name = None

#     return render(request, 'creator/mypage.html', {
#         "channel_name": channel_name,
#     })


# def mypage(request):
#     creator = request.user.creator
#     supports = creator.supports.filter(is_paid=True)
#     total = 0
    
#     for support in supports:
#         total += support.amount
    
#     return render(request, 'creator/mypage.html', {
#         'creator': creator,
#         'supports': supports,
#         'total': total
#     })

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             return redirect('creator:login')
#         else:
#             print(form.errors)
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'creator/signup.html',{
#         'form': form
#     })
    

# def creators(request):
        
#     creators = Creator.objects.all()
        
#     return  render(request, 'creator/creators.html', {
#         'creators': creators
#     })
    
# def creator(request, pk):
        
#     creator = Creator.objects.get(pk=pk)
        
#     return  render(request, 'creator/creator.html', {
#         'creator': creator
#     })
    
# def support_success(request, creator_id, support_id):
#     # print('Support success')
#     # print(request)
#     # print(creator_id)
#     # print(support_id)
    
#     support = Support.objects.get(pk=support_id)
    
#     payment = Client.payment(PAYMENT_KEY, MERCHANT_UUID)
    
#     # print(support, support.cryptomus_uuid)
    
#     result = payment.info({
#         "uuid": f"{support.cryptomus_uuid}",
#         "order_id" : f"{support.id}"
#     })
    
#     print(result)
    
#     if result['payment_status'] == 'paid':
#         support.is_paid = True
#         support.save()
    
#     return  render(request, 'creator/success.html')

# def edit(request):
#     try:
#         creator = request.user.creator
        
#         if request.method == 'POST':
#             form = CreateForm(request.POST, request.FILES, instance=creator)
            
#             if form.is_valid():
#                 form.save()
                
#                 return redirect('core:index')
#         else:
#             form = CreateForm(instance=creator)        
#     except Exception:
#         if request.method == 'POST':
#             form = CreateForm(request.POST, request.FILES)
            
#             if form.is_valid():
#                 creator = form.save(commit=False)
#                 creator.user = request.user
#                 creator.save()
                
#                 return redirect('core:index')
#         else:
#             form = CreateForm()
    
#     return render(request, 'creator/edit.html', {
#         'form': form
#     })


# from django.shortcuts import render, redirect
# from .forms import TicketPurchaseForm, ReloadCardForm
# from .models import Ticket, ReloadCard, UserProfile
# from creator.models import Creator

# def reload_card_view(request):
#     if request.method == 'POST':
#         form = ReloadCardForm(request.POST)
#         if form.is_valid():
#             card_number = form.cleaned_data['card_number']
#             amount = form.cleaned_data['amount']
#             try:
#                 card = ReloadCard.objects.get(card_number=card_number)
#                 card.balance += amount
#                 card.save()
#                 return render(request, 'success.html', {'message': 'Card reloaded successfully!'})
#             except ReloadCard.DoesNotExist:
#                 return render(request, 'error.html', {'message': 'Card not found!'})
#     else:
#         form = ReloadCardForm()
#     return render(request, 'reload_card.html', {'form': form})

# def purchase_ticket_view(request):
#     if request.method == 'POST':
#         form = TicketPurchaseForm(request.POST)
#         if form.is_valid():
#             ticket_type = form.cleaned_data['ticket_type']
#             ticket_price = form.cleaned_data['ticket_price']
#             if request.user.userprofile.card_balance >= ticket_price:
#                 request.user.userprofile.card_balance -= ticket_price
#                 request.user.userprofile.save()
#                 Ticket.objects.create(user=request.user, ticket_type=ticket_type, ticket_price=ticket_price)
#                 return render(request, 'success.html', {'message': 'Ticket purchased successfully!'})
#             else:
#                 return render(request, 'error.html', {'message': 'Insufficient balance!'})
#     else:
#         form = TicketPurchaseForm()
#     return render(request, 'purchase_ticket.html', {'form': form})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from cryptomus import Client
from .forms import PassengerForm, PassengerRegForm, AdminPassengerRegForm, ChildrenRegForm
from .models import Passenger, Passenger_Reg, Admin_Passenger_Reg, Children_form
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