# from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
# from triapp.models import host_UserData
# from triapp.models import Property
# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# import pymongo
# from django.contrib.auth.hashers import make_password
# import bcrypt
# from django.contrib import messages
# from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required
# User = get_user_model()
# @csrf_exempt
# def host_signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone=request.POST.get('phone')
#         password = request.POST.get('password')
#         # Check if the username is already taken
#         if User.objects.filter(email=email).exists():
#             return JsonResponse({'success': False, 'message': 'Username is already taken.'})
#             # context = {
#                 # 'error_message': 'Email is already taken. Please choose another email.'
#             # }
#             # return render(request, 'register.html', context)
#         user_data = host_UserData(username=username, email=email, phone=phone, password=make_password(password))
#         user_data.save()
#         # Create the user``
#         user = User.objects.create_user(username=email, email=email, password=password)
#         user.save()
#         data = {
#             'username': username,
#             'email': email,
#             'phone': phone,
#             'password': password,
#         }       
#         return JsonResponse({'success': True, 'message': 'User created successfully.','data':data})
#     else:
#         return JsonResponse({'success': False, 'message': 'Invalid request method.'})
# @csrf_exempt
# def host_login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'success': True})
#         else:
#         #    messages.error(request, 'Invalid email or password.')
#             return JsonResponse({'success': False, 'error': 'Invalid login credentials'})
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method'})
#         # return HttpResponse('wel to login page')


# # def get_data(request, email):
# #     try:
# #         obj = User.objects.get(email=email)
# #     except User.DoesNotExist:
# #         return HttpResponse('Object not found', status=404)
# #     else:
# #         return HttpResponse(f'The object with ID {id} has data: {obj.user_data}')
# @csrf_exempt
# def host_forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             user = None
#         if user is not None:
#             # If user exists, show them the form to enter new password
#             return render(request, 'change.html', {'email': email})
#         else:
#             # If user doesn't exist, show error message
#             messages.error(request, 'This email address does not exist.')
#             return redirect('forgot_password')
#     return render(request,'forgot.html')
# @csrf_exempt

# def host_change_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         if password1 != password2:
#             return HttpResponse('password not match')
#         else:
#             try:
#                 user = User.objects.get(email=email)
#             except User.DoesNotExist:
#                 return JsonResponse({'error': 'No user with the given email exists.'})
#             user.set_password(password1)
#             user.save()
#             return JsonResponse({'success': 'Your password has been changed successfully.'})
#     return JsonResponse({'error': 'Invalid request method.'})
# @login_required(login_url='login')
# @csrf_exempt
# def home_page(request):
#     if request.method == 'POST':
#         # host = request.user.host_Userdata
#         # property_list = Property.objects.filter(host=host)# Assuming you have a OneToOneField from User to host_UserData
#         type = request.POST.get('type')
#         rental_mode = request.POST.get('rental_mode')
#         area = request.POST.get('area')
#         city = request.POST.get('city')
#         state = request.POST.get('state')
#         pincode = request.POST.get('pincode')
#         description = request.POST.get('description')
#         sleeping_arrangement = request.POST.get('sleeping_arrangement')
#         washrooms = request.POST.get('washrooms')
#         images = request.FILES.get('images')
#         nearest_station_airport = request.POST.get('nearest_station_airport')
#         nearest_station_bus = request.POST.get('nearest_station_bus')
#         nearest_station_train = request.POST.get('nearest_station_train')
#         photos = request.POST.get('photos')
#         amenities = request.POST.get('amenities')
#         preferred_guest = request.POST.get('preferred_guest')
#         length_of_stay = request.POST.get('length_of_stay')
        
#         owner = request.user
#         property_data = {
#             'owner':owner,
#             'type': type,
#             'rental_mode': rental_mode,
#             'area': area,
#             'city': city,
#             'state': state,
#             'pincode': pincode,
#             'description': description,
#             'sleeping_arrangement': sleeping_arrangement,
#             'washrooms': washrooms,
#             'images': images,
#             'nearest_station_airport': nearest_station_airport,
#             'nearest_station_bus': nearest_station_bus,
#             'nearest_station_train': nearest_station_train,
#             'photos': photos,
#             'amenities': amenities,
#             'preferred_guest': preferred_guest,
#             'length_of_stay': length_of_stay,
#         }
#         property = Property(**property_data)
#         property.save()
#         return JsonResponse({'success': ' successfully.'})
#         # return redirect('home')
#     # return render(request,'home.html')
#     return JsonResponse('invalid')

