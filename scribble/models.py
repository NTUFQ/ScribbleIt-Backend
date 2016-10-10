from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Template(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True)
    created_by = models.DateTimeField(auto_now=True)
    difficulty = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.pk) + "|" + self.name


class Room(models.Model):
    started = models.BooleanField(default=False)
    created_by = models.DateTimeField(auto_now=True)
    started_by = models.DateTimeField(blank=True)
    template = models.ForeignKey(Template, default=None)

    def __str__(self):
        return str(self.pk)


class Player(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    fbid = models.CharField(max_length=16, primary_key=True)
    email = models.EmailField(max_length=30, blank=True)
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name="players")

    def __str__(self):
        return self.fbid + "|" + self.name


class Artwork(models.Model):
    name = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to="pic/", default="pic/not_found.jpg")
    created_by = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="artwork_list")
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, default=None, null=True)
    public = models.BooleanField(default=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, default=None, null=True, blank=True, related_name="artworks")

    def __str__(self):
        return str(self.pk) + "|" + self.name + "|" + self.owner.__str__()


class Comment(models.Model):
    text = models.TextField(max_length=200)
    created_by = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.pk) + "|" + self.text + "|" + self.owner.__str__() + "|" + self.artwork.__str__()


class Like(models.Model):
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name="likes")
    created_by = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + "|" + self.owner.__str__() + "|" + self.artwork.__str__()
