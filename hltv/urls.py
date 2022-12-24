from django.urls import path

from . import views

app_name='hltv'

urlpatterns=[
    path('',view=views.index,name='index'),
    path('match/all/',view=views.MatchListView.as_view(),name='match-list'),
    path('match/<int:pk>/',view=views.MatchDetailView.as_view(),name='match-detail'),
    path('event/all/',view=views.EventListView.as_view(),name='event-list'),
    path('event/<int:pk>/',view=views.EventDetailView.as_view(),name='event-detail'),
    path('team/all/',view=views.TeamListView.as_view(),name='team-list'),
    path('team/<int:pk>/',view=views.TeamDetailView.as_view(),name='team-detail'),
    path('player/all/',view=views.PlayerListView.as_view(),name='player-list'),
    path('player/<int:pk>/',view=views.PlayerDetailView.as_view(),name='player-detail'),
    path('podcast/all/',view=views.PodcastListView.as_view(),name='podcast-list'),
    path('news/all/',view=views.NewsListView.as_view(),name='news-list'),
    path('news/<int:pk>/',view=views.NewsDetailView.as_view(),name='news-detail'),
    path('user/logout/',view=views.user_logout,name='user-logout'),
    path('login/page/',view=views.login_page,name='login-page'),
    path('user/login/',view=views.user_login,name='user-login'),
    path('match/<int:pk>/add/comment/',view=views.add_new_comment,name='add-new-comment'),
    path('fav/change/<int:pk>/',view=views.change_fav_status,name='fav-status'),
    path('config/',view=views.configure_page,name='config'),
    path('add/team/',view=views.add_new_team,name='add-team'),
    path('search/',view=views.search,name='search'),
    path('api/team/all',view=views.TeamListAPIView.as_view(),name='api-team-list'),
]


#http://127.0.0.1:8001/hltv/api/team/all