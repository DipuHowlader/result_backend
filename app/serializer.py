from rest_framework import serializers
from .models import StudentModel


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['roll', 'passed', 'result', 'failed_subjects']