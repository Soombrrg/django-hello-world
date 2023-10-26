from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.
def hello(request, user_name):
    context = {'name': user_name}
    return render(request, 'hello.html', context)

class GreetingView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")

def feedback(request):
    if request.method == "GET":
        return render(request, "feedback.html")
    else:
        data = request.POST
        name = data['name']
        review = data['user_feedback']
        print(name,review)
        return HttpResponse("Thank you for your answer")
