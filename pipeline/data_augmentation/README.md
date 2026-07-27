Image Augmentation with TensorFlow – Summary of Implemented Methods

This repository contains a concise set of image augmentation operations implemented using TensorFlow’s tf.image API. The goal was to build a minimal, practical collection of transformations commonly used in computer vision pipelines to increase dataset variability and improve model robustness. Each augmentation is applied directly to 3-D image tensors and tested using the Stanford Dogs dataset from tensorflow_datasets.

Horizontal Flipping

A function was implemented to flip images horizontally. This operation introduces mirrored visual variants of the data, enabling models to generalize better when object orientation is not fixed.

Key API: tf.image.flip_left_right

Random Cropping

We added a function that performs random cropping based on a specified output size. Random crops expose the model to different spatial compositions of the same image, reducing overfitting and improving localization robustness.

Key API: tf.image.random_crop

90-Degree Rotation

A simple rotation function was created to rotate images 90 degrees counter-clockwise. This transformation provides directional variance and can help when orientation is not guaranteed in real-world data.

Key API: tf.image.rot90

Random Contrast Adjustment

A contrast-adjustment function was implemented, selecting a random factor within a user-defined range. Changing contrast helps models adapt to varying lighting conditions and different scene exposures.

Key API: tf.image.random_contrast

Random Brightness Adjustment

We implemented brightness augmentation by adding a random delta to the image’s brightness level. This prepares models to handle shadows, strong lighting, and other illumination changes.

Key API: tf.image.random_brightness

Hue Adjustment

Finally, a hue modification function was added to shift the color tone of the image. Altering the hue helps models become less sensitive to color variations and more focused on underlying structural features.

Key API: tf.image.adjust_hue

Dataset and Visualization

All augmentations were validated using samples from the Stanford Dogs dataset. Images were visualized with Matplotlib to ensure correctness of each transformation.

Summary

Collectively, these implementations cover a core subset of image augmentation techniques widely used in computer vision workflows. They provide a solid practical foundation for building more advanced augmentation pipelines or integrating them into training loops for deep learning models.