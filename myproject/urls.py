from django.contrib import admin
from django.urls import path, include
from backend import views as backend_views
from blog import views as blog_views
from practice import views as practice_views
from frontend import views as frontend_views  # Import frontend views
from crud_app import views as crud_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Backend Views
    path('', backend_views.home, name='home'),
    path('thanveer/', backend_views.thanveer, name='thanveer'),

    # Blog Views
    path('blog/', blog_views.blog_home, name='blog_home'),

    # Practice App
    path('practice/', practice_views.practice_home, name='practice_home'),

    # Frontend Views (Newly Added)
    path('home/', frontend_views.home, name='home'),
    path('about/', frontend_views.about, name='about'),
    path('services/', frontend_views.services, name='services'),
    path('contact/', frontend_views.contact, name='contact'),

    # CRUD VIEWS
    path('crud/', crud_views.item_list, name='item_list'),
    path('crud/create/', crud_views.item_create, name='item_create'),
    path('crud/update/<int:id>/', crud_views.item_update, name='item_update'),
    path('crud/delete/<int:id>/', crud_views.item_delete, name='item_delete'),

    #students
    path('students/', include('student_record.urls')),
]
