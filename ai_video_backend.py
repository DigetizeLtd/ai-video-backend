from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/generate_video', methods=['POST'])
def generate_video():
    data = request.json
    text_prompt = data.get('text')
    if not text_prompt:
        return jsonify({"error": "No text provided"}), 400
    
    # Example: Send text to an AI video generation API (Replace with actual API call)
    ai_response = requests.post(
        "https://api.runwayml.com/v1/generate-video",  # Example API (Replace with actual service)
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        json={"prompt": text_prompt}
    )
    
    if ai_response.status_code == 200:
        video_url = ai_response.json().get("video_url")
        return jsonify({"message": "Video generated successfully", "video_url": video_url})
    else:
        return jsonify({"error": "Failed to generate video"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
