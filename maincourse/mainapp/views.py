from django.shortcuts import render

# Create your views here.
def hello(request, user_name):
    context = {'name': user_name}
    return render(request, 'hello.html', context)