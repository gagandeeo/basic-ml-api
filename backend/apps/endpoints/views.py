from rest_framework.response import Response
from rest_framework import viewsets, views
import json
from .models import MLRequest
from .serializers import MLRequestSerializer
from ..ml.income_happ.linear_regression import LinearRegressionAlgo
# Create your views here.


class MLRequestViewSet(viewsets.ModelViewSet):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()


class PredictView(views.APIView):

    def post(self, request, format=None):
        model = LinearRegressionAlgo()
        prediction = model.compute_prediction(request.data)
        ml_request = MLRequest(
            input_data=json.dumps(request.data),
            full_response=prediction,
            response='Done',
            feedback="",
        )
        ml_request.save()

        return Response(prediction)
