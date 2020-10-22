from . import views, food_store
from django.urls import path


rapp= 'rapp'

urlpatterns= [

    #Generall url
    path('about-us/', views.Aboutview.as_view(), name='about'),

    #food store
    path('restaurant/', food_store.RestaurantFoodView.as_view(), name='home'),
    path('cart/', food_store.CartListView.as_view(), name= 'cart'),
    path('checkout/', food_store.CheckoutListView.as_view(), name= 'checkout'),
    path('base/', food_store.basehtml.as_view(), name= ''),

    #json response path
    path('update_item/', food_store.updateItem, name='update_item'),

    #Orders urls


    #Reservation url
    path('reservation/', views.Reservation_form, name='reservation'),
    # path('reservation/', views.ReservationFormView.as_view(), name='reservation')
]