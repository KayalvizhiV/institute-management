from ..views.program_view import ProgramView
from django.urls import path

urlpatterns = [
   
   path("createprogram", ProgramView.as_view({'post': 'create_program'}), name = "create_program"),
   path("getallprogram", ProgramView.as_view({'get': 'get_program'}), name = "get_program" ),
   path("getprogrambyname/<str:name>", ProgramView.as_view({'get': 'get_program_by_name'}), name = "get_program_by_name" ),
   path("getprogrambyid/<str:id>", ProgramView.as_view({'get': 'get_program_by_id'}),name = "get_program_by_id" ),
   path("updateprogrambyid/<str:id>", ProgramView.as_view({'put':'update_program_by_id'}), name="update_program_by_id"),
   path("deleteprogrambyname/<str:name>", ProgramView.as_view({'delete':'delete_program_by_name'}), name="delete_program_by_name"),
   
]
