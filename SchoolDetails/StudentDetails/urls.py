from django.contrib import admin
from django.conf.urls import url
from StudentDetails import views
from django.urls import path

app_name = 'myApp'

urlpatterns = [  
    path('', views.SchoolListView.as_view(), name = 'school_list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail'),
    path('create/', views.SchoolCreateView.as_view(), name = 'create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = 'delete'),
    
]
# url(r'^$', views.CBView.as_view(), name="CBView"),
# url(r'^index/', views.IndexView.as_view(), name="IndexView"),
# url(r'^$', views.SchoolListView.as_view(), name="school_list"),
# url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name="detail"),
# url(r'^create/$', views.SchoolCreateView.as_view(), name="create")


# path(r'^update', views.SchoolUpdateView.as_view(), name = 'update'),
#     path(r'^delete', views.SchoolDeleteView.as_view(), name = 'delete'),
