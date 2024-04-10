from django.urls import path, re_path, register_converter
from . import converters
from . import views

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.WomenTag.as_view(), name='tag'),
    path('edit/<int:pk>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePage.as_view(), name='delete_page'),
]