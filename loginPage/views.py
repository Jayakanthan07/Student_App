from django.shortcuts import render

# Create your views here.
def loginView(request):
    context = {
    }
    return render(request, 'login.html', context)