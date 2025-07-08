import qrcode
import cv2
import numpy as np
from utils import chunk_data

def zip_to_video(zip_path, video_path, chunk_size=1000, fps=30):
    with open(zip_path, 'rb') as f:
        data = f.read()

    chunks = chunk_data(data, chunk_size)
    qr_images = []

    for chunk in chunks:
        qr = qrcode.make(chunk)
        img = qr.convert('RGB')
        qr_images.append(np.array(img))

    height, width, _ = qr_images[0].shape
    out = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

    for frame in qr_images:
        out.write(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    out.release()
