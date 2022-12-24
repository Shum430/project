from django.db.models import Q
from rest_framework import generics

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .forms import *


from .models import *
from .serializers import TeamSerializer1


def index(request):
    context={
        'best_teams':Team.objects.order_by('-points')[:5],
        'newses': News.objects.order_by('title'),
        'matches': Match.objects.order_by('team1')[:5],
        'events': Event.objects.order_by('name'),
        # 'podcasts': Podcast.objects.order_by('')
    }
    return render(request, template_name='hltv/index.html',
                  context=context)


class MatchListView(ListView):
    model=Match
    queryset=Match.objects.order_by('team1')
    context_object_name='all_matches'


class MatchDetailView(DetailView):
    model=Match


    extra_context = {
        'mcf':MatchCommentForm(),
    }


class EventListView(ListView):
    model=Event
    queryset=Event.objects.order_by('name')
    context_object_name='all_events'

class EventDetailView(DetailView):
    model=Event


class TeamListView(ListView):
    model=Team
    queryset = Team.objects.order_by('rank')
    context_object_name = 'all_teams'
    extra_context={
        'player': Player,
    }

class TeamDetailView(DetailView):
    model=Team

    extra_context = {
        'players':Player.objects.order_by('id'),
    }



class PlayerListView(ListView):
    model=Player
    queryset = Player.objects.order_by('-rating')
    context_object_name = 'all_players'

class PlayerDetailView(DetailView):
    model=Player


class PodcastListView(ListView):
    model=Podcast
    queryset=Podcast.objects.order_by('name')
    context_object_name='all_podcasts'


class PodcastDetailView(DetailView):
    model=Podcast



class NewsListView(ListView):
    model=News
    queryset=News.objects.order_by('title')
    context_object_name='all_newses'


class NewsDetailView(DetailView):
    model=News


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('hltv:index'))

def login_page(request):
    return render(request, 'hltv/login.html')


def user_login(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user= authenticate(request, username=username, password=password)
    if user:
        login(request,user)
        return HttpResponseRedirect(reverse('hltv:index'))
    else:
        context={
            'message':'incorrect login or password',
        }
        return render(request,'hltv/login.html',context=context)



def add_new_comment(request,pk):
    match=Match.objects.get(pk=pk)
    author=request.user
    text=request.POST.get('text')
    if match and author and text:
        new_comment=MatchComment(text=text,author=author,match=match)
        new_comment.save()

    return  HttpResponseRedirect(match.url_detail())



def change_fav_status(request,pk):
    user=request.user
    team=Team.objects.get(pk=pk)
    if user in team.fans.all():
        team.fans.remove(user)

    else:
        team.fans.add(user)


    return HttpResponseRedirect(team.url_detail())


def configure_page(request):
    context={
        'tf': TeamForm(),
    }
    return render(request,template_name='hltv/config.html',
                  context=context)


def add_new_team(request):
    f = TeamForm(request.POST)
    if f.is_valid():
        new_team=f.save(commit=False)
        if 'trophies'  in request.FILES:
            new_team.trophies=request.FILES['trophies']
        if 'logo'  in request.FILES:
            new_team.logo=request.FILES['logo']
        new_team.save()
        return HttpResponseRedirect(reverse('hltv:team-list'))
    else:
        print(f.errors)
        return HttpResponseRedirect(reverse('hltv:config'))


def search(request):
    match = request.POST.get('match')
    if match:
        teams= Team.objects.filter(name__icontains=match)
        players= Player.objects.filter( Q(first__icontains=match) |
                                        Q(last__icontains=match) |
                                        Q(nickname__icontains=match))
        events= Event.objects.filter(name__icontains=match)
        context={
            'match': match,
            'teams':teams,
            'players':players,
            'events':events,
        }
        return render(request,template_name='hltv/search.html',context=context)

    else:
        return HttpResponseRedirect(reverse('hltv:index'))



class TeamListAPIView(generics.ListAPIView):
    serializer_class = TeamSerializer1
    queryset = Team.objects.order_by('-points')




















