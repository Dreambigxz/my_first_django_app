from . import views, category_views
from django.urls import path


urlpatterns= [

    path('', views.HomeListView.as_view(), name='product_store'),
    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('sports/', category_views.SportListView.as_view(), name='sports'),
    path('fashion/', category_views.FashionListView.as_view(), name='fashion'),
]