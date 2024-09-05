class Song:
    
    count = 0
    genres = []
    genre_count = {}
    artist_count = {}
    artists = []
  
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artist_count(self.artist)
        Song.add_to_genres(self.genre)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)  # Use the method argument 'genre'
        
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)  # Use the method argument 'artist'
        
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage
song1 = Song("song1", "Artist1", "Rap")
song2 = Song("song2", "Artist2", "Pop")
song3 = Song("song3", "Artist1", "Rock")
song4 = Song("song4", "Artist3", "Pop")
song5 = Song("song5", "Artist1", "Rap")

print(Song.genre_count) 
print(Song.artist_count)     #888999888