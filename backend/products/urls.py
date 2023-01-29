from django.urls import path

from . import views 

urlpatterns = [
    # --- Class based views ---
    # path('', views.product_create_view),
    # path('list/', views.product_list_create_view),
    # path('<int:pk>/', views.product_detail_view)

    # --- Function based views ---
    path('', views.product_alt_view),
    path('<int:pk>/', views.product_alt_view)
]