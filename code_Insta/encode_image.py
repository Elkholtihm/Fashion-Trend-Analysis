from tensorflow.keras.models import Model, load_model
import numpy as np
import cv2 
import os 


autoencoder = load_model("models/autoencoder.h5")
autoencoder.summary()
encoder = Model(inputs=autoencoder.input, outputs=autoencoder.get_layer('dropout_4').output)

def encode(image_name):
    path = os.path.join("images/original_images", image_name)
    if not os.path.exists(path):
        return None
    img = cv2.imread(path)
    img = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (256, 256))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    latent = encoder.predict(img, verbose=0).flatten()
    return latent
