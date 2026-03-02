import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from . import global_app_settings

import requests
import json
import hashlib
import hmac
import base64

def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def getdetails(request):
    try:
        d = global_app_settings.GlobalAppSettings.EmbedDetails
    except Exception as e:
        return JsonResponse({'error': 'Could not load embed details', 'details': str(e)}, status=500)

    return JsonResponse({
        'DashboardId': d.DashboardId,
        'ServerUrl': d.ServerUrl,
        'EmbedType': d.EmbedType,
        'Environment': d.Environment,
        'SiteIdentifier': d.SiteIdentifier,
    })

@api_view(['POST'])
def authorization_server(request):
    body = json.loads(request.body.decode('utf-8'))
    embedQuerString = body.get("embedQuerString")
    dashboardServerApiUrl = body.get("dashboardServerApiUrl")
    embedQuerString = embedQuerString + "&embed_user_email=" + global_app_settings.GlobalAppSettings.EmbedDetails.UserEmail
    timeStamp = (datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()
    embedQuerString += "&embed_server_timestamp=" + str(timeStamp)
    embedDetailsUrl = "/embed/authorize?" + embedQuerString + "&embed_signature=" + get_signature_url(embedQuerString)
    result_content=requests.get(dashboardServerApiUrl + embedDetailsUrl)
    return HttpResponse(result_content)

def get_signature_url(message):
    EmbedSecret = global_app_settings.GlobalAppSettings.EmbedDetails.EmbedSecret
    keyBytes = bytes(EmbedSecret.encode('utf-8'))
    messageBytes = bytes(message.encode('utf-8'))
    hashMessage = base64.b64encode(hmac.new(keyBytes,messageBytes,digestmod=hashlib.sha256).digest())
    
    return str(hashMessage, "utf-8")            