# # def host_change_password(request):
# #     if request.method == 'POST':
# #         email = request.POST.get('email')
# #         password1 = request.POST.get('password1')
# #         password2 = request.POST.get('password2')

# #         # Check if any of the fields are empty
# #         if not email or not password1 or not password2:
# #             messages.error(request, 'Please fill in all the fields.')
# #             # return redirect('change_password')
# #             return render(request,'change.html')

# #         if password1 != password2:
# #             messages.error(request, 'Passwords do not match.')
# #             return render(request,'change.html')
# #         user = get_object_or_404(User, email=email)
# #         user.set_password(password1)
# #         user.save()
# #         messages.success(request, 'Your password has been changed successfully.')
# #         return render(request,'home.html')
# #     return render(request,'change.html')

from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.response import Response
from django.views import View
from rest_framework.views import APIView
from triapp.models import host_UserData
from triapp.models import Property
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import serializers
from django.contrib import messages
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Property
from .serializers import PropertySerializer
import jwt
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from django.conf import settings
import json
from django.contrib.auth import get_user
from django.forms.models import model_to_dict
User = get_user_model()
@method_decorator(csrf_exempt, name='dispatch')
class HostSignupView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        username = jsonData.get('username')
        email = jsonData.get('email')
        phone = jsonData.get('phone')
        password = jsonData.get('password')
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'email is already taken.'})
        user_data = host_UserData(username=username, email=email, phone=phone, password=make_password(password))
        user_data.save()

        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        data = {
            'username': username,
            'email': email,
            'phone': phone,
            'password':make_password(password),
        }
        login(request, user)
        payload = {'user_id': user.id}
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return JsonResponse({'success': True, 'message': 'User created successfully.', 'data': data, 'token': str(token)})

@method_decorator(csrf_exempt, name='dispatch')
class HostLogView(View):
    def post(self, request):
        jsonData = json.loads(request.body)
        email = jsonData.get('email')
        password = jsonData.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            user_data = host_UserData.objects.get(email=email)
            data = {
                'user_id': user.id,
                'username': user_data.username,
                'email': user_data.email,
                'phone': user_data.phone,
                'password': user_data.password,
            }
            payload = {'user_id': user.id}
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
            return JsonResponse({'success': True,'token': str(token),'data': data})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid login credentials'})

@method_decorator(csrf_exempt, name='dispatch')
class HostForgotPasswordView(View):
    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'change.html', {'email': email})
        else:
            messages.error(request, 'This email address does not exist.')
            return redirect('forgot_password')
