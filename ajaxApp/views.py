from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, "index.html")
    # return HttpResponse("hello")

# submit data
def new_user(request):
    print('running view', request.POST)

    User.objects.create(
        FullName = request.POST['fullname'],
        Email = request.POST['email'],
        Technology = request.POST['technology'],
    )

    users = User.objects.all()
    all_users = []

    for user in users:
        all_users.append(
            {
                'id': user.id,
                'fullname': user.FullName,
                'email': user.Email,
                'technology': user.Technology,
            }
        )

        

    return JsonResponse({'all_users': all_users[::-1]})