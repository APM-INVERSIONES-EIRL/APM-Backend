from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ProfileView(APIView):
    def put(self, request, *args, **kwargs):
        # Aquí iría la lógica para actualizar el perfil del candidato
        data = request.data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        cv_file = data.get('file')
        area = data.get('area')

        # Ejemplo de respuesta exitosa
        return Response(
            {
                "status": "success",
                "message": "Perfil actualizado",
            },
            status=status.HTTP_200_OK
        )