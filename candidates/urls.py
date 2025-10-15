from django.urls import path
from .views.profile import ProfileView
from .views.progress import ProgressView
from .views.self_diagnosis import SelfDiagnosisView
from .views.bootcamp import BootcampView, BootcampDetailView
from .views.submission import SubmissionView

app_name = 'candidates'

urlpatterns = [

    #Actualizar el perfil del candidato.
    path('profile/', ProfileView.as_view(), name='profile'), #PUT
    
    #Obtener el progreso del candidato.
    path('progress/', ProgressView.as_view(), name='progress'), #GET
    
    #Registrar las respuestas del autodiagnóstico del candidato.
    path('self-diagnosis/', SelfDiagnosisView.as_view(), name='self_diagnosis'), #POST
    
    #Obtener los detalles generales del bootcamp.
    path('bootcamp/', BootcampView.as_view(), name='bootcamp'), #GET
    
    #Obtener detalles específicos de un día del bootcamp.
    path('bootcamp/<int:day>/', BootcampDetailView.as_view(), name='bootcamp_detail'), #GET
    
    #Subir un ejercicio o tarea completada por el candidato.
    path('submission/', SubmissionView.as_view(), name='submission'), #POST
]