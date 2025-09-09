from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    properties = LandForSale.objects.all()[:4]
    testiminials = Testimonial.objects.all()
    teams = TeamMember.objects.all()
    context = {
        'testimonials': testiminials,
        'properties': properties,
        'teams': teams
    }
    return render(request, 'rent/index.html', context)

# def categories(request):
#     all_categories = Category.objects.all()
#     return {'all_categories': all_categories}

# def list_category(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     return render(request, 'rent/list_category.html')



def house_for_rent(request):
    houses = HouseForRent.objects.all()
    context = {
        'houses': houses
    }
    return render(request, 'rent/house/house_for_rent.html', context)

def house_for_rent_detail(request, rent_slug):
    house = get_object_or_404(HouseForRent, slug=rent_slug)
    context = {
        'house': house
    }
    return render(request, 'rent/house/house_for_rent_detail.html', context)

def house_for_sale(request):
    
    houses = HouseForSale.objects.all()
    context = {
        'houses': houses
    }
    return render(request, 'rent/house/house_for_sale.html', context)


def house_for_sale_detail(request, sale_slug):
    house = get_object_or_404(HouseForSale, slug=sale_slug)
    context = {
        'house': house
    }
    return render(request, 'rent/house/house_for_sale_detail.html', context)




def about(request):
    return render(request, 'rent/about.html')
def tenant(request):
    return render(request, 'rent/tenant.html')




def faq(request):
 return render(request, 'rent/faq.html')


def propertyDetails(request):
 return render(request, 'rent/propertyDetails.html')



def land(request):
    lands = LandForSale.objects.all()
    context = {
        'lands': lands,
        'title': 'Land'
    }
    return render(request, 'rent/land/land.html', context)


def landDetail(request, land_slug):
    land = get_object_or_404(LandForSale, slug=land_slug)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        additional_requests = request.POST.get('additional_requests')
        
        # Here, you would typically save the booking information to the database
        # For example:
        Booking.objects.create(
            property=land,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            additional_requests=additional_requests
        )
        
        # Redirect to a success page or back to the land detail page
        return redirect('landDetail', land_slug=land.slug)
    context = {
        'land': land,
        'title': 'Land Detail'
    }
    return render(request, 'rent/land/landDetail.html', context)

def hostel(request):
    hostels = HostelForRent.objects.all()
    context = {
        'hostels': hostels,
        'title': 'Hostels'
    }
    return render(request, 'rent/hostel/hostel.html', context)

def hostelDetail(request, hostel_slug):
    hostel = get_object_or_404(LandForSale, slug=hostel_slug)
    context = {
        'hostel': hostel,
        'title': 'Hostel Detail'
    }
    return render(request, 'rent/hostel/hostelDetail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        
        message = request.POST['message']
        contacts = Contact(name=name, email=email, message=message)
        contacts.save()
        return redirect('contact')
    return render(request, 'rent/contact.html')
