from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    data = request.json
    text_prompt = data.get('text')
    if not text_prompt:
        return jsonify({"error": "No text provided"}), 400

    # Placeholder response simulating AI video generation
    return jsonify({
        "message": "Video generated successfully",
        "video_url": "https://example.com/generated-video.mp4"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
