from django.shortcuts import render

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)

    return render(request, 'app1/add.html')

def show_all(request):
    return render(request, 'app1/show_all.html', {'people': people})