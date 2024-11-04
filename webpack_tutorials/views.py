from django.shortcuts import render

# Create your views here.
def webpack_index(request):
    return render(request, 'webpack_templ/index.html', {})