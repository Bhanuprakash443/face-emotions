from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
from deepface import DeepFace
import json

app = Flask(__name__)
CORS(app)

# Load playlists
with open('indian_playlist.json', 'r', encoding='utf-8') as f:
    playlists = json.load(f)

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    image_data = data.get('image')
    language = data.get('language', 'hindi')
    if not image_data:
        return jsonify({'error': 'No image provided'}), 400
    # Decode base64 image
    try:
        header, encoded = image_data.split(',', 1)
        img_bytes = base64.b64decode(encoded)
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    except Exception as e:
        return jsonify({'error': 'Invalid image data'}), 400
    # Detect emotion
    try:
        result = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        mood = result['dominant_emotion'].lower()
        # Map to our moods
        mood_map = {
            'happy': 'happy',
            'sad': 'sad',
            'angry': 'angry',
            'neutral': 'neutral',
            'surprise': 'surprise',
            'fear': 'neutral',
            'disgust': 'angry'
        }
        mood = mood_map.get(mood, 'neutral')
    except Exception as e:
        return jsonify({'error': 'Could not detect mood'}), 500
    # Get songs
    songs = playlists.get(language, {}).get(mood, [])
    return jsonify({'mood': mood, 'songs': songs})

if __name__ == '__main__':
    app.run(debug=True) 