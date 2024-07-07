## API Documentation

This documentation outlines the available API endpoints for managing users, artists, albums, songs, stores, posts, reports, tickets, messages, UGC, profile linking, and lyrics distribution. All endpoints require JWT authentication unless stated otherwise.

**Base URL:** `/api`

# User API

#### 1\. Get all Users

*   **Endpoint:** `/users`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific User

*   **Endpoint:** `/users/<user_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `user_id`: (integer) The ID of the user to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** User not found

#### 3\. Create a new User (No JWT required for this endpoint)

*   **Endpoint:** `/users`
*   **Method:** `POST`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing User

*   **Endpoint:** `/users/<user_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `user_id`: (integer) The ID of the user to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** User not found

#### 5\. Delete a User

*   **Endpoint:** `/users/<user_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `user_id`: (integer) The ID of the user to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** User not found

# Artist API

#### 1\. Get all Artists

*   **Endpoint:** `/artists`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Artist

*   **Endpoint:** `/artists/<artist_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `artist_id`: (integer) The ID of the artist to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Artist not found

#### 3\. Create a new Artist

*   **Endpoint:** `/artists`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Artist

*   **Endpoint:** `/artists/<artist_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `artist_id`: (integer) The ID of the artist to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Artist not found

#### 5\. Delete an Artist

*   **Endpoint:** `/artists/<artist_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `artist_id`: (integer) The ID of the artist to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Artist not found

# Album API

#### 1\. Get all Albums

*   **Endpoint:** `/albums`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Album

*   **Endpoint:** `/albums/<album_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `album_id`: (integer) The ID of the album to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Album not found

#### 3\. Create a new Album

*   **Endpoint:** `/albums`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Album

*   **Endpoint:** `/albums/<album_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `album_id`: (integer) The ID of the album to update.
    *   **Body:** (JSON) Similar to Create Album, include only the fields to update.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Album not found

#### 5\. Delete an Album

*   **Endpoint:** `/albums/<album_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `album_id`: (integer) The ID of the album to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Album not found

# Song API

#### 1\. Get all Songs

*   **Endpoint:** `/songs`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Song

*   **Endpoint:** `/songs/<song_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `song_id`: (integer) The ID of the song to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Song not found

#### 3\. Create a new Song

*   **Endpoint:** `/songs`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Song

*   **Endpoint:** `/songs/<song_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `song_id`: (integer) The ID of the song to update.
    *   **Body:** (JSON) Similar to Create Song, include only fields to update.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Song not found

#### 5\. Delete a Song

*   **Endpoint:** `/songs/<song_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `song_id`: (integer) The ID of the song to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Song not found

# Store API

#### 1\. Get all Stores

*   **Endpoint:** `/stores`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Store

*   **Endpoint:** `/stores/<store_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `store_id`: (integer) The ID of the store to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Store not found

#### 3\. Create a new Store

*   **Endpoint:** `/stores`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Store

*   **Endpoint:** `/stores/<store_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `store_id`: (integer) The ID of the store to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Store not found

#### 5\. Delete a Store

*   **Endpoint:** `/stores/<store_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `store_id`: (integer) The ID of the store to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Store not found

# Post API

#### 1\. Get all Posts

*   **Endpoint:** `/posts`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Post

*   **Endpoint:** `/posts/<post_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `post_id`: (integer) The ID of the post to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Post not found

#### 3\. Create a new Post

*   **Endpoint:** `/posts`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Post

*   **Endpoint:** `/posts/<post_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `post_id`: (integer) The ID of the post to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Post not found

#### 5\. Delete a Post

*   **Endpoint:** `/posts/<post_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `post_id`: (integer) The ID of the post to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Post not found

# Report API

#### 1\. Get all Reports

*   **Endpoint:** `/reports`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Report

*   **Endpoint:** `/reports/<report_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `report_id`: (integer) The ID of the report to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Report not found

#### 3\. Create a new Report

*   **Endpoint:** `/reports`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Report

*   **Endpoint:** `/reports/<report_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `report_id`: (integer) The ID of the report to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Report not found

#### 5\. Delete a Report

