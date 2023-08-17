
from lib.album_repository import AlbumRepository
from lib.album import Album

'''
When I call #all
I get all the albums in a table
'''

def test_all(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = AlbumRepository(db_connection)
    repository.all() == [
    Album(1,'Doolittle', 1989, 1)
    ]


'''
When I call #create
I create an album in the database
And I can see it back in #all
'''   

def test_create(db_connection):
    db_connection.seed('seeds/music_app.sql')
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test Title', 500, 2)
    repository.create(album)
    assert repository.all() == [
        Album(1,'Doolittle', 1989, 1),Album(2, 'Test Title', 500, 2)
    ]