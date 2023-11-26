# Project Description

The Windows on Earth program receives astronaut photos from the International Space Station (ISS). We know the location of the ISS when the photo was taken, but not what the photo is of. The subject is generally in a 300 mile radius of ISS location. 

This project seeks to use image recognition/machine learning combined with a virtual world simulator (we use Cesium) to attempt to geolocate the images automatically. We have a website at [Windows on Earth](https://www.windowsonearth.org/). 

Our goal is to accurately "predict" the location of the image. Specifically, we need the ability to recognize what the image is of, based on a simulated view of the world using things such as coastal or lake outlines, rivers, and other features. The system would need to "look around" in the simulation trying to match the photo to likely subjects (again, usually within 300 miles radius).

# [Project Members](COLLABORATORS)

- Hemant Kumar Singh
- Jaisal Singh
- Vedika Srivastava

<!-- # [Project Outline](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/project-outline.md) -->

# Expermients and Notebook Description:

### [Poc_pipeline-usingSIFT.ipynb](notebooks/Poc_pipeline-usingSIFT.ipynb)
This notebook documents one of our initial approaches which utilized the Scale-Invariant Feature Transform (SIFT) for template matching, aiming to identify the query image within a designated area of interest. Below are the key points and outcomes from this approach:
- **Initial Attempts with Google Maps API:** The preliminary method involved generating an area of interest using the Google Maps API. This service, however, was limited to producing images of 640x640 pixels, which often proved insufficient for covering the entire query image.
- **Transition to Mapbox API:** To overcome the size constraint, we switched to the Mapbox API. This allowed us to create images as large as 3000x3000 pixels. It's important to note that generating such large images takes approximately 1 minute, with even larger images requiring 3-4 minutes. For our project needs, a 3000x3000 image at zoom level 10 was generally adequate.
- **Direct SIFT Matching:** We initially attempted to match the query image directly to the area of interest using SIFT. The results, however, were unsatisfactory as illustrated below: \
![Alt text](assets/images/image.png) \
This image showcases the ineffectiveness of direct SIFT matching on the generated area of interest.
- **Subsampling for Template Matching:** Our next step involved subdividing the area of interest into smaller segments and performing template matching on these subsamples. Despite this effort, the best match identified by the algorithm was inaccurate, as demonstrated in the following image: \
![Alt text](assets/images/image-1.png) \
This image represents the algorithm's best match, which is evidently incorrect.
- **Experiments with Zoom Levels and Image Sizes:** Further experimentation was conducted with varying zoom levels and sizes of the area of interest, still employing the subsampling method. These modifications, unfortunately, did not yield successful results either. The following images depict the lackluster outcomes from these trials: \
![Alt text](assets/images/image-2+3.png) \
These images display unsuccessful attempts at matching, using different zoom levels and sizes.

The experiments conducted in this notebook highlight the challenges of applying SIFT for direct image matching in a complex task like geolocating images from the ISS. Despite the setbacks, these attempts have been instrumental in guiding us towards more refined methods.


### [Poc_pipeline_NN.ipynb](notebooks/Poc_pipeline_NN.ipynb)
This notebook explores a different approach from the previous SIFT-based method, employing a neural network-based image recognition technique to identify geographic features in astronaut photos from the ISS.
- **Key Aspects of this Approach:** A shift from SIFT to leveraging the VGG16 model, a neural network pre-trained on ImageNet data. This model is known for its effectiveness in image recognition tasks, which we harness to extract features from the images. We preprocess the images to fit the input requirements of the VGG16 model and perform feature extraction. The extracted features then undergo a cross-correlation process to find potential matches within the area of interest, followed by a peak-finding algorithm to determine the best match.
- **Results**
The application of the neural network-based approach using the VGG16 model has yielded promising results for a subset of images. Our method involved identifying the best two matches within the area of interest and pinpointing their central location.\
    - _Challenges with Cloud Cover:_ In one instance, the algorithm accurately detected the target area, as shown in the sequence of images below. The first image is the query image, while the second image demonstrates the detected location, marked by a blue dot.\
    ![Alt text](assets/images/image-4+5.png) \
    The cloud cover, which can obscure relevant features, was a significant factor in this case. The area of interest for this image was sampled at a zoom level of 10 with a resolution of 3000x3000 pixels.
    - _Successful Detection:_ The algorithm managed to locate the correct position in another set of images. The first image below is the query, followed by the image displaying the detected location with a blue dot. \
    ![Alt text](assets/images/image-6+7.png) \
    Notably, for this correct match, the area of interest was generated at a zoom level of 9.5. This indicates that zoom levels are critical to the algorithm's performance, suggesting a need for further optimization to enhance robustness.


### [sliding_window_matcher_final.ipynb](notebooks/sliding_window_matcher_final.ipynb)
-

### [sliding_window_matcher_final_NN+SIFT.ipynb](notebooks/sliding_window_matcher_final_NN+SIFT.ipynb)
In our continued efforts to refine the geolocation pipeline, we ventured to combine the strengths of both [Neural Networks (NN)]((https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/Poc_pipeline_NN.ipynb)) and the [Scale-Invariant Feature Transform (SIFT)](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/sliding_window_matcher_final.ipynb) algorithms. Our objective was to enhance the robustness and accuracy of our pipeline by integrating these two powerful methods. Our idea was to extract features using VGG16 Imagenet weights and then compare using SIFT. However we encountered a fundamental compatibility challenge. The feature extraction process with VGG16 yields a high-dimensional representation of the image's content. This transformation results in the loss of the original pixel structure necessary for the SIFT algorithm, which operates on grayscale images and requires that pixel structure to identify and match key points.

### [Poc_pipeline_LoFTR.ipynb](notebooks/Poc_pipeline_LoFTR.ipynb)
Building upon the insights from our previous experiments, this notebook introduces the implementation of the LoFTR (Local Feature Transformer) algorithm, as detailed in the original [LoFTR](https://zju3dv.github.io/loftr/) paper. LoFTR leverages a transformer-based architecture to match features across images with wide baseline separations and varied viewpoints, making it well-suited for analyzing ISS photographs. Its ability to handle significant appearance changes and partial occlusions makes it a strong candidate for improving the accuracy of geolocating ISS photographs within the vast and visually diverse landscapes of Earth. Following are some results obtained by LoFTR: \
![Alt text](assets/images/image-8.png) \
![Alt text](assets/images/image-9.png) \
![Alt text](assets/images/image-10.png) \
As we can see, the algorithm is not able to detect the location accurately, it certainly performs slightly better on islands or continents however it struggles with more zoomed-in locations.

# Future Work and Suggestions: