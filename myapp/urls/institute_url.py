from ..views.institute_view import InstituteView
from django.urls import path

urlpatterns = [
   
   # path("getallinsts", InstituteView.get_inst, name = "get_inst"),
   path("getallinsts", InstituteView.as_view({'get': 'retrieve'}), name = "get_inst"),
   path("createinstitute", InstituteView.as_view({'post': 'create_inst'}), name = "create_inst"),
   path("getinstbyname/<str:name>", InstituteView.as_view({'get': 'get_inst_by_name'}), name = "get_inst_by_name" ),
   path("getinstbyid/<str:id>", InstituteView.as_view({'get': 'get_inst_by_id'}),name = "get_inst_by_id" ),
   path("updateinstbyid/<str:id>", InstituteView.as_view({'put':'update_inst_by_id'}), name="update_inst_by_id"),
   path("deleteinstbyname/<str:name>", InstituteView.as_view({'delete':'delete_inst_by_name'}), name="delete_inst_by_name"),
   
]
