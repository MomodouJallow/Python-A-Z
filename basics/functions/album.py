def make_album(artist_name, album_title):
    """Return a dictionary describing a music album."""
    album = {'name':artist_name, 'title': album_title}
    return album


artist = make_album('bob marley', 'one love')
for name, title in artist.items():
    print(artist['name'], artist['title'])