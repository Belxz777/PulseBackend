from rest_framework import serializers
from .models import User, JobTitle, Project, Task


class UsersSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id',
                  'job_title_id',
                  'avatar', 
                  'age',
                  'first_name',
                  'last_name',
                  'father_name',
                  'position',
                  'login',
                  'password')
        # пароль не возвращать
        extra_kwargs = {'password': {'write_only': True},
        'login': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


        def update(self, instance, validated_data):
            instance.job_title_id = validated_data.get('job_title_id', instance.job_title_id)
            instance.age = validated_data.get('age', instance.age)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.father_name = validated_data.get('father_name', instance.father_name)
            instance.login = validated_data.get('login', instance.login)
            instance.password = validated_data.get('password', instance.password)
            instance.save()
            return instance


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ('id',
                  'name',)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'description',
                  'members'
                  )
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    
class GetProectsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = ('id',
                      'name',
                      'description',
                      'members',
                      'created_at',
                      )
        
class GetTasksSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = ('id',
                  'project_id',
                  'name',
                  'description',
                  'hoursToAccomplish',
                  'stageAt',
                  'priority',
                  'workers',
                  'created_at',
                      )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'project_id',
                  'name',
                  'description',
                  'hoursToAccomplish',
                  'stageAt',
                  'priority',
                  'workers',
                  )
    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    def updateStage(self, instance, validated_data):
        instance.stageAt = validated_data.get('stageAt', instance.stageAt)
        instance.save()
        return instance
