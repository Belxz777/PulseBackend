from rest_framework import serializers
from .models import User, JobTitle, Project, Task, UserWithTask


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
        # пароль не возвращать
        extra_kwargs = {'password': {'write_only': True}}

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
                  'description'
                  )
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',
                  'project_id',
                  'name',
                  'description'
                  )
    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class UserWithTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWithTask
        fields = ('id',
                  'user_id',
                  'project_id',
                  'task_id',
                  'status',
                  'work_date',
                  'work_time'
                  )
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.task_id = validated_data.get('task_id', instance.task_id)
        instance.status = validated_data.get('status', instance.status)
        instance.work_date = validated_data.get('work_date', instance.work_date)
        instance.work_time = validated_data.get('work_time', instance.work_time)
        instance.save()
        return instance