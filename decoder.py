import cv2
from pyzbar.pyzbar import decode
from PIL import Image

def video_to_zip(video_path, output_zip_path):
    cap = cv2.VideoCapture(video_path)
    decoded_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        qr_codes = decode(pil_img)
        if qr_codes:
            decoded_data.append(qr_codes[0].data)

    cap.release()

    with open(output_zip_path, 'wb') as f:
        for part in decoded_data:
            f.write(part)
