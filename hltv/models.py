from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone



class Team(models.Model):
    name = models.CharField(max_length=128)
    points = models.IntegerField()
    rank = models.IntegerField()
    country= models.CharField(max_length=128)
    coach = models.CharField(max_length=128)
    trophies = models.FileField(upload_to='hltv_histories/',null=True, blank=True)
    logo=models.ImageField(upload_to='hltv_teams/',null=True, blank=True)
    inst= models.CharField(max_length=100,null=True,blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    slug=models.SlugField(null=True, blank=True)
    fans= models.ManyToManyField(User, related_name='favs')
    #player

    def __str__(self):
        return f'{self.name}'

    def url_detail(self):
        return reverse('hltv:team-detail', kwargs={'pk': self.id})







class Player(models.Model):
    first= models.CharField(max_length=128)
    last= models.CharField(max_length=128)
    age= models.IntegerField()
    country= models.CharField(max_length=128)
    rating= models.FloatField(max_length=10)
    logo = models.ImageField(upload_to='hltv_teams/', null=True, blank=True)
    nickname = models.CharField(max_length=64)
    maps_played = models.IntegerField(default=50)
    inst = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)
    twitch = models.CharField(max_length=100, null=True, blank=True)
    current_team=models.ForeignKey(Team,related_name="player",on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    major_ach = models.FileField(upload_to='player_ach/',null=True, blank=True)


    def __str__(self):
        return f'{self.first} "{self.nickname}" {self.last}'

    def url_detail(self):
        return reverse('hltv:player-detail', kwargs={'pk': self.id})



class News(models.Model):
    title = models.CharField(max_length=128)
    content=models.FileField(upload_to='hltv_content/',null=True, blank=True)
    comm_with_players = models.ForeignKey(Player, related_name='news',on_delete=models.SET_NULL
                                          , null=True, blank=True)
    comm_with_team = models.ForeignKey(Team, related_name='news', on_delete=models.SET_NULL
                                          , null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def url_detail(self):
        return reverse('hltv:news-detail', kwargs={'pk': self.id})



class Event(models.Model):
    name = models.CharField(max_length=128)
    prize_pool= models.IntegerField(default=150_000)
    country = models.CharField(max_length=128)
    logo = models.ImageField(upload_to='hltv_teams/', null=True, blank=True)
    def __str__(self):
        return self.name

    def url_detail(self):
        return reverse('hltv:event-detail', kwargs={'pk': self.id})


class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='match1', on_delete=models.SET_NULL,null=True, blank=True)
    team2 = models.ForeignKey(Team, related_name='match2', on_delete=models.SET_NULL,null=True, blank=True)
    stage=models.CharField(max_length=128)
    tournament=models.ForeignKey(Event, related_name='match', on_delete=models.SET_NULL
                                 , null=True, blank=True)
    coef1=models.FloatField(default=1.8)
    coef2=models.FloatField(default=1.8)

    def __str__(self):
        return f'{self.team1} vs {self.team2}'

    def url_detail(self):
        return reverse('hltv:match-detail',kwargs={'pk':self.id})





class Podcast(models.Model):
    number = models.IntegerField()
    name=models.CharField(max_length=256)
    link=models.CharField(max_length=11)


    def __str__(self):
        return f'{self.name}'

    def url_detail(self):
        pass


class UserAddon(models.Model):
    ava = models.ImageField(upload_to='user_avatars/', null=True, blank=True)
    user = models.OneToOneField(User,related_name='addon', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}\'s addon'



class MatchComment(models.Model):
    text=models.CharField(max_length=512)
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    match=models.ForeignKey(Match,on_delete=models.CASCADE,related_name='comments')
    published=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

    class Meta:
        ordering=['-published']











