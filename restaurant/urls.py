# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('menu/items/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
