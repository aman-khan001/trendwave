from django.urls import path
from . import views
urlpatterns = [
    path('cart-details/', views.cartDetails, name="cartDetail"),
    path('add-cart/<int:product_id>/', views.add_to_cart, name="addCart"),
    path('remove-item/<int:item_id>/', views.remove_item, name="removeCart"),
    path('quantity/<int:item_id>/', views.quantity, name="quantity"),

]