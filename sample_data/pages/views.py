from django.shortcuts import render
from pages.models import Bio

# Create your views here.
def home(request):
    return render(request, "pages/home.html", {})

def bio_index(request):
    bios = Bio.objects.all()
    context = {
        "bios": bios
    }
    return render(request, "pages/bio_index.html", context)