from django.forms import CharField, ValidationError
from rest_framework import serializers
from .models import User, JobTitle
from django.contrib.auth.models import User as mUser

class UsersSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id',
                      'job_title_id',
                      'age',
                      'first_name',
                      'last_name',
                      'father_name',
                      'login',
                      'password')
            #пароль не возвращать
            extra_kwargs = {'password': {'write_only': True}}
            def create(self,validated_data):
                password = validated_data.pop('password',None)
                instance = self.Meta.model(**validated_data)
                if password is not None:
                   instance.set_password(password)  
                instance.save()
                return instance

class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ('id',
                  'name'
                  )
