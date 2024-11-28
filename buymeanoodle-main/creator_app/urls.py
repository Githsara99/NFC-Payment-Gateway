# from django.contrib.auth import views as auth_views
# from django.urls import path
# from . import api
# from . import views

# app_name = 'creator'

# urlpatterns = [
#     path('api/create_support', api.create_support, name='api_create_support'),
#     path('mypage/', views.mypage, name="mypage"),
#     path('creators/', views.creators, name='creators'),
#     path('creators/<int:pk>', views.creator, name='creator'),
#     path('creators/<int:creator_id>/success/<int:support_id>', views.support_success, name='success'),
#     path('edit/', views.edit, name='edit'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', auth_views.LoginView.as_view(template_name='creator/login.html'), name='login'),
# ]


# from django.urls import path
# from . import views, api

# urlpatterns = [
#     path('reload-card/', views.reload_card_view, name='reload_card'),
#     path('purchase-ticket/', views.purchase_ticket_view, name='purchase_ticket'),
#     path('api/reload-card/', api.reload_card, name='api_reload_card'),
#     path('api/purchase-ticket/', api.purchase_ticket, name='api_purchase_ticket'),
#     path('api/bitcoin-payment/', api.bitcoin_payment, name='api_bitcoin_payment'),
# ]


# from django.contrib.auth import views as auth_views
# from django.urls import path
# from . import api
# from . import views

# app_name = 'creator'

# urlpatterns = [
#     #sample
#     path('create/', views.passenger_form, name="passenger_insert"),
#     path('list/', views.passenger_list, name="passenger_list"),
#     path('<int:id>/', views.passenger_form, name="passenger_update"),
#     path('delete/<int:id>', views.passenger_delete, name="passenger_delete"),
    
#     path('createReg/', views.reg_passenger_form, name="reg_passenger_insert"),
#     path('listReg/', views.reg_passenger_list, name="reg_passenger_list"),
#     path('<int:id>/', views.reg_passenger_form, name="reg_passenger_update"),
#     path('deleteReg/<int:id>', views.passenger_delete, name="reg_passenger_delete"),
    
#     path('admincreateReg/', views.reg_passenger_form, name="admin_reg_passenger_insert"),
#     path('adminlistReg/', views.reg_passenger_list, name="admin_reg_passenger_list"),
#     path('<int:id>/', views.reg_passenger_form, name="admin_reg_passenger_update"),
#     path('admindeleteReg/<int:id>', views.passenger_delete, name="admin_reg_passenger_delete"),
#     # Existing paths
#     path('api/create_support', api.create_support, name='api_create_support'),
#     path('mypage/', views.mypage, name="mypage"),
#     path('mypage/', views.creators, name='creators'),
#     path('creators/<int:pk>', views.creator, name='creator'),
#     path('creators/<int:creator_id>/success/<int:support_id>', views.support_success, name='success'),
#     path('edit/', views.edit, name='edit'),
#     path('signup/', views.signup, name='signup'),
#     path('login/', auth_views.LoginView.as_view(template_name='creator/login.html'), name='login'),
#     # Change `bitcoin/` to `bitcoin_transactions/`
#     path('bitcoin_transactions/', views.bitcoin_transactions, name='bitcoin_transactions'),
#     path('api/create_bitcoin_transaction/', views.create_bitcoin_transaction, name='create_bitcoin_transaction'),
#     path('api/cryptomus_callback/', views.cryptomus_callback, name='cryptomus_callback'),
# ]

from django.contrib.auth import views as auth_views
from django.urls import path
from . import api
from . import views

# Updated app_name to make it unique
app_name = 'creator_app'

urlpatterns = [
    
    path('create-payment/', views.create_payment, name='create_payment'),
    path('webhook/', views.webhook, name='webhook'),
    
    # Children URLs
    path('childCreate/', views.children_form, name="children_insert"),
    path('childList/', views.children_list, name="children_list"),
    path('childUpdate<int:id>/', views.children_form, name="children_update"),
    path('childDelete/<int:id>', views.children_delete, name="children_delete"),
    
    path('childCardCreate/', views.childrenCard_form, name="childrenCard_insert"),
    path('childCardList/', views.childrCard_list, name="childCard_list"),
    path('childCardUpdate/<int:id>/', views.childrenCard_form, name="childrenCard_update"),
    path('childCardDelete/<int:id>', views.childrenCard_delete, name="childrenCard_delete"),
    
    # Adults URLs
    path('adultsCreate/', views.adults_form, name="adults_insert"),
    path('adultsList/', views.adults_list, name="adults_list"),
    path('<int:id>/', views.adults_form, name="adults_update"),
    path('adultsDelete/<int:id>', views.adults_delete, name="adults_delete"),
    
    path('adultsCardCreate/', views.adultsCard_form, name="adultsCard_insert"),
    path('adultCardList/', views.adultsCard_list, name="adultsCard_list"),
    path('adultCardUpdate/<int:id>/', views.adultsCard_form, name="adultsCard_update"),
    path('adultCardDelete/<int:id>', views.adultsCard_delete, name="adultsCard_delete"),
    
    # Passenger URLs
    path('create/', views.passenger_form, name="passenger_insert"),
    path('list/', views.passenger_list, name="passenger_list"),
    path('passengerUpdate/<int:id>/', views.passenger_form, name="passenger_update"),
    path('delete/<int:id>', views.passenger_delete, name="passenger_delete"),
    
    # Registered Passenger URLs
    path('createReg/', views.reg_passenger_form, name="reg_passenger_insert"),
    path('listReg/', views.reg_passenger_list, name="reg_passenger_list"),
    path('reg/<int:id>/', views.reg_passenger_form, name="reg_passenger_update"),
    path('deleteReg/<int:id>', views.passenger_delete, name="reg_passenger_delete"),
    
    # Admin Registered Passenger URLs
    path('admin/createReg/', views.admin_passenger_form, name="admin_reg_passenger_insert"),
    path('admin/listReg/', views.admin_passenger_list, name="admin_passenger_list"),
    path('admin/<int:id>/', views.admin_passenger_form, name="admin_reg_passenger_update"),
    path('admin/deleteReg/<int:id>', views.admin_passenger_delete, name="admin_reg_passenger_delete"),
    
    path('passengerHome/', views.passenger_home, name="passenger_home"),
    path('selectCat/', views.select_cat, name="select_cat"),
    path('adminHome/', views.admin_home, name="admin_home"),
]
