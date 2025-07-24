# 🎵 Face-Based Music Recommendation System

Detect your mood from your face and get Indian song recommendations instantly!

## Features
- Detects user's mood from webcam using DeepFace
- Recommends Indian songs (Hindi, Telugu, Tamil, English) based on emotion
- Clean, responsive UI with Bootstrap
- Lottie animations for mood feedback
- Embedded YouTube players for one-click play
- Language selection for playlists

## How It Works
1. Open the web page and allow webcam access
2. Click "Detect Mood" to capture your face
3. The backend analyzes your emotion
4. Get a playlist of songs matching your mood and language

## Project Structure
```
face based model/
│
├── index.html
├── style.css
├── script.js
├── app.py
├── indian_playlist.json
├── requirements.txt
├── README.md
└── animations/
    ├── happy.json
    ├── sad.json
    ├── angry.json
    ├── neutral.json
    └── surprise.json
```

## Setup Instructions

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Lottie Animations
- Place mood Lottie files (happy.json, sad.json, angry.json, neutral.json, surprise.json) in the `animations/` folder directly inside your main project directory (`face based model/animations/`).
- You can get free Lottie files from [lottiefiles.com](https://lottiefiles.com/).
- **Update your `script.js` paths as follows:**
  ```js
  const lottieFiles = {
    happy: 'animations/happy.json',
    sad: 'animations/sad.json',
    angry: 'animations/angry.json',
    neutral: 'animations/neutral.json',
    surprise: 'animations/surprise.json',
  };
  ```

### 3. Run the Backend
```bash
python app.py
```

### 4. Open the Frontend
- Open `index.html` in your browser (for local Flask, use a simple server or set up CORS).
- Or, deploy both backend and frontend to a service like Render or Hugging Face Spaces.

## Deployment
- For public deployment, serve both backend and frontend from the same domain or configure CORS.
- You can use [Render](https://render.com/) or [Hugging Face Spaces](https://huggingface.co/spaces) for free hosting.

## Customizing Playlists
- Edit `indian_playlist.json` to add your favorite songs for each mood and language.

## Credits
- Face emotion detection: [DeepFace](https://github.com/serengil/deepface)
- UI: Bootstrap, Lottie
- Indian song curation: You!

---
Enjoy your personalized music experience! ✨ 