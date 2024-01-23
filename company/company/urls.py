"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Employee_mgnt import views
from Department_mgnt import views as d
from Salary_mgnt import views as s

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',views.emp),
    # path('dep/',d.dep),
    # path('dep/reportpg/',d.rep),
    path('heirpg/<int:heir_id>/',d.heir,name='heir'),
    path('reportpgs/<int:sal_id>/', s.reps, name='reps')
]
