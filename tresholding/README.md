# Thresholding

This project utilizes OpenCV to apply thresholding techniques to an image in order to highlight its edges. The result of the thresholding process is shown below:

Original Image             | Thresholded Image (Edge Detection)
:-------------------------:|:-------------------------:
![Original Image](./man.jpg) | ![Thresholded Image](./man_edited.jpg)

## Usage

To run this project, ensure that you have OpenCV installed on your system. If you haven't installed it yet, please refer to the installation instructions provided in the main README of this repository.

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pachecowillians/opencv.git
   ```

2. Navigate to the `thresholding` directory:

   ```bash
   cd opencv/thresholding
   ```

3. Run the `thresholding.py` script:

   ```bash
   python thresholding.py
   ```

   This script will process the original image and apply thresholding to detect and mark the edges. The resulting image will be saved as `man_edited.jpg`.

4. View the resulting images:

   - `man.jpg` is the original image.
   - `man_edited.jpg` is the thresholded image with the highlighted edges.

Feel free to modify the `thresholding.py` script and experiment with different thresholding techniques or parameters to achieve desired effects. OpenCV provides a wide range of thresholding methods and options that can be explored further for image enhancement and analysis tasks.