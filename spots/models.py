from django.db import models
from django.contrib.auth.models import User


class Spot(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    spotify_id = models.CharField(max_length=22)
    picture_url = models.URLField(blank=True)
    follower = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Artist(Spot):
    genres = models.JSONField()


class Album(Spot):
    ALBUM = "album"
    SINGLE = "single"
    COMPILATION = "compilation"
    ALBUM_TYPE_CHOICES = [
        (ALBUM, "Album"),
        (SINGLE, "Single"),
        (COMPILATION, "Compilation")
    ]
    album_type = models.CharField(max_length=11, choices=ALBUM_TYPE_CHOICES)
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE)
    genres = models.JSONField()
    release_date = models.DateField(blank=True)

    def is_album(self):
        """Returns true if the album is a album."""
        return self.album_type == ALBUM

    def is_single(self):
        """Returns true if the album is a single."""
        return self.album_type == SINGLE

    def is_compilation(self):
        """Returns true if the album is a compilation."""
        return self.album_type == COMPILATION


class Track(Spot):
    explicit = models.BooleanField(default=False)
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(to=Album, on_delete=models.RESTRICT)
    disc_number = models.PositiveSmallIntegerField(default=1)
    track_number = models.PositiveSmallIntegerField()
    duration_ms = models.PositiveIntegerField(
        verbose_name='duration in milliseconds')
