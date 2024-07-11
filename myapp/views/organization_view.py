from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.organization_serializer import OrganizationSerializer
from ..models.organization_model import OrganizationModel
from rest_framework import status
from rest_framework.decorators import api_view

# class OrganizationView(APIView):
@api_view(["POST"])
def create_org(request):
    if request.method == "POST":
        serializer_obj = OrganizationSerializer(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status = status.HTTP_201_CREATED )
        # return Response(serializer_obj.data, status = status.HTTP_400_BAD_REQUEST )
        

@api_view(["GET"])
def get_org(request):
    if request.method == "GET":
        org_model = OrganizationModel.objects.all()
        serializer = OrganizationSerializer(org_model, many=True)
        print(serializer.data)
        return Response(serializer.data)
        # return Response(serializer_obj.data, status = status.HTTP_400_BAD_REQUEST )
        



