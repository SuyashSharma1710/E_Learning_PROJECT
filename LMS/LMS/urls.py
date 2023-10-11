
from django.contrib import admin
from django.urls import path, include
from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base',views.BASE,name='base' ),
    path('404',views.PAGE_NOT_FOUND,name='404' ),
    path('',views.HOME,name='home' ),

    path('courses',views.SINGLE_COURCE,name='single_course' ),
    path('courses/filter-data',views.filter_data,name="filter-data"),
    path('courses/<slug:slug>',views.COURSE_DETAILS,name="course_details"),
    path('search',views.SEARCH_COURSE,name="search_course"),
    path('contact_us',views.CONTACT_US,name='contact_us' ),

    path('about_us',views.ABOUT_US,name='about_us' ),
    path('doLogin',user_login.DO_LOGIN,name='do_login' ),

    path('accounts/register',user_login.REGISTER,name='register' ),
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/profile',user_login.PROFILE,name='profile' ),
    path('accounts/profile/update',user_login.PROFILE_UPDATE,name='profile_update' ),

    path('checkout/<slug:slug>',views.CHECKOUT,name='checkout' ),
    path('my-course',views.MY_COURSE,name='my_course' ),


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
