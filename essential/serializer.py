from rest_framework import serializers
from .models import User, JobTitle, Project, Task, Issue, Department


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
                  'login',
                  'password',
                  'position',
                  'department_id')
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
            instance.avatar = validated_data.get('avatar', instance.avatar)
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.father_name = validated_data.get('father_name', instance.father_name)
            instance.login = validated_data.get('login', instance.login)
            instance.password = validated_data.get('password', instance.password)
            instance.position = validated_data.get('position', instance.position)
            instance.department_id = validated_data.get('department_id', instance.department_id)
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
    

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id',
                  'name',
                  'head')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.head = validated_data.get('head', instance.head)
        instance.save()
        return instance
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id',
                  'name',
                  'description',
                  'members',
                  'created_at'
                  )

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.members.set(validated_data['members'])
        instance.save()
        return instance


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
                  'created_at',
                  )

    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.hoursToAccomplish = validated_data.get('hoursToAccomplish', instance.hoursToAccomplish)
        instance.stageAt = validated_data.get('stageAt', instance.stageAt)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.workers.set(validated_data['workers'])
        instance.save()
        return instance


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
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

    def update(self, instance, validated_data):
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.hoursToAccomplish = validated_data.get('hoursToAccomplish', instance.hoursToAccomplish)
        instance.stageAt = validated_data.get('stageAt', instance.stageAt)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.workers.set(validated_data['workers'])
        instance.save()
        return instance
