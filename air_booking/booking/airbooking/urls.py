from django.urls import path
from airbooking import views
app_name = 'airbooking'
urlpatterns=[
    path('details',views.get_view,name='clients'),
    path('postdata',views.post_view,name='post')
]
