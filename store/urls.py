from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('about/blog/', views.blog, name='blog'),
    path('about/blog/blog-details/', views.blog_details, name='blog_details'),
    path('about/testimonials/', views.testimonials, name='testimonials'),
    path('about/terms/', views.terms, name='terms'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
