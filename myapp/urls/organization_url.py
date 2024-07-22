from django.urls import path
from ..views.organization_view import create_org,get_org, get_org_by_name,get_update_delete_by_id

urlpatterns = [
  # path('user/', OrganizationView.as_view()),
  # path('organization/<str:org_name>/<str:org_short_name>/', OrganizationView.as_view()),
  path('insertorg', create_org, name="create_org"),
  path('getorg', get_org, name="get_org"),
  path('getorgbyname/<str:name>', get_org_by_name, name = "get_org_by_name"),
  path('getupdatedeletebyid/<int:id>', get_update_delete_by_id, name = "get_update_delete_by_id")
]