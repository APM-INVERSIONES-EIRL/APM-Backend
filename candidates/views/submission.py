from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SubmissionView(APIView):
    def post(self, request, *args, **kwargs):
        # Aquí iría la lógica para subir un ejercicio
        bootcamp_day = request.data.get('bootcamp_day')
        file = request.data.get('file')
        file_type = request.data.get('type')

        return Response(
            {
                "status": "success",
                "message": "Entrega registrada",
            },
            status=status.HTTP_200_OK
        )