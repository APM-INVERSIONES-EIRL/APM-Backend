from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProgressView(APIView):
    def get(self, request, *args, **kwargs):
        # Aquí iría la lógica para obtener la barra de progreso
        progress_data = {"progress": 75}  # Ejemplo

        return Response(
            {
                "status": "success",
                "progress": progress_data,
            },
            status=status.HTTP_200_OK
        )