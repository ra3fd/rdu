from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('search/', views.search, name='search'),
    path('qsls/', views.qsls, name='qsls'),
    path('statistics/', views.statistics, name='statistics'),
    path('random/', views.rand, name='rand'),
    path('period/', views.period, name='period'),
    path('new_calls/', views.new_calls, name='new_calls'),
    path('max_qso/', views.max_qso, name='max_qso'),
    path('call_allbands/', views.call_allbands, name='call_allbands'),
    path('call_allmode/', views.call_allmode, name='call_allmode'),
    path('call_allbands_mode/', views.call_allbands_mode, name='call_allbands_mode'),
    path('renew/', views.renew, name='renew'),

]
