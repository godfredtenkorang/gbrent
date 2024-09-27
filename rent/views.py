from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'rent/index.html')
def property(request):
    return render(request, 'rent/property.html')
def propertyDetail(request):
    return render(request, 'rent/propertyDetail.html')