from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

client_id = os.environ.get('SOUNDCLOUD_CLIENT_ID')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    url = f"https://api-v2.soundcloud.com/search/queries?q={query}&client_id={client_id}&limit=10&offset=0&linked_partitioning=1&app_version=1716534432&app_locale=en"

    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500

@app.route('/searchOne', methods=['GET'])
def search_one():
    query = request.args.get('q')
    url = f"https://api-v2.soundcloud.com/search/queries?q={query}&client_id={client_id}&limit=10&offset=0&linked_partitioning=1&app_version=1716534432&app_locale=en"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        suggestions = data.get('collection', [])
        if suggestions:
            first_suggestion = suggestions[0].get('query', '')
            return jsonify({"suggestion": first_suggestion})
        else:
            return jsonify({"suggestion": None}), 404
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500
        

if __name__ == '__main__':
    app.run(debug=True)
