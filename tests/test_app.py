# Tests for your routes go here

''' When I post an album to albums on albums route
The album is added to the database
'''

#POST /albums
#    title: The Score
#    release_year: 2005
#    artist_id = 5
#  Expected response (200 OK):
"""
Album has been added to database
"""

def test_post_albums(db_connection, web_client):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.post('/albums', data={'title': "The Score", 'release_year': 2005, 'artist_id': 5})
    assert response.status_code == 200
    assert response.data.decode('utf=8') == ''

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf=8') == 'Album(1, Doolittle, 1989, 1),Album(2, The Score, 2005, 5)'



'''
When I call GET /albums
I get a list of albums back
'''


def test_get_albums(db_connection, web_client):
    db_connection.seed('seeds/music_app.sql')
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf=8') == 'Album(1, Doolittle, 1989, 1)'




# POST /albums
#  Expected response (400 Bad Request):
"""
Supply album details
"""
def test_post_albums_with_no_data(db_connection, web_client):
    db_connection.seed('seeds/music_app.sql')
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf=8') == 'No album details supplied'

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf=8') == 'Album(1, Doolittle, 1989, 1)'


