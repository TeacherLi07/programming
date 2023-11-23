from django.shortcuts import render

# Create your views here.
def indexpage(request):
    context = {}
    return render(request, 'index.html', context)

def dino_play(request):
    context = {}
    return render(request, 'dino-play.html', context)