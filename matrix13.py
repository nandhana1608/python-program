
import numpy as np

# Create image matrix
image = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print("Original Image:")
print(image)

# Reshape image
print("\nReshaped Image:")
print(image.reshape(1, 9))

# Slicing image
print("\nSliced Image:")
print(image[0:2, 0:2])

# Brightness adjustment using broadcasting
print("\nBrightness Adjusted Image:")
bright = image + 10
print(bright)

# Matrix multiplication
print("\nTransformed Image:")
matrix = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

result = np.dot(image, matrix)
print(result)
