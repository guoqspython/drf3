from rest_framework import serializers
from rest_framework import exceptions

from api.models import Employee
from drf3 import settings

class EmployeeSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    salt=serializers.SerializerMethodField()

    def get_salt(self,obj):
        return "salt"

    gender=serializers.SerializerMethodField()

    def get_gender(self,obj):
        print(type(obj.gender))
        return obj.get_gender_display()

    pic=serializers.SerializerMethodField()

    def get_pic(self,obj):
        print(obj.pic)

        return "%s%s%s" %("http://127.0.0.1:8000",settings.MEDIA_URL,obj.pic)

class EmployeeDeSerializer(serializers.Serializer):
    username=serializers.CharField(
        max_length=8,
        min_length=2,
        error_messages={
            "max_length":"长度太长了",
            "min_length":"长度太短了"
        }
    )
    password=serializers.CharField()
    phone=serializers.CharField(min_length=11,required=True)

    re_pwd=serializers.CharField()
    def validate_username(self,value):
        if "小" in value:
            raise exceptions.ValidationError("用户名有误")

        return value

    def validate(self, attrs):
        pwd=attrs.get("password")
        re_pwd=attrs.get("password")
        if pwd != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")
        return attrs

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
