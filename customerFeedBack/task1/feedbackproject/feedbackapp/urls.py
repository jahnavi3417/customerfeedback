from django.urls import path
from feedbackapp import views

urlpatterns=[
    path('',views.show_feedback,name='feedback'),
    path('edit/<int:pk>',views.feedback_view,name='edit'),
    path('add',views.addfeedback,name='add'),
  
   
]