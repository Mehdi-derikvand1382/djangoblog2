from django.shortcuts import render, HttpResponse

def about(request):
    # return HttpResponse("hi,this is about page")
    return render(request, 'about.html')

def home(request):
    # return HttpResponse("home")
    return render(request, 'home.html')

#def weblog(request):
    # return render(request, 'weblog.html')

# def store(request):
    # return render(request, 'store.html')