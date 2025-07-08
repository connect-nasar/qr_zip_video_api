from flask import Flask, request, send_file
import os
from encoder import zip_to_video
from decoder import video_to_zip

app = Flask(__name__)
TEMP_DIR = 'temp'
os.makedirs(TEMP_DIR, exist_ok=True)

@app.route('/encode', methods=['POST'])
def encode_zip():
    zip_file = request.files['file']
    zip_path = os.path.join(TEMP_DIR, 'input.zip')
    video_path = os.path.join(TEMP_DIR, 'output.avi')

    zip_file.save(zip_path)
    zip_to_video(zip_path, video_path)

    return send_file(video_path, as_attachment=True)

@app.route('/decode', methods=['POST'])
def decode_video():
    video_file = request.files['file']
    video_path = os.path.join(TEMP_DIR, 'input.avi')
    output_zip = os.path.join(TEMP_DIR, 'decoded.zip')

    video_file.save(video_path)
    video_to_zip(video_path, output_zip)

    return send_file(output_zip, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
