from faker import Faker

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Artist, Album, Track

fake = Faker()


class ArtistModelTests(TestCase):
    def test_creating_artist(self):
        """
        Can create an artist.
        """
        fake_name = fake.name()
        fake_description = fake.text()
        fake_spotify_id = "123456789"
        fake_picture_url = fake.image_url()

        artist = Artist(
            name=fake_name,
            description=fake_description,
            spotify_id=fake_spotify_id,
            picture_url=fake_picture_url
        )
        artist.save()

        self.assertIsNotNone(artist)
        self.assertIsInstance(artist, Artist)
        self.assertEquals(artist.name, fake_name)
        self.assertEquals(artist.description, fake_description)
        self.assertEquals(artist.spotify_id, fake_spotify_id)
        self.assertEquals(artist.picture_url, fake_picture_url)
        self.assertIsNotNone(artist.likers)
        self.assertIsNotNone(artist.followers)

    def test_user_likes_artist(self):
        """
        Can like an artist.
        """
        user = User(username=fake.first_name(), password=fake.password(8))
        user.save()
        artist = Artist(name=fake.name())
        artist.save()

        artist.likers.add(user)

        self.assertTrue(artist.likers.filter(pk=user.pk).exists())
        self.assertEquals(artist.likers.get(id=user.pk), user)

    def test_user_unlikes_artist(self):
        """
        Can unlike an artist.
        """
        user = User(username=fake.first_name(), password=fake.password(8))
        user.save()
        artist = Artist(name=fake.name())
        artist.save()
        artist.likers.add(user)

        artist.likers.remove(user)

        self.assertFalse(artist.likers.filter(pk=user.pk).exists())

    def test_user_follows_artist(self):
        """
        Can follow an artist.
        """
        user = User(username=fake.first_name(), password=fake.password(8))
        user.save()
        artist = Artist(name=fake.name())
        artist.save()

        artist.followers.add(user)

        self.assertTrue(artist.followers.filter(pk=user.pk).exists())
        self.assertEquals(artist.followers.get(id=user.pk), user)

    def test_user_unfollows_artist(self):
        """
        Can unfollow an artist.
        """
        user = User(username=fake.first_name(), password=fake.password(8))
        user.save()
        artist = Artist(name=fake.name())
        artist.save()
        artist.followers.add(user)

        artist.followers.remove(user)

        self.assertFalse(artist.followers.filter(pk=user.pk).exists())
