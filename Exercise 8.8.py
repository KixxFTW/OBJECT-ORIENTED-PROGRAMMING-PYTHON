def make_album(artist_name, album_title, num_tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if num_tracks:
        album['tracks'] = num_tracks
    return album

# Create three music album dictionaries
album1 = make_album('Bruno mars', '24k Magic',9)
album2 = make_album('Taylor swift', 'Speak now', 22)
album3 = make_album('Drake', 'For all the dogs',23 )

# Print the album dictionaries
print(album1)
print(album2)
print(album3)

# Allow users to enter album information using a while loop
while True:
    artist = input("Enter the artist name (or 'q' to quit): ")
    if artist == 'q':
        break
    title = input("Enter the album title: ")
    tracks = input("Enter the number of tracks: ")
    user_album = make_album(artist, title, tracks)
    print(user_album)
