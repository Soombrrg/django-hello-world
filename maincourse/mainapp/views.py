from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage

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

def something(request):
    return render("page.html", {"digit": 2})

def something2(request):
    return render("page,html", {"color": "green"})

def upload_file(request):
    if requesr.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')