from lib.album import Album


'''
construct an album instance with id, title, release_date and artist
'''

def test_album():
    album = Album(1, "A title", 2000, 2)
    assert album.id == 1
    assert album.title == "A title"
    assert album.release_year == 2000
    assert album.artist_id == 2

'''
albums with identical content are seen as equal
'''

def test_equality():
    album1 = Album(1, "A title", 2000, 2)
    album2 = Album(1, "A title", 2000, 2)
    assert album1 == album2

'''
returns a formatted string
'''
def test_string():
    album = Album(1, "A title", 2000, 2)
    assert str(album) == 'Album(1, A title, 2000, 2)'