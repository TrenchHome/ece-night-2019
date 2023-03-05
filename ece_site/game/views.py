# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout

# from .models import Profile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.db import IntegrityError
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.db import transaction
from rest_framework.authtoken.models import Token
from .models import Profile
from datetime import datetime
import json

# Create your views here.

def main_page(request):
	return render(
        request, 'main.html', {'profile': Profile.objects.all()[:3],}
    )

def leaderboard(request):
    return render(
        request, 'leaderboard.html', {'profile': Profile.objects.all(),}
    )

@login_required
def gamePage(request):
	return render(request, 'game/game.html')

@login_required
def setname(request):
    try:
        if 'username' in request.GET:
            username = request.GET['username']
            if len(username) < 10 and len(username) != 0: 
                Profile.set_username(request.user, username=username)
                return redirect('/')

        player = Profile.get_profile(request.user)
        return render(
            request, 'setname.html', {'player': player}
        )
    except:
        player = Profile.get_profile(request.user)
        return render(
            request, 'setname.html', {'player': player}
        )

@login_required
def google_oauth(request):
	user = request.user
	profile = Profile.get_profile(user)
	request.session.set_expiry(settings.LOGIN_SESSION_TTL)                      # sets the exp. value of the session 
	login(request, user, backend='django.contrib.auth.backends.ModelBackend')   # the user is now logged in
	try:
		token = Token.objects.create(user=user)
	except IntegrityError:
		token = Token.objects.get(user=request.user)
	if user.username == '':
		httpResponse = redirect('/setname/')
	else: 
		httpResponse = redirect('/')

	httpResponse.set_cookie('nctu-ece-token', token.key)
	httpResponse.set_cookie('nctu-ece-id', user.id)
	httpResponse.set_cookie('nctu-ece-profile-id', profile.id)
	return httpResponse
	#return render(request, 'game/game.html')


def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def testu(request):
    return render(request, 'testu.html')