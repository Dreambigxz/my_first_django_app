from . import views, category_views, crud
from django.urls import path

#app_name = 'ecommerce'
urlpatterns= [

    path('', views.HomeListView.as_view(), name='product_store'),

    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('sports/', category_views.SportListView.as_view(), name='sports'),
    path('fashion/', category_views.FashionListView.as_view(), name='fashion'),


    path('cart/', views.CartListView.as_view(), name='cart'),
    path('checkout/', views.CheckOutListView.as_view(), name='checkout'),
    path('account/', views.Account.as_view(), name='account'),


    path('add-to-cart/<slug>/', views.AddtoCart, name='addtocart'),
    path('clear_cart/', views.ClearCart, name='clearcart'),
    path('increase_qty/<slug>/', views.IncreaseQty, name='increase'),
    path('decrease_qty/<slug>/', views.DecreaseQty, name='decrease'),
    path('deleteanitem/<slug>/', views.deleteanitem, name='delete_an_item'),
    path('rating/<slug>/', views.RatingViews.as_view(), name='rate'),
    path('process_rating/<slug>/', views.RAtingProcess, name='process_rating'),
    path('process_review/<slug>/', views.ProcessReviews, name='process_review'),

    path('payment/', views.payment, name='payment'),

    ##############CRUD###############
    path('edit_shipping_address/<int:pk>/', crud.UpdateShippingDetails.as_view(), name='edit_shipping_details'),
    path('add_product', crud.AccountDetails.as_view(), name='account_details'),
    path('update_shipping_address/<int:pk>/', crud.UpdateShippingAddress.as_view(), name='update_shipping_address'),
]