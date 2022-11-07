from rest_framework import serializers
from .models import Lyric, Song

class LyricSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ['content']

class SongSerializer(serializers.ModelSerializer):
    #to get lyric content in song
    lyric = serializers.SerializerMethodField('get_lyric')
    artiste_id = serializers.StringRelatedField('read_only=True')

    def get_lyrics(self, instance):
        query = instance.lyric_set.all()
        lyric = LyricSerializers(query, many=True).data

        return lyric

    class Meta:
            model = Song
            fields = ['id', 'artist_id', 'title', 'date_released', 'likes', 'lyric']

class UpdateSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['title', 'date_released', 'artist_id']

    