*   **Endpoint:** `/reports/<report_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `report_id`: (integer) The ID of the report to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Report not found

# Ticket API

#### 1\. Get all Tickets

*   **Endpoint:** `/tickets`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Ticket

*   **Endpoint:** `/tickets/<ticket_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ticket_id`: (integer) The ID of the ticket to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Ticket not found

#### 3\. Create a new Ticket

*   **Endpoint:** `/tickets`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Ticket

*   **Endpoint:** `/tickets/<ticket_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ticket_id`: (integer) The ID of the ticket to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Ticket not found

#### 5\. Delete a Ticket

*   **Endpoint:** `/tickets/<ticket_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ticket_id`: (integer) The ID of the ticket to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Ticket not found

# Message API

#### 1\. Get all Messages

*   **Endpoint:** `/messages`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Message

*   **Endpoint:** `/messages/<message_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `message_id`: (integer) The ID of the message to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Message not found

#### 3\. Create a new Message

*   **Endpoint:** `/messages`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Message

*   **Endpoint:** `/messages/<message_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `message_id`: (integer) The ID of the message to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Message not found

#### 5\. Delete a Message

*   **Endpoint:** `/messages/<message_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `message_id`: (integer) The ID of the message to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Message not found

# UGC API

#### 1\. Get all UGCs

*   **Endpoint:** `/ugcs`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific UGC

*   **Endpoint:** `/ugcs/<ugc_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ugc_id`: (integer) The ID of the UGC to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** UGC not found

#### 3\. Create a new UGC

*   **Endpoint:** `/ugcs`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing UGC

*   **Endpoint:** `/ugcs/<ugc_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ugc_id`: (integer) The ID of the UGC to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** UGC not found

#### 5\. Delete a UGC

*   **Endpoint:** `/ugcs/<ugc_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `ugc_id`: (integer) The ID of the UGC to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** UGC not found

# Profile Linking API

#### 1\. Get all Profile Links

*   **Endpoint:** `/profilelinkings`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Profile Link

*   **Endpoint:** `/profilelinkings/<profilelinking_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `profilelinking_id`: (integer) The ID of the Profile Link to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Profile Link not found

#### 3\. Create a new Profile Link

*   **Endpoint:** `/profilelinkings`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Profile Link

*   **Endpoint:** `/profilelinkings/<profilelinking_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `profilelinking_id`: (integer) The ID of the Profile Link to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Profile Link not found

#### 5\. Delete a Profile Link

*   **Endpoint:** `/profilelinkings/<profilelinking_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `profilelinking_id`: (integer) The ID of the Profile Link to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Profile Link not found

# Distribute Lyrics API

#### 1\. Get all Lyrics Distributions

*   **Endpoint:** `/distributelyrics`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:** None
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**

#### 2\. Get a specific Lyrics Distribution

*   **Endpoint:** `/distributelyrics/<distributelyric_id>`
*   **Method:** `GET`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `distributelyric_id`: (integer) The ID of the Lyrics Distribution to retrieve.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Lyrics Distribution not found

#### 3\. Create a new Lyrics Distribution

*   **Endpoint:** `/distributelyrics`
*   **Method:** `POST`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 201 Created
    *   **Body:**

#### 4\. Update an existing Lyrics Distribution

*   **Endpoint:** `/distributelyrics/<distributelyric_id>`
*   **Method:** `PUT`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `distributelyric_id`: (integer) The ID of the Lyrics Distribution to update.
    *   **Body:** (JSON)
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Lyrics Distribution not found

#### 5\. Delete a Lyrics Distribution

*   **Endpoint:** `/distributelyrics/<distributelyric_id>`
*   **Method:** `DELETE`
*   **Headers:**
    *   `Authorization`: `Bearer <JWT_TOKEN>`
*   **Parameters:**
    *   `distributelyric_id`: (integer) The ID of the Lyrics Distribution to delete.
*   **Response:**
    *   **Status Code:** 200 OK
    *   **Body:**
    *   **Status Code:** 404 Not Found
    *   **Body:** Lyrics Distribution not found

```
{
"message": "Distributelyric deleted successfully!"
}
```

```
{
"id": 1,
"message": "Distributelyric updated successfully!" 
}
```

```
{
"lyrics": "Updated lyrics content..." 
}
```

```
{
"id": 3,
"message": "Distributelyric created successfully!" 
}
```

```
{
"user_id": 1,
"release_title": "New Lyrics Distribution Release Title", 
"audio_title": "New Lyrics Distribution Audio Title",
"language": "English",
"lyrics": "Lyrics content..." 
}
```

```
{
"id": 1,
"user_id": 1,
"release_title": "Lyrics Distribution Release Title One" 
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "release_title": "Lyrics Distribution Release Title One"
},
{
    "id": 2,
    "user_id": 2,
    "release_title": "Lyrics Distribution Release Title Two" 
}
]
```

```
{
"message": "Profilelinking deleted successfully!"
}
```

```
{
"id": 1,
"message": "Profilelinking updated successfully!"
}
```

```
{
"fb": "https://facebook.com/updated-artist-profile",
"ig": "https://instagram.com/updated-artist-profile" 
}
```

```
{
"id": 3,
"message": "Profilelinking created successfully!" 
}
```

```
{
"user_id": 1,
"release_title": "New Profile Link Release Title",
"audio_title": "New Profile Link Audio Title",
"artist": "Artist Name",
"fb": "https://facebook.com/artist-profile",
"ig": "https://instagram.com/artist-profile" 
}
```

```
{
"id": 1,
"user_id": 1,
"release_title": "Profile Link Release Title One" 
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "release_title": "Profile Link Release Title One"
},
{
    "id": 2,
    "user_id": 2,
    "release_title": "Profile Link Release Title Two"
}
]
```

```
{
"message": "Ugc deleted successfully!"
}
```

```
{
"id": 1,
"message": "Ugc updated successfully!"
}
```

```
{
"release_title": "Updated UGC Release Title",
"audio_title": "Updated UGC Audio Title", 
"url": "https://example.com/updated-ugc-content"
}
```

```
{
"id": 3,
"message": "Ugc created successfully!"
}
```

```
{
"user_id": 1,
"release_title": "New UGC Release Title",
"audio_title": "New UGC Audio Title",
"policy": "UGC Policy Agreement", 
"url": "https://example.com/ugc-content"
}
```

```
{
"id": 1,
"user_id": 1,
"release_title": "UGC Release Title One"
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "release_title": "UGC Release Title One"
},
{
    "id": 2,
    "user_id": 2,
    "release_title": "UGC Release Title Two"
}
]
```

```
{
"message": "Message deleted successfully!"
}
```

```
{
"id": 1,
"message": "Message updated successfully!"
}
```

```
{
"message": "Updated message content..." 
}
```

```
{
"id": 3,
"message": "Message created successfully!"
}
```

```
{
"author_id": 1,
"ticket_id": 1,
"message": "New message content...",
"attachment": "https://example.com/attachment.pdf" 
}
```

```
{
"id": 1,
"author_id": 1,
"ticket_id": 1,
"message": "Message content one..."
}
```

```
[
{
    "id": 1,
    "author_id": 1,
    "ticket_id": 1,
    "message": "Message content one..."
},
{
    "id": 2,
    "author_id": 2,
    "ticket_id": 2,
    "message": "Message content two..."
}
]
```

```
{
"message": "Ticket deleted successfully!"
}
```

```
{
"id": 1,
"message": "Ticket updated successfully!"
}
```

```
{
"reason": "Updated Ticket Reason" 
}
```

```
{
"id": 3,
"message": "Ticket created successfully!"
}
```

```
{
"user_id": 1,
"reason": "New Ticket Reason"
}
```

```
{
"id": 1,
"user_id": 1,
"reason": "Technical Issue"
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "reason": "Technical Issue"
},
{
    "id": 2,
    "user_id": 2,
    "reason": "Account Question"
}
]
```

```
{
"message": "Report deleted successfully!"
}
```

```
{
"id": 1,
"message": "Report updated successfully!"
}
```

```
{
"report_for": "Updated Report Type",
"start_date": "2023-12-05",
"end_date": "2023-12-31"
}
```

```
{
"id": 3,
"message": "Report created successfully!"
}
```

```
{
"user_id": 1,
"report_for": "New Report Type",
"start_date": "2023-12-01",
"end_date": "2023-12-28"
}
```

```
{
"id": 1,
"user_id": 1,
"report_for": "Sales Report"
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "report_for": "Sales Report"
},
{
    "id": 2,
    "user_id": 2,
    "report_for": "Engagement Report"
}
]
```

```
{
"message": "Post deleted successfully!"
}
```

```
{
"id": 1,
"message": "Post updated successfully!"
}
```

```
{
"title": "Updated Post Title",
"content": "Updated post content..."
}
```

```
{
"id": 3,
"message": "Post created successfully!"
}
```

```
{
"title": "New Post Title",
"content": "New post content..."
}
```

```
{
"id": 1,
"title": "Post Title One",
"content": "Post content one..."
}
```

```
[
{
    "id": 1,
    "title": "Post Title One",
    "content": "Post content one..."
},
{
    "id": 2,
    "title": "Post Title Two",
    "content": "Post content two..."
}
]
```

```
{
"message": "Store deleted successfully!"
}
```

```
{
"id": 1,
"message": "Store updated successfully!"
}
```

```
{
"store_name": "Updated Store Name"
}
```

```
{
"id": 3,
"message": "Store created successfully!"
}
```

```
{
"song_id": 1,
"store_name": "New Store"
}
```

```
{
"id": 1,
"song_id": 1,
"store_name": "Store One"
}
```

```
[
{
    "id": 1,
    "song_id": 1,
    "store_name": "Store One"
},
{
    "id": 2,
    "song_id": 2,
    "store_name": "Store Two"
}
]
```

```
{
"message": "Song deleted successfully!"
}
```

```
{
"id": 1,
"message": "Song updated successfully!"
}
```

```
{
"id": 3,
"message": "Song created successfully!"
}
```

```
{
"album_id": 1,
"track": "01",
"version": "Original", 
"instrumental": "No",
"title": "New Song",
"subtitle": "Subtitle", 
"primary_artist1": "Artist One",
"primary_artist2": "Artist Two", 
"primary_artist3": "Artist Three", 
"featuring_artist1": "Featuring Artist One",
"featuring_artist2": "Featuring Artist Two", 
"featuring_artist3": "Featuring Artist Three", 
"author": "Author Name",
"composer": "Composer Name",
"producer": "Producer Name",
"p_line": "P Line",
"production_year": "2023",
"publisher": "Publisher Name",
"isrc": "123456789012", 
"genre": "Genre",
"subgenre": "Subgenre",
"explicit": false, 
"title_language": "English",
"lyrics_language": "English",
"lyrics": "Lyrics...",
"caller_tune": "Caller Tune URL" 
}
```

```
{
"id": 1,
"album_id": 1,
"title": "Song Title One"
}
```

```
[
{
    "id": 1,
    "album_id": 1,
    "title": "Song Title One"
},
{
    "id": 2,
    "album_id": 2,
    "title": "Song Title Two"
}
]
```

```
{
"message": "Album deleted successfully!"
}
```

```
{
"id": 1,
"message": "Album updated successfully!"
}
```

```
{
"id": 3,
"message": "Album created successfully!"
}
```

```
{
"user_id": 1,
"artwork": "https://example.com/artwork.jpg",
"title": "New Album",
"type": "Album",
"primary_artist1": "Artist One",
"primary_artist2": "Artist Two", 
"primary_artist3": "Artist Three", 
"featuring_artist1": "Featuring Artist One", 
"featuring_artist2": "Featuring Artist Two", 
"featuring_artist3": "Featuring Artist Three", 
"genre": "Genre",
"sub_genre": "Subgenre",
"label_name": "Label Name",
"release_date": "2023-12-28",
"p_line": "P Line",
"c_line": "C Line",
"upc_ean": "123456789012" 
}
```

```
{
"id": 1,
"user_id": 1,
"title": "Album Title One"
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "title": "Album Title One"
},
{
    "id": 2,
    "user_id": 2,
    "title": "Album Title Two"
}
]
```

```
{
"message": "Artist deleted successfully!"
}
```

```
{
"id": 1,
"message": "Artist updated successfully!"
}
```

```
{
"name": "Updated Artist Name"
}
```

```
{
"id": 3,
"message": "Artist created successfully!"
}
```

```
{
"user_id": 1,
"name": "New Artist"
}
```

```
{
"id": 1,
"user_id": 1,
"name": "Artist One"
}
```

```
[
{
    "id": 1,
    "user_id": 1,
    "name": "Artist One"
},
{
    "id": 2,
    "user_id": 2,
    "name": "Artist Two"
}
]
```

```
{
"message": "User deleted successfully!"
}
```

```
{
"id": 1,
"message": "User updated successfully!"
}
```

```
{
"name": "John Doe Jr.", 
"email": "john.doe.jr@example.com" 
}
```

```
{
"id": 3,
"message": "User created successfully!"
}
```

```
{
"name": "John Doe",
"email": "john.doe@example.com",
"password": "password123" 
}
```

```
{
"id": 1,
"name": "John Doe",
"email": "john.doe@example.com"
}
```

```
[
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
},
{
    "id": 2,
    "name": "Jane Doe",
    "email": "jane.doe@example.com"
}
]
```