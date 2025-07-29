from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

@api_view(['GET'])
def PatientList(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def PatientCreate(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        "status": "success"
    })


@api_view(['PUT'])
def PatientUpdate(req,id):
    patient = Patient.objects.get(id=id)
    serializer = PatientSerializer(patient,data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response({
        "status": "success"
    })

@api_view(['delete'])
def PatientDelete(req,id):
    Patient.objects.filter(id=id).delete()
    return Response({
        "status": "success"
    })