# Colorize Black & White Images with Python
<p>Like RGB, Lab is another color space. It is also three channel color space like RGB where the channels are:</p>
<p>L channel: This channel represents the Lightness</p>
<p>a channel: This channel represents green-red</p>
<p>b channel: This channel represents blue-yellow</p>
In this color space, the grayscale part of the image is only encoded in L channel. Therefore Lab color space is more favorable.
<p align="center">
  <figure class="image">
    <img src="https://github.com/wmkthi/Open-CV/blob/main/mkdir%20models/result.png" alt="Coloured Image" width="500" height="250">
    <figcaption>Original image</figcaption>
  </figure>
  <figure class="image">
    <img src="https://github.com/wmkthi/Open-CV/blob/main/mkdir%20models/test2.jpg" alt="Original Image" width="500" height="250">
    <figcaption>Coloured image</figcaption>
  </figure>
</p>

The problem statement can be formulated as to predict a and b channels, given an input grayscale image.
THis project uses OpenCV DNN architecture which is trained on ImageNet dataset. The neural net is trained with the L channel of images as input data and a,b channels as target data.

