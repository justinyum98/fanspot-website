from django.db import models
from django.contrib.auth.models import User


class Spot(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    spotify_id = models.CharField(max_length=22, blank=True)
    picture_url = models.URLField(blank=True)
    likers = models.ManyToManyField(to=User, blank=True)
    followers = models.ManyToManyField(to=User, blank=True, related_name='+')

    class Meta:
        abstract = True


class Artist(Spot):
    genres = models.JSONField(default=list)

    def __str__(self):
        return self.name


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
    artists = models.ManyToManyField(to=Artist)
    genres = models.JSONField(default=list)
    release_date = models.DateField(blank=True)

    def __str__(self):
        return self.name

    def is_album(self) -> bool:
        """Returns true if the album is a album."""
        return self.album_type == ALBUM

    def is_single(self) -> bool:
        """Returns true if the album is a single."""
        return self.album_type == SINGLE

    def is_compilation(self) -> bool:
        """Returns true if the album is a compilation."""
        return self.album_type == COMPILATION


class Track(Spot):
    explicit = models.BooleanField(default=False)
    artists = models.ManyToManyField(to=Artist)
    album = models.ForeignKey(to=Album, on_delete=models.RESTRICT)
    disc_number = models.PositiveSmallIntegerField(default=1)
    track_number = models.PositiveSmallIntegerField()
    duration_ms = models.PositiveIntegerField(
        verbose_name='duration in milliseconds'
    )

    def __str__(self):
        return self.name
