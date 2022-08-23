from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults


def predict(request):
    return render(request, 'predict.html')


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        duration = float(request.POST.get('duration'))
        waiting = float(request.POST.get('waiting'))

        # Unpickle model
        model = pd.read_pickle(
            r"D:/Repo/django/project2/prediction/geyser.pickle")
        # Make prediction
        result = model.predict(
            [[duration, waiting]])

        classification = result[0]

        PredResults.objects.create(
            duration=duration, waiting=waiting, classification=classification)

        jsonResp = JsonResponse({'result': classification, 'duration': duration,
                                 'waiting': waiting},
                                safe=False)
    return jsonResp


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
