from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'rent/index.html')
def property(request):
    return render(request, 'rent/property.html')
def propertyDetail(request):
    return render(request, 'rent/propertyDetail.html')
def wishListPage(request):
    return render(request, 'rent/wishListPage.html')
def userDashboard(request):
    return render(request, 'rent/userDashboard.html')
def dashboardHome(request):
    return render(request, 'rent/dashboardHome.html')
def schedule(request):
    return render(request, 'rent/schedule.html')
def help(request):
    return render(request, 'rent/help.html')
def account(request):
    return render(request, 'rent/account.html')
def about(request):
    return render(request, 'rent/about.html')
def tenant(request):
    return render(request, 'rent/tenant.html')
def signUp(request):
    return render(request, 'rent/signUp.html')
def login(request):
    return render(request, 'rent/login.html')