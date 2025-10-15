from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SelfDiagnosisView(APIView):
    def post(self, request, *args, **kwargs):
        # Aquí iría la lógica para recibir el autodiagnóstico
        answers = request.data.get('answers', [])

        return Response(
            {
                "status": "success",
                "message": "Autodiagnóstico registrado",
            },
            status=status.HTTP_200_OK
        )