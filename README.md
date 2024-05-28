# SoundCloud Search API - Flask Server

This Flask server provides endpoints to search for tracks on SoundCloud using the SoundCloud Search API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/prakhardoneria/SoundCloud-Search.git
    ```

2. Navigate into the project directory:

    ```bash
    cd SoundCloud-Search
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Set the SoundCloud client ID as an environment variable:

    ```bash
    export SOUNDCLOUD_CLIENT_ID=your_soundcloud_client_id
    ```

2. Run the Flask app:

    ```bash
    python main.py
    ```

3. Make GET requests to the endpoints with the `q` parameter to search for tracks on SoundCloud.

#### `/search` Endpoint

Make a GET request to the `/search` endpoint to search for tracks:

Example:

```bash
curl http://localhost:5000/search?q=khamo
```

Sample Response:

```json
{
    "collection": [
        {
            "output": "khamoshiyan arjit singh",
            "query": "khamoshiyan arjit singh"
        },
        ...
    ],
    ...
}
```

#### `/searchOne` Endpoint

Make a GET request to the `/searchOne` endpoint to get the first suggestion:

Example:

```bash
curl http://localhost:5000/searchOne?q=khamo
```

Sample Response:

```json
{
    "suggestion": "khamoshiyan arjit singh"
}
```

If no suggestions are found:

```json
{
    "suggestion": null
}
```

### Environment Variables

- `SOUNDCLOUD_CLIENT_ID`: Your SoundCloud API client ID.

### Endpoints

1. **/search**: Returns a list of search suggestions for the given query.

    - **URL**: `/search`
    - **Method**: `GET`
    - **Query Parameter**: `q` (The search query)

2. **/searchOne**: Returns the first search suggestion for the given query.

    - **URL**: `/searchOne`
    - **Method**: `GET`
    - **Query Parameter**: `q` (The search query)

### Sample Usage

#### `/search` Endpoint

```bash
curl http://localhost:5000/search?q=khamo
```

#### `/searchOne` Endpoint

```bash
curl http://localhost:5000/searchOne?q=khamo
```