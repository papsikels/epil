from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import CustomerUser, Costume, Bookmark
from django.db import transaction
from django.db.models import Exists, OuterRef
import time
from django import template
from .form import RegistrationForm, ChangePasswordForm, EditProfileForm, CostumeForm, BookmarkForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404


@login_required
def update_product(request, pk):
    costume = get_object_or_404(Costume, pk=pk)

    if request.method == 'POST':
        form = CostumeForm(request.POST, request.FILES, instance=costume)
        if form.is_valid():
            form.save()
            return redirect(reverse('product', args=[pk]))
    else:
        form = CostumeForm(instance=costume)

    return render(request, 'pages/update_product.html', {'form': form})

@login_required
def delete_product(request, pk):
    costume = get_object_or_404(Costume, pk=pk)

    if request.method == 'POST':
        costume.delete()
        return redirect('homepage')  

    return render(request, 'pages/delete_product.html', {'costume': costume})


@login_required
def product(request, costume_id):
    costume = get_object_or_404(Costume, id=costume_id)
    user_review = costume.review_set.filter(user=request.user).first()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.costume = costume
            review.save()
    else:
        form = ReviewForm(instance=user_review)

    return render(request, 'pages/product.html', {'costume': costume, 'user_review': user_review, 'form': form})

@login_required(login_url='Login')
def bookmarked_costumes(request):
    profile_data = {
        'profile': request.user.profile.url if request.user.profile else None,
    }

    bookmarked_costumes = Costume.objects.filter(bookmarked_by=request.user)

    return render(request, "pages/bookmark.html", {'bookmarked_costumes': bookmarked_costumes, 'profile_data': profile_data})

@login_required(login_url='Login')
def toggle_bookmark(request, costume_id):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            costume = Costume.objects.get(pk=costume_id)
        except Costume.DoesNotExist:
            raise Http404("Costume does not exist")

        with transaction.atomic():
            if costume.is_bookmarked_by_user(request.user):
                Bookmark.objects.filter(user=request.user, costume=costume).delete()
                is_bookmarked = False
            else:
                Bookmark.objects.create(user=request.user, costume=costume)
                is_bookmarked = True

        return JsonResponse({'status': 'success', 'is_bookmarked': is_bookmarked})
    return JsonResponse({'status': 'error'})
    
@login_required
def edit_profile(request):
    profile_data = {
        'full_name': request.user.full_name,
        'email': request.user.email,
        'username': request.user.username,
        'contact_number': request.user.contact_number,
        'address': request.user.address,
        'profile': request.user.profile.url if request.user.profile else None,
        'status': request.user.status,
        'birthdate': request.user.birthdate,
        'date_created': request.user.date_created,
    }

    user = request.user

    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES, instance=user)
        password_form = ChangePasswordForm(user, request.POST)

        if password_form.is_valid():
            old_password = password_form.cleaned_data.get('old_password')
            new_password1 = password_form.cleaned_data.get('new_password1')
            new_password2 = password_form.cleaned_data.get('new_password2')

            if old_password and new_password1 and new_password2:
                password_form.save()
                update_session_auth_hash(request, user)

        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            return redirect('profile')

    else:
        profile_form = EditProfileForm(instance=user)
        password_form = ChangePasswordForm(user)

    return render(request, 'pages/editprofile.html', {'profile_data': profile_data, 'profile_form': profile_form, 'password_form': password_form})

@login_required(login_url='Login')
def profile(request):
    profile_data = {
        'full_name': request.user.full_name,
        'email': request.user.email,
        'username': request.user.username,
        'contact_number': request.user.contact_number,
        'address': request.user.address,
        'profile': request.user.profile.url if request.user.profile else None,
        'status': request.user.status,
        'birthdate': request.user.birthdate,
        'date_created': request.user.date_created,
    }

    return render(request, 'pages/profile.html', {'profile_data': profile_data})

def logout_view(request):
    logout(request)
    return redirect('homepage')


def home(request):
    if request.user.is_authenticated:
        profile_data = {
            'profile': request.user.profile.url if hasattr(request.user, 'profile') and request.user.profile else None,
            'status': request.user.status,
        }
    else:
        profile_data = {
            'profile': None,
            'status': 'guest',
        }

    if request.method == 'POST':
        form = CostumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
        else:
            print(form.errors)  
    else:
        form = CostumeForm()

    return render(request, 'pages/homepage.html', {'profile_data': profile_data, 'form': form})
    

@login_required(login_url='Login')
def child(request):
    profile_data = {
        'profile': request.user.profile.url if request.user.profile else None,
    }
    child_costumes = Costume.objects.filter(status='child').annotate(
        is_bookmarked_by_current_user=Exists(Bookmark.objects.filter(costume=OuterRef('pk'), user=request.user))
    )
    return render(request, "pages/child.html", {'child_costumes': child_costumes, 'profile_data': profile_data})


@login_required(login_url='Login')
def adult(request):
    profile_data = {
        'profile': request.user.profile.url if request.user.profile else None,
    }
    adult_costumes = Costume.objects.filter(status='adult').annotate(
        is_bookmarked_by_current_user=Exists(Bookmark.objects.filter(costume=OuterRef('pk'), user=request.user))
    )
    
    return render(request, "pages/adult.html", {'adult_costumes': adult_costumes, 'profile_data': profile_data})

def register(request):

    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            full_name = form.cleaned_data['full_name']

            if CustomerUser.objects.filter(email=email).exists():
                messages.error(request, 'Email address already exists. Please use a different email.')
            elif CustomerUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                messages.error(request, 'Password and confirm password do not match.')
            else:
                CustomerUser.objects.create_user(email=email, username=username, password=password, full_name=full_name)

                messages.success(request, 'Account registered successfully.')
                return redirect('Login')
        else:
            if 'confirm_password' in form.errors:
                messages.error(request, 'Password and confirm password do not match.')
            elif 'email' in form.errors:
                messages.error(request, 'Email address already exists. Please use a different email.')
            elif 'username' in form.errors:
                messages.error(request, 'Username already exists. Please choose a different username.')
            else:
                messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'pages/register.html', {'form': form})


def Login(request):

    if request.user.is_authenticated:
        return redirect('homepage')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome! Please log in or register.')
            return redirect('Login')
        else:
            messages.error(request, 'Invalid email or password.')


    return render(request, 'pages/login.html')



