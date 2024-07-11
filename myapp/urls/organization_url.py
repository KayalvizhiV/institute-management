from django.urls import path
from ..views.organization_view import create_org,get_org

urlpatterns = [
  # path('user/', OrganizationView.as_view()),
  # path('organization/<str:org_name>/<str:org_short_name>/', OrganizationView.as_view()),
  path('insertorg', create_org,name="create_org"),
  path('getorg',get_org,name="get_org")
]