
from django.http import HttpResponse
import datetime


def programmer_day(request):
    current_year = datetime.datetime.now().year
    programmer_day_date = datetime.datetime(current_year, 1, 1) + datetime.timedelta(days=255)
    return HttpResponse(f"День программиста в текущем году: {programmer_day_date.strftime('%d.%m.%Y')}")
