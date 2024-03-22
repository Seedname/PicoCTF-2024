from PIL import Image
import numpy as np

# Assuming 'data' is your processed data array that you want to visualize as an image
# You might need to reshape or process 'data' to fit your needs

# Example: Create a 128x128 grayscale image from 'data'
image_data = np.reshape(data, (128, 128)).astype(np.uint8)
img = Image.fromarray(image_data, 'L')

# Save the image as BMP
img.save('output.bmp')