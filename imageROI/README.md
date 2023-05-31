# Image ROI

This project showcases the usage of OpenCV to define a Region of Interest (ROI) in an image, scale it, and insert it back into the original image. The resulting images are displayed below:

Original Image             | Edited Image
:-------------------------:|:-------------------------:
![Original Image](./manCubeSword.jpg) | ![Edited Image](./manCubeSword_edited.jpg)

## Usage

To run this project, make sure you have OpenCV installed on your system. If not, please refer to the installation instructions provided in the main README of this repository.

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/pachecowillians/opencv.git
   ```

2. Navigate to the `imageROI` directory:

   ```bash
   cd opencv/imageROI
   ```

3. Run the `imageROI.py` script:

   ```bash
   python imageROI.py
   ```

   This will process the original image, define a Region of Interest (ROI), scale it, and save the edited image as `manCubeSword_edited.jpg`.

4. View the resulting images:

   - `manCubeSword.jpg` is the original image.
   - `manCubeSword_edited.jpg` is the edited image with the scaled ROI inserted.

Feel free to modify the `imageROI.py` script and experiment with different regions and scaling factors to further explore the capabilities of OpenCV for working with ROIs in images.