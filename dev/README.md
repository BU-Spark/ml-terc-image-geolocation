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

 This notebook aims to implement SIFT in fine-tuned way for the distinctive aspects of aerial photography, with the aim to accurately match Earth's geographical features as captured from ISS.
Key aspects: 
- **Metadata extraction**:  Essential metadata is extracted from the EXIF data of ISS images, which includes:
    - **GPSLatitudeRef, GPSLatitude, GPSLongitudeRef, GPSLongitude**: These provide the ISS's exact coordinates at the time the photo was captured.

    - **GPSAltitude, Model, FocalLength**: These are used to determine the camera's field of view and the approximate area covered in the photo.
- **Generation of Area of Interest Image**: A high-resolution Area of Interest (AOI) image (30,000 x 30,000 pixels) that spans an area of 1200km x 1200km is constructed with center pixel having GPS coordinates of ISS and has zoom level 11. We leveraged a publicly available git repository which uses an image stitching technique, aggregating multiple small tiles from Google Maps into one large image.
- **Matching process**: A series of subsampled images are generated from the AOI image, each subsample image covers an area correlating with the area visible in the ISS image (query image). For example, if query image covers 8 km x 12 km area, then a subsample will cover 13 km x 20 km area. The objective is to create at least one subsample image in which the location featured in the query image is present clearly. Then, SIFT matching is performed for each subsample against the query image. Finally, we get the matching value of each comparison and we take the highest matched subsample as our result.
- **Results and Execution**: An Excel spreadsheet functions as a database to input multiple image names, which subsequently displays the GPS coordinates of center pixels of best matched sample in the corresponding columns. For validation purposes, images with known coordinates are included to assess the proximity of the predicted coordinates to the actual labeled locations.

### [sliding_window_matcher_final_v2.ipynb](notebooks/sliding_window_matcher_final_v2.ipynb)

In this iteration, we introduced enhancements to refine our model:
- **Preclusion Criterion**: We implemented a preclusion criterion, discarding any image that predominantly shows water with no significant landmass, aligning with the dataset's characteristics in which each image has some landmass. This will help reduce the number of images to match and it solves an issue where best matches for a query image with significant landmass were ocean water bodies.
- **Updated Result Strategy**: Afte the SIFT comparison, the GPS coordinates of center pixels of top two best matched sample images are stored as result. Sometimes the first match resembles the query image but it is not the location we wanted, and second match is our actual location in the query image. 

### [sliding_window_matcher_final_v3.ipynb](notebooks/sliding_window_matcher_final_v3.ipynb)

In this iteration, we updated our result format to work better in docker container.
- **Data Format Conversion**: We converted our excel sheet into a csv file as it is convenient to access. For validation purposes, images with known coordinates are included to assess the proximity of the predicted coordinates to the actual labeled locations. 

#### Below figure shows a query image, its corresponding AOI image the the best matched subsampled images.

![Sample prediction 1](./assets/images/SIFT_result_1.png)

![Sample prediction 2](./assets/images/SIFT_result_2.png)


#### Below results shows 3 query images, there labeled location and predicted location.

![SIFT Sample Results](./assets/images/SIFT_result_3.png)

### [sliding_window_matcher_final_NN+SIFT.ipynb](notebooks/sliding_window_matcher_final_NN+SIFT.ipynb)
In our continued efforts to refine the geolocation pipeline, we ventured to combine the strengths of both [Neural Networks (NN)]((https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/Poc_pipeline_NN.ipynb)) and the [Scale-Invariant Feature Transform (SIFT)](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/sliding_window_matcher_final.ipynb) algorithms. Our objective was to enhance the robustness and accuracy of our pipeline by integrating these two powerful methods. Our idea was to extract features using VGG16 Imagenet weights and then compare using SIFT. However we encountered a fundamental compatibility challenge. The feature extraction process with VGG16 yields a high-dimensional representation of the image's content. This transformation results in the loss of the original pixel structure necessary for the SIFT algorithm, which operates on grayscale images and requires that pixel structure to identify and match key points.

## Notable approaches that underperformed:
In our quest for a superior image matching solution, we explored various other techniques: We tried to check different image matching techniques to check and see how well they perform.


### [Poc_pipeline_LoFTR.ipynb](notebooks/Poc_pipeline_LoFTR.ipynb)
Building upon the insights from our previous experiments, this notebook introduces the implementation of the LoFTR (Local Feature Transformer) algorithm, as detailed in the original [LoFTR](https://zju3dv.github.io/loftr/) paper. LoFTR leverages a transformer-based architecture to match features across images with wide baseline separations and varied viewpoints, making it well-suited for analyzing ISS photographs. Its ability to handle significant appearance changes and partial occlusions makes it a strong candidate for improving the accuracy of geolocating ISS photographs within the vast and visually diverse landscapes of Earth. Following are some results obtained by LoFTR: \
![Alt text](assets/images/image-8.png) \
![Alt text](assets/images/image-9.png) \
![Alt text](assets/images/image-10.png) \
As we can see, the algorithm is not able to detect the location accurately, it certainly performs slightly better on islands or continents however it struggles with more zoomed-in locations.


### SE2-LoFTR:
SE2-LOFTR, a rotation-equivariant version of LoFTR using steerable CNNs, initially seemed promising. However, its pre-training on outdoor and indoor scenes didn't translate well to aerial imagery, resulting in suboptimal matches for our task. More details can be found here. https://github.com/georg-bn/se2-loftr

Following is a sample result from SE2-LoFTR.
![SE2-LoFTR Result](./assets/images/Se2-loftr_result.png)


### CasMTR:
CASMTR aimed to enhance Transformer-based image matching by capturing spatially informative keypoints. Despite its potential, its heavy GPU requirements led to computational resource allocation errors, hindering its practical application in our project. More details can be found here. https://github.com/ewrfcas/CasMTR


# Evaluations on the Pipelines:
## Pipeline 1 (NN):
![issues-pie](./assets/images/nn-eval-pie-1.png) ![error](./assets/images/nn-bar-eval.png)

## Pipeline 2 (SIFT):

## Pipeline 3(GPT-4):

# Future Work and Suggestions: