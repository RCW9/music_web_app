# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._


# Submit message route
POST /albums
  title: string
  release_year: number (str)
  artist_id: number (str)
```

## 2. Create Examples as Tests

# POST /albums
#    tile: The Score
#    release_year: 2005
#    artist_id = 5
#  Expected response (200 OK):
"""
Album has been added to database
"""

# GET /albums
#  Expected response (200 OK):
"""
List of album class instances
"""

# POST /albums
#  Expected response (400 Bad Request):
"""
Supply album details
"""


## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```


