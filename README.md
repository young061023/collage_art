# collage_art

You can create mosaic pictures with the collage technique.

## Examples
<p align="center"><img width="300" alt="flower1" src="https://github.com/young061023/collage_art/assets/116246341/494b9ff5-4c06-4e75-ab8a-08df5cc0e145">
<img width="300" alt="flowr" src="https://github.com/young061023/collage_art/assets/116246341/c568c740-f2ed-420f-af8e-6652f4211c65"></p>
<br/>
<p align="center"><img width="300" alt="crow1" src="https://github.com/young061023/collage_art/assets/116246341/fc3c52e2-4b77-4ec9-a6e7-4c0b8b5a6e16">
<img width="300" alt="corw" src="https://github.com/young061023/collage_art/assets/116246341/016b18b4-d1d3-4903-9388-2a0bd4fe07d5"></p>

## Overview
The script performs the following operations:

#### 1. Generate Image Grid
  - Takes an input image and creates a 2x2 grid using different transformations (mirroring and rotation).
  - Saves the resulting grid as a new image.

#### 2. Cut and Stack Images
  - Take the generated image grid and slice it horizontally with the specified number of n.
  - 1, n, 2, n-2, 3, n-3... Arrange them in order.

#### 3. Cut and Stack Images (Part. 2)
  - Cut out the photo made vertically at 2 by the specified n.
  - If you stack the cut-out pictures alternately as shown in 2, you create an image like the final mosaic.

#### 4. Crop Image
  - Cut the final mosaic image so that only one picture comes out.

## Usage

#### Installation
```
pip install pillow
```
#### Parameters

  * ##### input_image_path: The path of the input image file.
  * ##### output_image_path: The path to store the generated image.
  * ##### level1_image_path, level2_image_path, level3_image_path: the path to store the intermediate image.
  * ##### final_image_path: The path to save the final cropped image.
  * ##### num_slice: the number of slices used to segment a picture.

#### Result
The script will output a final processed image (final.jpg) after completing the image processing pipeline.

## process
<img width="180" alt="a" src="https://github.com/young061023/collage_art/assets/116246341/87c22e60-9336-477d-ab58-19bdcb3ff8bb">
<img width="180" alt="c" src="https://github.com/young061023/collage_art/assets/116246341/0072b0a2-32c7-44ab-98f5-bf49a97cd205">
<img width="180" alt="d" src="https://github.com/young061023/collage_art/assets/116246341/17544cf4-60a5-4bcb-ae50-47eccd3326ae">
<img width="180" alt="e" src="https://github.com/young061023/collage_art/assets/116246341/2ef437f1-1ce6-4d8f-9433-34374e1120c3">
<img width="180" alt="b" src="https://github.com/young061023/collage_art/assets/116246341/96d27262-4e0b-4233-befa-0405db7ff5c0">

