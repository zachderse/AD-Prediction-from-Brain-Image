# AD-Prediction-from-Brain-Image
Uses Machine Learning to predict AD score from a cross-sectional image of brains.
Trying different types of models including binary to find how accurate and how specific the data can be classified.

Both pytorch and tensorflow seem to have issues discovering the distinction between 0, 0.5, and 1 using the prebuilt models. Further optimizations are needed to be done to fine-tune to this sparse dataset.
