from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from emp import views

router = DefaultRouter()

router.register(r'employee-list',views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
]