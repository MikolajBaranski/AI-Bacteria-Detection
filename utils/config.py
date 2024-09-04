# Data location
RAW_DATA_PATH = "data/train_data"

# Data split parameters
TRAIN_SPLIT = 0.8
DATA_SPLIT_TRAIN_PATH = "data/train.txt"
DATA_SPLIT_VAL_PATH = "data/validation.txt"

# YOLO data parameters
DATA_YOLO_PATH = "data/data_yolo"

# Model training configuration
MODEL = 'yolov8l.pt'
DATA = 'training_instructions.yaml'
EPOCHS = 25
PATIENCE = 3
BATCH = 30
IMGSZ = 640
CLOSE_MOSAIC = 5
DEVICE = 1