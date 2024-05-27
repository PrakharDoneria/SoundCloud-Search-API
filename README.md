# SoundCloud Search API - Flask Server

This Flask server provides an endpoint to search for tracks on SoundCloud using the SoundCloud Search API.

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

3. Make GET requests to the `/search` endpoint with the `q` parameter to search for tracks on SoundCloud:

    Example:

    ```bash
    curl http://localhost:5000/search?q=khamoshiya
    ```

### Environment Variables

- `SOUNDCLOUD_CLIENT_ID`: Your SoundCloud API client ID.

