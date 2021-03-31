from django.urls import path
from . import views

urlpatterns = [


    path('' ,
         views.contacts_list,
         name='contacts_all'),


   path('<int:contact_id>/<slug:contact_slug>/',
        views.select_contact,
        name='select_contact'),
   

   path('create_contact/',
        views.create_contact,
        name='create_contact'),
   

   path('update_contact/<pk>/',
        views.ContactUpdate.as_view(),
        name='update_contact'),
   
   
   path('delete_contact/<int:contact_id>/<slug:contact_slug>/',
        views.delete_contact,
        name='delete_contact'),
   

   path('confirm_delete/<int:contact_id>/<slug:contact_slug>/',
        views.delete_confirm,
        name='confirm_delete'),
   

   path('delete_email/<int:email_id>/',
        views.delete_email,
        name='delete_email'),
   

   path('sent/', views.emails_sent,name='emails_sent'),


   path('send/' , views.send_emails , name='send_emails'),

]