from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.organization_serializer import OrganizationSerializer
from ..models.organization_model import OrganizationModel
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(["POST"])
def create_org(request):
    if request.method == "POST":
        serializer_obj = OrganizationSerializer(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status = status.HTTP_201_CREATED )
        return Response(serializer_obj.data, status = status.HTTP_400_BAD_REQUEST )
        

@api_view(["GET"])
def get_org(request):
    if request.method == "GET":
        org_model = OrganizationModel.objects.all()
        serializer = OrganizationSerializer(org_model, many=True)
        return Response(serializer.data)
        
@api_view(["GET"])
def get_org_by_name(request, name):
    if request.method == "GET":
        try:
            org_model = OrganizationModel.objects.filter(org_name=name)
            serializer = OrganizationSerializer(org_model, many=True)
            return Response(serializer.data, status = 200)
        except OrganizationModel.DoesNotExist:
            return Response({'success': False,'message': f"ORG_NAME {name} doesn't exist."}, status=400)

@api_view(['GET','PUT','DELETE','PATCH'])
def get_update_delete_by_id(request,id):
    try:
        queryset = OrganizationModel.objects.get(org_id = id)
        if request.method == "GET":
            serializer = OrganizationSerializer(queryset)
            return Response(serializer.data, status = 200)

        if request.method == 'PUT':
            serializer = OrganizationSerializer(queryset, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': serializer.data, 'message': 'Updated successfully'}, status = 204)

        if request.method == 'PATCH':
            serializer = OrganizationSerializer(queryset, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'result': serializer.data, 'message': 'Updated/Patch successfully'}, status = 204)

        if request.method == 'DELETE':
            queryset.delete()
            return Response({'message': 'Deleted successfully'}, status = 204)
        
    except OrganizationModel.DoesNotExist:
            return Response({'success': False,'message': f"ORG_ID {id} doesn't exist."}, status=400)

