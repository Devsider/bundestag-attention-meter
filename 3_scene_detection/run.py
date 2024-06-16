import os
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Path to the directory containing the images
image_dir = './images'

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

# Iterate over all images in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load and preprocess the image
        img_path = os.path.join(image_dir, filename)
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = preprocess_input(x)
        x = tf.expand_dims(x, axis=0)

        # Make predictions using the ResNet50 model
        preds = model.predict(x)
        predictions = decode_predictions(preds, top=3)[0]

        # Print the predictions for the image
        print(f'Predictions for {filename}:')
        for pred in predictions:
            print(f'{pred[1]}: {pred[2]}')
        print('---')