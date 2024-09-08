from django.urls import path
from ..views.organization_view import create_org,get_org, get_org_by_name,get_update_delete_by_id

urlpatterns = [
  path('insertorg', create_org, name="create_org"),
  path('getallorgs', get_org, name="get_org"),
  path('getorgbyname/<str:name>', get_org_by_name, name = "get_org_by_name"),
  path('getupdatedeletebyid/<int:id>', get_update_delete_by_id, name = "get_update_delete_by_id")
]