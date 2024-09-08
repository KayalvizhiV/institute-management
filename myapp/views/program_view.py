from ..models.program_model import ProgramModel
from ..serializers.program_serializer import ProgramSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets

class ProgramView(viewsets.ViewSet):

    def create_program(self,request):
        if request.method == "POST":
            prog_serializer = ProgramSerializer(data = request.data)
            if prog_serializer.is_valid():
                prog_serializer.save()
                return Response({"message": "Created Successfully", 'result': prog_serializer.data},status = 201)
            return Response(prog_serializer.errors)

    def get_program(self,request):
        if request.method == "GET":
            program = ProgramModel.objects.all()
            prog_serializer = ProgramSerializer(program, many=True)
            # return Response(prog_serializer.data)
            return HttpResponse(prog_serializer.data,status = 200)

    def get_program_by_name(self,request, name):
        if request.method == "GET":
            program = ProgramModel.objects.filter(program_name=name)
            if len(program) > 0:
                prog_serializer = ProgramSerializer(program, many=True)
                return Response(prog_serializer.data, status = 200)
            else:
                return Response({'success': False,'message': f"'{name}' doesn't exist."}, status=400)

    def get_program_by_id(self,request,id):
        if request.method == "GET":
            try:
                program = ProgramModel.objects.get(program_id=id)
                prog_serializer = ProgramSerializer(program)
                return Response(prog_serializer.data, status = 200)
            except ProgramModel.DoesNotExist:
                return Response({'success': False,'message': f"PROGRAM_ID '{id}' doesn't exist."},status=400)

    def update_program_by_id(self,request,id):
        if request.method == "PUT":
            try:
                program = ProgramModel.objects.get(program_id=id)
                prog_serializer = ProgramSerializer(program, data = request.data)
                if prog_serializer.is_valid():
                    prog_serializer.save()
                    return Response({'success': True, 'result': prog_serializer.data, 'message': 'Updated successfully'},status = 204)

            except ProgramModel.DoesNotExist:
                return Response({'success': False,'message': f"PROGRAM_ID '{id}' doesn't exist."},status=400)

    def delete_program_by_name(self,request,name):
        if request.method == "DELETE":
            program = ProgramModel.objects.filter(program_name=name)
            if len(program) > 0:
                property.delete()
                return Response({'success': True , 'message': f'{name} deleted successfully'}, status = 204)
            else:
                return Response({'success': False,'message': f"'{name}' doesn't exist."},status=400)

