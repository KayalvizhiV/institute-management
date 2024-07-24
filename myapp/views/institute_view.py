from ..models.institute_model import InstituteModel
from ..serializers.institute_serializer import InstituteSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response

class InstituteView(APIView):

    def post(self,request):
        if request.method == "POST":
            serializer = InstituteSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": serializer.data},status = 201)
            return Response(serializer.errors)
