from django.http import HttpResponse
from datetime import datetime


def myproject(request):
    return HttpResponse('Привет это тестовое приложение Django')


def current_datetime(request):
    now = datetime.now()
    html = f"<html><body>Текущая дата и время: {now}</body></html>"
    return HttpResponse(html)


