from django.db import models
from django.contrib.auth.models import User


class Discourse(models.Model):
    poster = models.OneToOneField(to=User, on_delete=models.CASCADE)
    liker = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Discourse):
    title = models.CharField(max_length=300)
    ARTIST = "artist"
    ALBUM = "album"
    TRACK = "track"
    SPOT_TYPE_CHOICES = [
        (ARTIST, "Artist"),
        (ALBUM, "Album"),
        (TRACK, "Track")
    ]
    spot_type = models.CharField(max_length=6, choices=SPOT_TYPE_CHOICES)
    artist = models.ForeignKey(
        to="spots.Artist", on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(
        to="spots.Album", on_delete=models.CASCADE, null=True)
    track = models.ForeignKey(
        to="spots.Track", on_delete=models.CASCADE, null=True)

    def is_under_artist_spot(self):
        """Returns true if the post is under an artist spot."""
        return self.spot_type == ARTIST and not artist

    def is_under_album_spot(self):
        """Returns true if the post is under an album spot."""
        return self.spot_type == ALBUM and not album

    def is_under_track_spot(self):
        """Returns true if the post is under a track spot."""
        return self.spot_type == TRACK and not track


class Comment(Discourse):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(to="self", on_delete=models.RESTRICT)

    def is_removed(self):
        """Returns true if the comment is removed."""
        return self.content == "[removed]"
