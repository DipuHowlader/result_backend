from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializer import ResultSerializer
from .models import StudentModel, SubjectsModel
from rest_framework.response import Response
from rest_framework import status


class ResultsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        try:
            subjects = []
            instance = StudentModel.objects.get(roll=pk)
            if instance.failed_subjects is not None:
                failed_subjects = list(instance.failed_subjects)
                for item in failed_subjects:
                    sub_instance = SubjectsModel.objects.filter(id=1)
                    # if sub_instance[0].name:
                    #     subjects.append(sub_instance[0].name)
                    # else:
                    #     subjects.append(sub_instance.code)
        except UnboundLocalError:
            return Response({"error": "This Roll number does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # return Response({"error" : "This server is on a business trip"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ResultSerializer(instance)
        return Response({"data": str(sub_instance[0].code)}, status=status.HTTP_201_CREATED)
