from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from triapp.models import host_UserData
from triapp.models import Property
from django.contrib import messages
import pymongo
from django.contrib.auth.hashers import make_password
import bcrypt
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User = get_user_model()
@csrf_exempt
def host_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone=request.POST.get('phone')
        password = request.POST.get('password')
        # Check if the username is already taken
        if User.objects.filter(email=email).exists():
            # return JsonResponse({'success': False, 'message': 'Username is already taken.'})
            context = {
                'error_message': 'Email is already taken. Please choose another email.'
            }
            return render(request, 'register.html', context)
        user_data = host_UserData(username=username, email=email, phone=phone, password=make_password(password))
        user_data.save()
        # Create the user``
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()
        return render(request,'home.html')
        # data = {
        #     'username': username,
        #     'email': email,
        #     'phone': phone,
        #     'password': password,
        # }       
        # return JsonResponse({'success': True, 'message': 'User created successfully.','data':data})
    else:
        return render(request, 'register.html')
@csrf_exempt
def host_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request,'home.html')
        else:
           messages.error(request, 'Invalid email or password.')
           return render(request, 'log.html')
    else:
        return HttpResponse('wel to login page')


# def get_data(request, email):
#     try:
#         obj = User.objects.get(email=email)
#     except User.DoesNotExist:
#         return HttpResponse('Object not found', status=404)
#     else:
#         return HttpResponse(f'The object with ID {id} has data: {obj.user_data}')
@csrf_exempt
def host_forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is not None:
            # If user exists, show them the form to enter new password
            return render(request, 'change.html', {'email': email})
        else:
            # If user doesn't exist, show error message
            messages.error(request, 'This email address does not exist.')
            return redirect('forgot_password')
    return render(request,'forgot.html')
@csrf_exempt

def host_change_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return HttpResponse('password not match')
        else:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return HttpResponse ('user not exit')
            user.set_password(password1)
            user.save()
            return redirect('home')
    return render(request,'change.html')

@login_required(login_url='login')
def home_page(request):
    if request.method == 'POST':
        # host = request.user.host_Userdata
        # property_list = Property.objects.filter(host=host)# Assuming you have a OneToOneField from User to host_UserData
        type = request.POST.get('type')
        rental_mode = request.POST.get('rental_mode')
        area = request.POST.get('area')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        description = request.POST.get('description')
        sleeping_arrangement = request.POST.get('sleeping_arrangement')
        washrooms = request.POST.get('washrooms')
        images = request.FILES.get('images')
        nearest_station_airport = request.POST.get('nearest_station_airport')
        nearest_station_bus = request.POST.get('nearest_station_bus')
        nearest_station_train = request.POST.get('nearest_station_train')
        photos = request.POST.get('photos')
        amenities = request.POST.get('amenities')
        preferred_guest = request.POST.get('preferred_guest')
        length_of_stay = request.POST.get('length_of_stay')
        
        owner = request.user
        property_data = {
            'owner':owner,
            'type': type,
            'rental_mode': rental_mode,
            'area': area,
            'city': city,
            'state': state,
            'pincode': pincode,
            'description': description,
            'sleeping_arrangement': sleeping_arrangement,
            'washrooms': washrooms,
            'images': images,
            'nearest_station_airport': nearest_station_airport,
            'nearest_station_bus': nearest_station_bus,
            'nearest_station_train': nearest_station_train,
            'photos': photos,
            'amenities': amenities,
            'preferred_guest': preferred_guest,
            'length_of_stay': length_of_stay,
        }
        property = Property(**property_data)
        property.save()
        return HttpResponse('sucess')
        # return redirect('home')
    return render(request,'home.html')

# def host_change_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')

#         # Check if any of the fields are empty
#         if not email or not password1 or not password2:
#             messages.error(request, 'Please fill in all the fields.')
#             # return redirect('change_password')
#             return render(request,'change.html')

#         if password1 != password2:
#             messages.error(request, 'Passwords do not match.')
#             return render(request,'change.html')
#         user = get_object_or_404(User, email=email)
#         user.set_password(password1)
#         user.save()
#         messages.success(request, 'Your password has been changed successfully.')
#         return render(request,'home.html')
#     return render(request,'change.html')

