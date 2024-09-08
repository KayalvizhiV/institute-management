from ..models.institute_model import InstituteModel
from ..serializers.institute_serializer import InstituteSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets

from django.shortcuts import get_object_or_404

# def get_inst(request):
#     if request.method == "GET":
#         inst = InstituteModel.objects.all()
#         serializer = InstituteSerializer(inst)
#         return Response(serializer.data)
#         # return HttpResponse(serializer.data,status = 200)

class InstituteView(viewsets.ViewSet):

    def create_inst(self,request):
        if request.method == "POST":
            serializer = InstituteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Created Successfully", "result": serializer.data},status = 201)
            return Response(serializer.errors)

    def retrieve(self,request):
        if request.method == "GET":
            inst = InstituteModel.objects.all()
            serializer = InstituteSerializer(inst, many=True)
            return Response(serializer.data)
            # return HttpResponse(serializer.data,status = 200)

    def get_inst_by_name(self,request, name):
        if request.method == "GET":
            inst = InstituteModel.objects.filter(inst_name=name)
            if len(inst) > 0:
                serializer = InstituteSerializer(inst, many=True)
                return Response(serializer.data, status = 200)
            else :
                return Response({'success': False,'message': f"'{name}' doesn't exist."},status=400)

    def get_inst_by_id(self,request,id):
        if request.method == "GET":
            try:
                inst = InstituteModel.objects.get(inst_id=id)
                serializer = InstituteSerializer(inst, many=True)
                if serializer.is_valid():
                    return Response(serializer.data, status = 200)
            except InstituteModel.DoesNotExist:
                return Response({'success': False,'message': f"INST_ID '{id}' doesn't exist."}, status=400)

    def update_inst_by_id(self,request,id):
        if request.method == "PUT":
            try:
                inst = InstituteModel.objects.filter(inst_id=id)
                serializer = InstituteSerializer(inst, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'success': True, 'result': serializer.data, 'message': 'Updated successfully'},status = 204)

            except InstituteModel.DoesNotExist:
                return Response({'success': False,'message': f"INST_ID '{id}' doesn't exist."},status=400)

    def delete_inst_by_name(self,request,name):
        if request.method == "DELETE":
            inst = InstituteModel.objects.filter(inst_name=name)
            if len(inst) > 0:
                inst.delete()
                return Response({'success': True , 'message': f'{name} deleted successfully'}, status = 204)
            else:
                return Response({'success': False,'message': f"'{name}' doesn't exist."},status=400)



