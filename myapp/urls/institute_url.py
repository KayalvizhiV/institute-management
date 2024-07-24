from ..views.institute_view import InstituteView
from django.urls import path

urlpatterns = [

   path("createinstitute", InstituteView.as_view())

]
