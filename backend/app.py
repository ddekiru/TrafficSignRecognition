import torch
from PIL import Image
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/do_nothing')
def do_nothing():
    response = jsonify(message="This Flask backend does nothing!")
    return response

@app.route('/detect_traffic_sign', methods=['POST'])
def detect_traffic_sign_endpoint():
    image_file = request.files['image']
    image_file.save('a.png')

    image = Image.open("a.png")
    result = model(image)
    # result.show()
    result.save(exist_ok=True)

    return send_file("./runs/detect/exp/a.jpg", as_attachment=True)


if __name__ == '__main__':
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt', force_reload=True)
    app.run(debug=True)