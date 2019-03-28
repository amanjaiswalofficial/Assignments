"""cbvcrudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crudapp.views import StudentGetPost,GreetUser, StudentUpdate, StudentDelete, StudentRetrieve, StudentList
urlpatterns = [
    path('greet/',GreetUser, name = 'greet-user'),
    path('student/<int:pk>',StudentRetrieve.as_view()),
    path('student/<int:pk>/update',StudentUpdate.as_view()),
    path('student/<int:pk>/delete',StudentDelete.as_view()),
    path('student/add',StudentGetPost.as_view()),
    path('student/',StudentList.as_view()),
    path('admin/', admin.site.urls),
]
