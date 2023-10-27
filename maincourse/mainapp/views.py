from django.shortcuts import render, HttpResponse
from django.views import View
from django.core.files.storage import FileSystemStorage


def compl(func):
    def wrapper(*args, **kwargs):
        print('start:',func.__name__)
        original_result = func(*args, **kwargs)
        print('complite')
        return original_result
    return wrapper


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
    return render("page.html", {"color": "green"})

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

def new1(request):
    return render(request, 'my_template.html')

############
# class words_list(View):
#     def __init__(self, word1, word2):
#         self.words1 = [word1]
#         self.words2 = [word2]
#         add_to_file(word1, word2)

#     def new(self, request):
#         render(request, 'add_word.html')
@compl
def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


@compl
def read_from_file():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2

@compl
def add_word(request):
    if request.method == 'POST':
        add_to_file(request.POST['word1'], request.POST['word2'])
        return render(request, 'dict_home.html')
    return render(request, 'add_word.html')

@compl
def words_reading(request):
    words1, words2 = read_from_file()
    # print(words1)
    # print(dict(zip(words1, words2)))
    data = dict(zip(words1, words2))
    return render(request, 'words_list.html', {'data': data})
# print(read_from_file())

@compl
def home(request):
    context = {'Tittle': 'My dictionary'}
    return render(request, 'dict_home.html', context)