from ultralytics import YOLO
model = YOLO("yolov8n.pt")  # build a new model from scratch
# Use the model
model.train(data="data.yaml", epochs=100, batch = 8, device=0)
