from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BootcampView(APIView):
    def get(self, request, *args, **kwargs):
        # Lógica para obtener los detalles del bootcamp
        bootcamp_data = {
            "days": [
                {"day_number": 1, "int": 5, "objectives": ["Objetivo 1"], "string": "Descripción"}
            ]
        }
        return Response(
            {
                "status": "success",
                "data": bootcamp_data,
            },
            status=status.HTTP_200_OK
        )

class BootcampDetailView(APIView):
    def get(self, request, day, *args, **kwargs):
        # Lógica para obtener detalles específicos de un día del bootcamp
        day_data = {
            "day_number": day,
            "int": 5,
            "objectives": ["Objetivo específico del día"],
            "string": f"Descripción del día {day}"
        }
        return Response(
            {
                "status": "success",
                "data": day_data,
            },
            status=status.HTTP_200_OK
        )
