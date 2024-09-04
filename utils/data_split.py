import os
import random
from utils.config import (
    TRAIN_SPLIT, 
    RAW_DATA_PATH, 
    DATA_SPLIT_TRAIN_PATH, 
    DATA_SPLIT_VAL_PATH
    )

def data_split(train_split = TRAIN_SPLIT, raw_data_path = RAW_DATA_PATH,
               data_split_train_path = DATA_SPLIT_TRAIN_PATH,
               data_split_val_path = DATA_SPLIT_VAL_PATH):
    # Define the directory containing the files
    directory = RAW_DATA_PATH

    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Extract unique file names without extensions
    unique_filenames = {os.path.splitext(file)[0] for file in files}

    # Split filenames into train and validation sets
    num_files = len(unique_filenames)
    num_train = int(train_split * num_files)
    train_filenames = random.sample(unique_filenames, num_train)
    validation_filenames = unique_filenames - set(train_filenames)

    # Write train and validation filenames to text files
    with open(data_split_train_path, "w") as train_file:
        for filename in train_filenames:
            train_file.write(filename + "\n")

    with open(data_split_val_path, "w") as validation_file:
        for filename in validation_filenames:
            validation_file.write(filename + "\n")