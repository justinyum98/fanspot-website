from datetime import date, timedelta
from faker import Faker

from django.contrib.auth.models import User
from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Artist, Album, Track

fake = Faker()


class ArtistModelTests(TestCase):
    def test_create_artist(self):
        """
        Can create an artist.
        """
        name = fake.name()
        description = fake.text()
        spotify_id = "123456789"
        picture_url = fake.image_url()

        artist = Artist(
            name=name,
            description=description,
            spotify_id=spotify_id,
            picture_url=picture_url
        )
        artist.save()

        self.assertIsNotNone(artist)
        self.assertIsInstance(artist, Artist)
        self.assertEquals(artist.name, name)
        self.assertEquals(artist.description, description)
        self.assertEquals(artist.spotify_id, spotify_id)
        self.assertEquals(artist.picture_url, picture_url)
        self.assertIsNotNone(artist.likers)
        self.assertIsNotNone(artist.followers)


class AlbumModelTests(TestCase):
    def test_create_album(self):
        """
        Can create an album.
        """
        name = fake.name()
        description = fake.text()
        spotify_id = "123456789"
        picture_url = fake.image_url()
        album_type = Album.ALBUM
        release_date = date.today()

        album = Album(
            name=name,
            description=description,
            spotify_id=spotify_id,
            picture_url=picture_url,
            album_type=album_type,
            release_date=release_date
        )
        album.save()

        self.assertIsNotNone(album)
        self.assertIsInstance(album, Album)
        self.assertEquals(album.name, name)
        self.assertEquals(album.description, description)
        self.assertEquals(album.spotify_id, spotify_id)
        self.assertEquals(album.picture_url, picture_url)
        self.assertEquals(album.album_type, album_type)
        self.assertEquals(album.release_date, release_date)

    def test_is_album(self):
        """
        Should return true if the album is an album.
        """
        album = Album(name=fake.name(), album_type=Album.ALBUM)
        album.save()

        self.assertTrue(album.is_album())

    def test_is_single(self):
        """
        Should return true if the album is a single.
        """
        album = Album(name=fake.name(), album_type=Album.SINGLE)
        album.save()

        self.assertTrue(album.is_single())

    def test_is_compilation(self):
        """
        Should return true if the album is a compilation.
        """
        album = Album(name=fake.name(), album_type=Album.COMPILATION)
        album.save()

        self.assertTrue(album.is_compilation())
