from django.urls import path, re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('search/', StudenSearch.as_view(), name='search'),
    path('', StudentHome.as_view(), name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('about/', about, name='about'),
    path('addpage/', AddObhodnoi.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowStudent.as_view(), name='post'),
    # new paths
    path('pdf_view/', ViewPDF.as_view(), name='pdf_view'),
    path('pdf_download', DownloadPDF.as_view(), name="pdf_download"),
]
