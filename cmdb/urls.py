from django.conf.urls import url
from django.urls import path
from cmdb import views
app_nime = 'cmdb'
urlpatterns=[
	path('base/', views.base),
	path('index/', views.index),
	path('dashboard/', views.dashboard),
	path('detail/', views.detail),

]