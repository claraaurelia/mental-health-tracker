from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306217304',
        'name': 'Clara Aurelia Setiady',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
