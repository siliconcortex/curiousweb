from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'handouts'

urlpatterns = [
    path('', views.Handouts.as_view(), name = 'main'),
    path('add/', views.AddHandout.as_view(), name='add'),
    path('addfile/<handoutpk>', views.AddHandoutFile.as_view(), name='addhandoutfile'),
    path('download/<filepk>', views.DownloadHandoutFile.as_view(), name='download'),
    path('detail/<handoutpk>', views.HandoutDetail.as_view(), name='detail'),
    path('delete/<handoutpk>', views.HandoutDelete.as_view(), name='delete'),

]