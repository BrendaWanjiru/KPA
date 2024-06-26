from django.urls import path
from . import views
from .views import upload_image, gallery, delete_image
from .views import add_member, edit_member, delete_member, events
from .views import about_us, about_us_view
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('upload/', upload_image, name='upload_image'),
    path('gallery/', gallery, name='gallery'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('add/', views.add_member, name='add_member'),
    path('delete/<int:memberid>/', views.delete_member, name='delete_member'),
    path('events/', views.events, name='events'),
    path('about_us/', views.about_us, name='about_us'),
    path('about-us/', about_us_view, name='about_us'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)