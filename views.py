from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

@csrf_exempt
def get_age(request):
    day = request.GET.get('day')
    month = request.GET.get('month')
    year = request.GET.get('year')
    dob = str(year) + '-' + str(month) + '-' + str(day)
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    print(dob)
    today = datetime.date.today()
    age =  today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return HttpResponse(age)
