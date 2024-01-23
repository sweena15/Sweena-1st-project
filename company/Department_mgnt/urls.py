from django.urls import path,include
from Department_mgnt import views 

urlpatterns=[
    path=('reportpg/',views.rep,name=rep),
    path=('heirpg/',views.rep,name=rep)
    
]