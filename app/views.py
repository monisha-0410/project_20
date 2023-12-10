from django.shortcuts import render

# Create your views here.
def bootstrap_document(request):
    return render(request,'bootstrap_document.html')

def boot(request):
    return render(request,'boot.html')

def strap(request):
    return render(request,'strap.html')


def magic(request):
    return render(request,'magic.html')

def black(request):
    return render(request,'black.html')

def white(request):
    return render(request,'white.html')

def disable(request):
    return render(request,'disable.html')