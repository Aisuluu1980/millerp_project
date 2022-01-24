from . import views
from django.urls import path
from .views import IndexView, FinanceView, ProcurementView, SafetytView, HumanResoursesView, CustomerView, MobileView, DocumentView, MigrationView,\
    AboutView, AssetView, ContactCreateView, success


app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('success/', success, name='success_page'),
    path('finance/', FinanceView.as_view(), name='finance'),
    path('procurement/', ProcurementView.as_view(), name='procurement'),
    path('safety/', SafetytView.as_view(), name='safety'),
    path('hr/', HumanResoursesView.as_view(), name='hr'),
    path('customer/', CustomerView.as_view(), name='customer'),
    path('mobile/', MobileView.as_view(), name='mobile'),
    path('document/', DocumentView.as_view(), name='document'),
    path('migration/',MigrationView.as_view(), name='migration'),
    path('asset/',AssetView.as_view(), name='asset'),



 ]