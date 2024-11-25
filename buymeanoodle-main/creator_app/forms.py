# from django.forms import ModelForm
# from .models import Creator
 
 
# class CreateForm(ModelForm):
#     class Meta:
#         model = Creator
#         fields = ('title', 'description', 'image',)
 


# from django import forms

# class TicketPurchaseForm(forms.Form):
#     ticket_type = forms.CharField(max_length=100)
#     ticket_price = forms.DecimalField(max_digits=10, decimal_places=2)

# class ReloadCardForm(forms.Form):
#     card_number = forms.CharField(max_length=16)
#     amount = forms.DecimalField(max_digits=10, decimal_places=2)


from django.forms import ModelForm
from .models import Passenger, Passenger_Reg, Admin_Passenger_Reg
from django import forms 


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ('name', 'card_id', 'mobile', 'recharge', 'famount', 'balance',)
        labels ={
            'name':'Name',
            'card_id':'Card ID',
            'mobile':'Mobile',
            'recharge':'Recharge',
            'famount':'Final Amount',
            'balance':'Balance',   
        }
    
    def __init__(self, *args, **kwargs):
        super(PassengerForm,self).__init__(*args, **kwargs)
        self.fields['card_id'].required = False
        

class PassengerRegForm(forms.ModelForm):
    class Meta:
        model = Passenger_Reg
        fields = ('name', 'mobile','category', 'package', 'package')
        labels ={
            'name':'Name',
            'mobile':'Mobile',
            'category':'Category',
            'package':'Package',
        }
    
    def __init__(self, *args, **kwargs):
        super(PassengerRegForm,self).__init__(*args, **kwargs)
        self.fields['mobile'].required = False        


class AdminPassengerRegForm(forms.ModelForm):
    class Meta:
        model = Admin_Passenger_Reg
        fields = ('card_id1',)  # Add a comma to make it a tuple
        labels = {
            'card_id1': 'Card ID',
        }

    def __init__(self, *args, **kwargs):
        super(AdminPassengerRegForm, self).__init__(*args, **kwargs)
        self.fields['card_id1'].required = False
               