from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout_page'),
    path('detail/<int:pk>', CarShowroomDetailView.as_view(), name='detail'),
    path('auto_detail/<int:pk>', AutoDetailView.as_view(), name='auto_detail'),
    path('sale_detail/<int:pk>', SaleDetailView.as_view(), name='sale_detail'),
    path('assistant_detail/<int:pk>', AssistantDetailView.as_view(), name='assistant_detail'),
    path('brands_details/<int:pk>', BrandsDetailView.as_view(), name='brands_detail'),
    path('clients_details/<int:pk>', ClientsDetailView.as_view(), name='clients_detail'),
    
    path('', include([
        path('',CarShowroomListView.as_view(), name='car_s'),
    ])),
        
    path('auto/', include([
        path('',AutoListView.as_view(), name='auto'),
    ])),      
         
    path('sale/', include([
        path('',SaleListView.as_view(), name='sale'),
    ])),
                          
    path('assistant/', include([
        path('',AssistantListView.as_view(), name='assistant'),
    ])),
    
    path('brands/', include([
        path('',BrandsListView.as_view(), name='brands'),
    ])),
    
    path('clietns/', include([
        path('',ClientsListView.as_view(), name='clients'),
    ])),
    path('edit_page/', ClientCreateView.as_view(), name='edit_page'),
    path('update_client/<int:pk>', ClientUpdateView.as_view(), name='update_page_clients'),
    path('delete_client/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),
    
    path('edit_page_brands/', BrandsCreateView.as_view(), name='edit_page_brands'),
    path('update_page_brands/<int:pk>', BrandUpdateView.as_view(), name='update_page_brands'),
    path('delete_brand/<int:pk>', BrandDeleteView.as_view(), name='delete_brand'),
    
    path('edit_page_assistant/', AssistantCreateView.as_view(), name='edit_page_assistant'),
    path('update_page_assistant/<int:pk>', AssistantUpdateView.as_view(), name='update_page_assistant'),
    path('delete_assistant/<int:pk>', AssistantDeleteView.as_view(), name='delete_assistant'),
    
    path('edit_page_sale/', SaleCreateView.as_view(), name='edit_page_sale'),
    path('update_page_sale/<int:pk>', SaleUpdateView.as_view(), name='update_page_sale'),
    path('delete_sale/<int:pk>', SaleDeleteView.as_view(), name='delete_sale'),
    
    path('edit_page_auto/', AutoCreateView.as_view(), name='edit_page_auto'),
    path('update_page_auto/<int:pk>', AutoUpdateView.as_view(), name='update_page_auto'),
    path('delete_auto/<int:pk>', AutoDeleteView.as_view(), name='delete_auto'),
    
    path('edit_page_showrooms/', ShowroomCreateView.as_view(), name="edit_page_showrooms"),
    path('update_page_showrooms/<int:pk>', ShowroomUpdateView.as_view(), name="update_page_showrooms"),
    path('delete_showroom/<int:pk>', ShowroomDeleteView.as_view(), name='delete_showroom'),
]