@method_decorator(csrf_exempt, name='dispatch')
class HostChangePasswordView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'})

        if not email:
            return JsonResponse({'error': 'Email is required.'})
        elif not password:
            return JsonResponse({'error': 'Password is required.'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return JsonResponse({'error': 'No user with the given email exists.'})

        user.set_password(password)
        user.save()
        return JsonResponse({'success': 'Your password has been changed successfully.'})
    

@csrf_exempt
def home_page(request):
    return HttpResponse('welcome to homepage')

class AddPropertyView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)  # Parse the JSON data from the request body
            owner_id = data.get('owner')
            owner = User.objects.get(id=owner_id)
            property_data = {
                'owner': owner,
                'property_type': data.get('property_type'),
                'number_properties': data.get('number_properties'),
                'property_model': data.get('property_model'),
                'property_name': data.get('property_name'),
                'house_number': data.get('house_number'),
                'postal_code': data.get('postal_code'),
                'city': data.get('city'),
                'landmark': data.get('landmark'),
                'instructions': data.get('instructions'),
                'number_of_bedrooms': data.get('number_of_bedrooms'),
                'beds': data.get('beds'),
                'living_room': data.get('living_room'),
                'other_spaces': data.get('other_spaces'),
                'shared_spaces': data.get('shared_spaces'),
                'allowed_guest': data.get('allowed_guest'),
                'bathroom': data.get('bathroom'),
                'number_of_bathrooms': data.get('number_of_bathrooms'),
                'no_of_separate_bathrooms': data.get('no_of_separate_bathrooms'),
                'apartment_size': data.get('apartment_size'),
                'general_amenities': data.get('general_amenities'),
                'cooking_cleaning_amenities': data.get('cooking_cleaning_amenities'),
                'other_amenities': data.get('other_amenities'),
                'outside_view': data.get('outside_view'),
                'email': data.get('email'),
                'free_meals': data.get('free_meals'),
                'paid_meals': data.get('paid_meals'),
                'parking': data.get('parking'),
                'parking_spots': data.get('parking_spots'),
                'languages': data.get('languages'),
                'price_per_night': data.get('price_per_night'),
                'price_per_week': data.get('price_per_week'),
                'price_per_month': data.get('price_per_month'),
                'house_rules': data.get('house_rules'),
                'photos': data.get('photos'),
                'gstin': data.get('gstin'),
                'pan': data.get('pan'),
                'aadhar': data.get('aadhar'),
                'state': data.get('state'),
                'area': data.get('area'),
                'bank_details':data.get('bank_details'),
                'locationState': data.get('locationState'),
            }
            property = Property(**property_data)
            property.save()
            saved_property_data = model_to_dict(property)
            return JsonResponse({'success': 'Property created successfully.', 'property': saved_property_data})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def get(self, request):
        return JsonResponse({'error': 'Invalid request.'})

'''
method_decorator(login_required(login_url='host_login'), name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class HomePageView(View):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            owner = request.user

            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]  # Get the token from the request headers
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            print(user_id)
            print(payload) 
            if user_id != request.user.id:
                raise PermissionDenied('You are not authorized to perform this action.')
            property_data = {
                'owner': owner,
                'property_type': request.POST.get('property_type'),
                'number_properties': request.POST.get('number_properties'),
                'property_model': request.POST.get('property_model'),
                'property_name': request.POST.get('property_name'),
                'house_number': request.POST.get('house_number'),
                'postal_code': request.POST.get('postal_code'),
                'city': request.POST.get('city'),
                'landmark': request.POST.get('landmark'),
                'instructions': request.POST.get('instructions'),
                'number_of_bedrooms': request.POST.get('number_of_bedrooms'),
                'beds': request.POST.get('beds'),
                'living_room': request.POST.get('living_room'),
                'other_spaces': request.POST.get('other_spaces'),
                'shared_spaces': request.POST.get('shared_spaces'),
                'allowed_guest': request.POST.get('allowed_guest'),
                'bathroom': request.POST.get('bathroom'),
                'number_of_bathrooms': request.POST.get('number_of_bathrooms'),
                'no_of_separate_bathrooms': request.POST.get('no_of_separate_bathrooms'),
                'apartment_size': request.POST.get('apartment_size'),
                'general_amenities': request.POST.get('general_amenities'),
                'cooking_cleaning_amenities': request.POST.get('cooking_cleaning_amenities'),
                'other_amenities': request.POST.get('other_amenities'),
                'outside_view': request.POST.get('outside_view'),
                'meals_type': request.POST.get('meals_type'),
                'free_meals': request.POST.get('free_meals'),
                'paid_meals': request.POST.get('paid_meals'),
                'parking': request.POST.get('parking'),
                'parking_spots': request.POST.get('parking_spots'),
                'languages': request.POST.get('languages'),
                'price_per_night': request.POST.get('price_per_night'),
                'price_per_week': request.POST.get('price_per_week'),
                'price_per_month': request.POST.get('price_per_month'),
                'house_rules': request.POST.get('house_rules'),
                'photos': request.FILES.get('photos'),
                'gstin': request.POST.get('gstin'),
                'pan': request.POST.get('pan'),
                'aadhar': request.POST.get('aadhar'),
                'state': request.POST.get('state'),
                'area': request.POST.get('area'),
                'locationState': request.POST.get('locationState')
            }
            property = Property(**property_data)
            property.save()
            saved_property_data = {
                'owner': property.owner.username,
                'property_type': property.property_type,
                'number_properties': property.number_properties,
                'property_model': property.property_model,
                'property_name': property.property_name,
                'house_number': property.house_number,
                'postal_code': property.postal_code,
                'city': property.city,
                'landmark': property.landmark,
                'instructions': property.instructions,
                'number_of_bedrooms': property.number_of_bedrooms,
                'beds': property.beds,
                'living_room': property.living_room,
                'other_spaces': property.other_spaces,
                'shared_spaces': property.shared_spaces,
                'allowed_guest': property.allowed_guest,
                'bathroom': property.bathroom,
                'number_of_bathrooms': property.number_of_bathrooms,
                'no_of_separate_bathrooms': property.no_of_separate_bathrooms,
                'apartment_size': property.apartment_size,
                'general_amenities': property.general_amenities,
                'cooking_cleaning_amenities': property.cooking_cleaning_amenities,
                'other_amenities': property.other_amenities,
                'outside_view': property.outside_view,
                'meals_type': property.meals_type,
                'free_meals': property.free_meals,
                'paid_meals': property.paid_meals,
                'parking': property.parking,
                'parking_spots': property.parking_spots,
                'languages': property.languages,
                'price_per_night': property.price_per_night,
                'price_per_week': property.price_per_week,
                'price_per_month': property.price_per_month,
                'house_rules': property.house_rules,
                'gstin': property.gstin,
                'pan': property.pan,
                'aadhar': property.aadhar,
                'state': property.state,
                'area':property.area,
                'locationState':property.locationState,
                'created_at': property.created_at,
                'updated_at': property.updated_at,
            }

            return JsonResponse({'success': 'Property created successfully.','data':saved_property_data})
        
        except jwt.exceptions.DecodeError:
            return JsonResponse({'error': 'Invalid JWT token.'}, status=400)
        except jwt.exceptions.InvalidSignatureError:
            return JsonResponse({'error': 'Invalid JWT signature.'}, status=400)
        except PermissionDenied as e:
            return JsonResponse({'error': str(e)}, status=403)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
'''
'''  
class SearchResultsView(View):
    def get(self, request):
        query = request.GET.get('query')
        
        if query is not None:
            properties = Property.objects.filter(
                Q(type__icontains=query) | Q(description__icontains=query)
            ).values(
                'id', 'type', 'rental_mode','area','city','state', 'pincode', 'description',
                'sleeping_arrangement', 'washrooms', 'images', 'nearest_station_airport',
                'nearest_station_bus', 'nearest_station_train', 'photos', 'amenities',
                'preferred_guest', 'length_of_stay'
            )

            results = list(properties)
            return JsonResponse({'properties': results, 'query': query})
        
        return JsonResponse({'properties': [], 'query': query})
'''
@method_decorator(csrf_exempt, name='dispatch')
class SearchResultsView(View):
    def post(self, request):
        data = json.loads(request.body)
        query = data.get('query')
        properties = Property.objects.filter(
            Q(property_type__iexact=query) |
            Q(number_properties__iexact=query) |
            Q(property_model__iexact=query) |
            Q(property_name__iexact=query) |
            Q(house_number__iexact=query) |
            Q(postal_code__iexact=query) |
            Q(city__iexact=query) |
            Q(landmark__iexact=query) |
            Q(instructions__iexact=query) |
            Q(number_of_bedrooms__iexact=query) |
            Q(beds__iexact=query) |
            Q(living_room__iexact=query) |
            Q(other_spaces__iexact=query) |
            Q(shared_spaces__iexact=query) |
            Q(allowed_guest__iexact=query) |
            Q(bathroom__iexact=query) |
            Q(number_of_bathrooms__iexact=query) |
            Q(no_of_separate_bathrooms__iexact=query) |
            Q(apartment_size__iexact=query) |
            Q(general_amenities__iexact=query) |
            Q(cooking_cleaning_amenities__iexact=query) |
            Q(other_amenities__iexact=query) |
            Q(outside_view__iexact=query) |
            Q(bank_details__iexact=query) |
            Q(free_meals__iexact=query) |
            Q(paid_meals__iexact=query) |
            Q(parking__iexact=query) |
            Q(parking_spots__iexact=query) |
            Q(languages__iexact=query) |
            Q(price_per_night__iexact=query) |
            Q(price_per_week__iexact=query) |
            Q(price_per_month__iexact=query) |
            Q(house_rules__iexact=query) |
            Q(gstin__iexact=query) |
            Q(pan__iexact=query) |
            Q(aadhar__iexact=query) |
            Q(state__iexact=query) |
            Q(is_active=True)
            ).values(
                'id', 'owner__username', 'property_type', 'number_properties', 'property_model', 'property_name',
                'house_number', 'postal_code', 'city', 'landmark', 'instructions', 'number_of_bedrooms', 'beds',
                'living_room', 'other_spaces', 'shared_spaces', 'allowed_guest', 'bathroom', 'number_of_bathrooms',
                'no_of_separate_bathrooms', 'apartment_size', 'general_amenities', 'cooking_cleaning_amenities',
                'other_amenities', 'outside_view', 'meals_type', 'free_meals', 'paid_meals', 'parking', 'parking_spots',
                'languages', 'price_per_night', 'price_per_week', 'price_per_month', 'house_rules', 'gstin', 'pan',
                'aadhar', 'state', 'created_at', 'updated_at'
            )

        results = list(properties)
        if len(results) == 0:
            return JsonResponse({'message': 'No matching properties found for the query'})
        else:
            response = {'properties': results, 'query': query}
            return JsonResponse(response)


class AllPropertiesView(View):
    def get(self, request):
        properties = Property.objects.all().values(
            'id', 'property_type', 'number_properties', 'property_model', 'property_name',
            'house_number', 'postal_code', 'city', 'landmark', 'instructions',
            'number_of_bedrooms', 'beds', 'living_room', 'other_spaces', 'shared_spaces',
            'allowed_guest', 'bathroom', 'number_of_bathrooms', 'no_of_separate_bathrooms',
            'apartment_size', 'general_amenities', 'cooking_cleaning_amenities', 'other_amenities',
            'outside_view', 'email', 'free_meals', 'paid_meals', 'parking', 'parking_spots',
            'languages', 'price_per_night', 'price_per_week', 'price_per_month', 'house_rules',
            'photos', 'gstin', 'pan', 'aadhar', 'state', 'is_active', 'is_deleted',
            'created_at', 'updated_at'
        )
        results = list(properties)
        return JsonResponse({'properties': results})
from django.shortcuts import get_object_or_404
class PropertyDetailView(View):
    def get(self, request, property_id):
        property = get_object_or_404(Property, id=property_id)
        nights = int(request.GET.get('nights', 0))  # Assuming the user provides the number of nights in the request query parameter

        total_price = property.calculate_total_price(nights)
        if total_price is not None:
            return JsonResponse({'total_price': total_price})
        else:
            return JsonResponse({'message': 'Invalid or unavailable price'}, status=400)
from django.db import models

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Property

@csrf_exempt
def get_property_data(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        days = int(request.POST.get('days'))

        properties = Property.objects.filter(city=city)

        result = []
        for property in properties:
            if 1 <= days <= 6:
                price_per_night = round(float(property.price_per_night) * days * 1.05, 2)
                data = {
                    'property_type': property.property_type,
                    'city': property.city,
                    'state': property.state,
                    'price_per_night': price_per_night,
                }
            elif days == 7:
                price_per_week = round(float(property.price_per_week) * 1.05, 2)
                data = {
                    'property_type': property.property_type,
                    'city': property.city,
                    'state': property.state,
                    'price_per_week': price_per_week,
                }
            elif days == 30:
                price_per_month = round(float(property.price_per_month) * 1.05, 2)
                data = {
                    'property_type': property.property_type,
                    'city': property.city,
                    'state': property.state,
                    'price_per_month': price_per_month,
                }
            elif 7 < days < 30:
                price_per_night = round(float(property.price_per_night) * days * 1.05, 2)
                data = {
                    'property_type': property.property_type,
                    'city': property.city,
                    'state': property.state,
                    'price_per_night': price_per_night,
                }
            else:
                # Handle invalid duration, return an error message or appropriate response
                continue
            result.append(data)
        return JsonResponse(result, safe=False)


    # ... your existing methods ...
def showSome(request):
    return HttpResponse ("welcome to my page")