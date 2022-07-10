from django.shortcuts import render
from rest_framework.permissions import AllowAny
from django.views import View
from rest_framework.views import APIView
from .serializer import ResultSerializer
from .models import StudentModel, SubjectsModel
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ResultsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            subjects = []
            instance = StudentModel.objects.get(roll=pk)
            if instance.failed_subjects is not None:
                failed_subjects = list(instance.failed_subjects)
                for item in failed_subjects:
                    sub_instance = SubjectsModel.objects.filter(code=item)[0]
                    if sub_instance.name:
                        subjects.append(sub_instance.name)
                    else:
                        subjects.append(sub_instance.code)
        except instance.UnboundLocalError:
            raise NotFound('This Roll number does not exist.')
            return Response({"error" : "This Roll number does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error" : "This server is on a business trip"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResultSerializer(instance)
        return Response({"data": serializer.data, "sub": subjects}, status=status.HTTP_201_CREATED)
