from django.shortcuts import render

# Create your views here.
def register_view(request):
    """Return the registration template """
    return render(request, 'register.html')