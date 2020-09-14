from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.models import Employee
from .serializers import EmployeeSerializer,EmployeeDeSerializer


class EmployeeAPIView(APIView):
    def get(self,request,*args,**kwargs):
        user_id=kwargs.get("id")

        if user_id:
            emp_obj=Employee.objects.get(pk=user_id)
            emp_ser=EmployeeSerializer(emp_obj).data

            return Response({
                "status":200,
                "message":"查询单个用户成了",
                "results": emp_ser
            })
        else:
            object_all=Employee.objects.all()
            all__data=EmployeeSerializer(object_all,many=True).data

            return Response({
                "status":200,
                "message":"查询所有用户成功",
                "results":all__data,
            })

    def post(self,request,*args,**kwargs):
        user_data=request.data

        if not isinstance(user_data,dict) or user_data=={}:
            return Response({
                "status":400,
                "message":"请求格式有误"
            })
        serializer=EmployeeDeSerializer(data=user_data)

        if serializer.is_valid():
            emp_obj=serializer.save()
            return Response({
                "status":200,
                "mwssage": "用户保存成功",
                "results":EmployeeDeSerializer(emp_obj).data
            })
        return Response({
            "status":400,
            "message":serializer.errors
        })