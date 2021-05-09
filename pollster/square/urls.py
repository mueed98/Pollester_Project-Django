# myapi/urls.pyfrom django.urls import include, path
from rest_framework import routers
from . import views
from django.urls import include, path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.index, name='index'),
    # path('<int:num>/', views.squareIt, name='squareIt'),

]