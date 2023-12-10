# Project Description

The Windows on Earth program receives astronaut photos from the International Space Station (ISS). We know the location of the ISS when the photo was taken, but not what the photo is of. This project seeks to use image recognition/machine learning to attempt to geolocate the images automatically. We have a website at [Windows on Earth](https://www.windowsonearth.org/). Our goal is to accurately "predict" the location of the image.

# [Project Members](COLLABORATORS)

- Hemant Kumar Singh
- Jaisal Singh
- Vedika Srivastava

<!-- # [Project Outline](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/project-outline.md) -->

# Expermients and Pipeline Description:

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

**Below figure shows a query image, its corresponding AOI image the the best matched subsampled images.**

![Sample prediction 1](./assets/images/SIFT_result_1.png)

![Sample prediction 2](./assets/images/SIFT_result_2.png)


**Below results shows 3 query images, there labeled location and predicted location.**

![SIFT Sample Results](./assets/images/SIFT_result_3.png)

### [sliding_window_matcher_final_NN+SIFT.ipynb](notebooks/sliding_window_matcher_final_NN+SIFT.ipynb)
In our continued efforts to refine the geolocation pipeline, we ventured to combine the strengths of both [Neural Networks (NN)]((https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/Poc_pipeline_NN.ipynb)) and the [Scale-Invariant Feature Transform (SIFT)](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/sliding_window_matcher_final.ipynb) algorithms. Our objective was to enhance the robustness and accuracy of our pipeline by integrating these two powerful methods. Our idea was to extract features using VGG16 Imagenet weights and then compare using SIFT. However we encountered a fundamental compatibility challenge. The feature extraction process with VGG16 yields a high-dimensional representation of the image's content. This transformation results in the loss of the original pixel structure necessary for the SIFT algorithm, which operates on grayscale images and requires that pixel structure to identify and match key points.

## TerraByte (based on GPT4 with Vision model)
### Introduction
TerraByte is a specialized AI model designed to analyze and geolocate images of Earth taken from the International Space Station (ISS). It identifies geographical and man-made features to predict the location depicted in the images. It is based on a customizable GPT4 model that is offered by OpenAI. It is publicly accessible with this link: [TerraByte](https://chat.openai.com/g/g-cGxe4cVEb-terrabyte) (requires GPT4 subscription for use).

### How to Use TerraByte
**Step 1: Image Submission**
- Provide an Image: Upload an image of Earth taken from the ISS for analysis.

**Step 2: ISS Location Information**
- Provide ISS Coordinates: If available, include the approximate GPS coordinates of the ISS at the time the image was taken. This helps in narrowing down potential locations.
- ISS Coordinates: Providing accurate ISS coordinates at the time of the image capture significantly enhances location prediction accuracy. However, if the location of the ISS is quite far from the location in the image, it might cause inaccurate identification.

### Sample Usage Screenshots
**1. Input: Amur Darya basin in Uzbekistan** \
![image5](./assets/TerraByte/img1.png)

**Output**: 
_“The landscape in the image is quite distinctive and could be identified as part of the Amu Darya river basin, which fits the geography of Central Asia. The Amu Darya river is one of the major rivers of the region, flowing through countries like Tajikistan, Afghanistan, Turkmenistan, and Uzbekistan. It's known for creating fertile oases in an otherwise very arid region and for its meandering path, which seems to match the winding patterns in the image._

_The large water bodies could potentially be man-made reservoirs, which are common in this region for irrigation and hydroelectric power generation. The presence of infrastructure such as roads or small settlements can be inferred from the patchy white spots, which may indicate human activity in an otherwise natural landscape.”_

**2. Input: Picture of Sinai Peninsula and Nile river in Egypt** \
![image3](./assets/TerraByte/img2.png)

**Output**:
_“The image shows a distinctive geological feature: a narrow waterway running through an arid region, separating two larger landmasses with varying terrain. The presence of cloud formations near the water indicates that the image was taken from a significant altitude, fitting the perspective of the International Space Station._

_Given the ISS location at approximately 33.40787°N latitude and 22.99734°E longitude, this places the ISS above Northeast Africa. The waterway shown in the image is very likely the Suez Canal, a man-made canal in Egypt that connects the Mediterranean Sea to the Red Sea, allowing for direct maritime passage between Europe and Asia without navigating around Africa._

_The image shows the canal running from the top left to the bottom right, with the Sinai Peninsula to the right and the Eastern Desert of Egypt to the left. The northern end of the Red Sea is visible at the bottom right corner, and the Mediterranean Sea would be out of the frame at the top left corner.”_

**3. Input: Picture of Jamaica** \
![image4](./assets/TerraByte/img3.png)

**Output**:
_“The image features an island with a complex coastline, surrounded by the deep blue of the ocean. There are visible cloud formations, which are particularly dense in the top-left corner, but the island itself is clear. The variances in water color around the coastline suggest shallow waters, possibly coral reefs, which are typical in tropical regions._

_The provided ISS coordinates are approximately 18.47024°N latitude and -80.37414°W longitude, which places the ISS above the Caribbean Sea. This region is known for its numerous islands, many of which are characterized by similar features to those visible in the image: lush vegetation, complex coastlines, and surrounding reef systems._

_Given the latitude and the appearance of the island, it could potentially be one of the larger islands in the Greater Antilles, such as Cuba, Hispaniola (the island shared by Haiti and the Dominican Republic), Jamaica, or Puerto Rico. However, the size and shape of the island, as well as the specific reef patterns, would need to be compared with maps or satellite imagery to determine the exact island.”_

**4. Input: Picture of Lake Tanganyika in Central Africa** \
![image1](./assets/TerraByte/img4.png)

**Output**:
_“The image shows a vast water body with a highly irregular shoreline and cloud cover interspersed throughout the area. The water appears to have different shades, indicating varying depths or sediment levels. The land areas exhibit a range of colors, suggesting different soil types, vegetation densities, or perhaps even agricultural use._

_The provided ISS coordinates are approximately 8.04204°S latitude and 30.28798°E longitude. This places the ISS over the African continent._

_Considering the shape of the water body and the location, this image is likely depicting Lake Tanganyika, which is one of the African Great Lakes. Lake Tanganyika is known for its elongated shape, significant depth, and it borders several countries including Tanzania, the Democratic Republic of the Congo (DRC), Burundi, and Zambia._

_The lake's distinctive features, such as its length and the surrounding topography, help in its identification. The northern end of the lake, which would be situated toward the upper part of the image, narrows and is bordered by mountainous regions, which is consistent with the geography of the area where the lake's shoreline comes close to the Rwenzori Mountains._

_The scale of the image and the ISS's vantage point suggest that a large portion of Lake Tanganyika is visible, potentially spanning hundreds of kilometers from north to south.”_


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


# Instruction to run the final pipelines can be found at [readme.md](../readme.md)

# Evaluations on the Pipelines:
## Pipeline 1 (NN):
The evaluations for this pipeline where run on a diverse set of over 140 images captured by the ISS. The following Figure shows a side-by-side comparison of labelled and predicted locations for various geographic features. Each pair of images compares the ground truth (labelled location) with the neural network's prediction (predicted location). The labelled location images here aren't query image they are images generated by Google Maps. The actuall query image mostly differ in scale or have details such as cloud cover. It is noteworthy that the model is able to perform very well given the noise the actual query images and is quite reliable.

![some outputs](./assets/images/nn-eval-res.png)

The following chart displays the distribution of images based on the area range they cover. The majority of the images fall within the smallest area range (0-1k km²), suggesting that the dataset has a significant number of images with detailed, small-scale features.

![area](./assets/images/area-eval.png)

The pie chart (below left) shows the percentage breakdown of the model's outcomes: successful matches, failures to find a match, and images with problems. A large portion (75.52%) of the images resulted in a match found, indicating a relatively high success rate of the neural network. A smaller segment (23.08%) shows that for a considerable number of images, the model could not find a match, which could be due to various factors like image quality, lack of distinctive features, occlusions, clouds, or artifacts that prevent the model from processing the image correctly. A tiny fraction (1.40%) indicates problems with the image itself, which in this case that the ISS latitude location was missing.

![issues-pie](./assets/images/nn-eval-pie-1.png)  ![error](./assets/images/nn-bar-eval.png)

The (above right) plots represent the density of errors in degrees for predicted latitude and longitude values against the best match values obtained by the neural network. For both latitude and longitude predictions, there's a noticeable concentration of density near the lower error values, which is a good sign as it indicates that most predictions are close to the correct values.

Find other plots and details (numbers) in [NN-Eval-Analysis.ipynb](./notebooks/NN-Eval-Analysis.ipynb)


## Pipeline 2 (SIFT):

## Pipeline 3(GPT-4):
Overall, TerraByte has performed really well, considering that the base GPT-4 model has been unable to even make a prediction on most images. TerraByte’s strength lies in the fact that it only requires an image upload and a rough ISS location. No extra prompting is required for it to get to work. The following chart depicts the performance of the TerraByte model:

![eval](./assets/TerraByte/eval.png)

We see that almost 90% of images can be approximately geolocated by the TerraByte model. It also correctly names the visible islands, rivers, lakes, and other prominent features visible in the image as well as describing the overall geography of the region. It can correctly identify the scale of the image as well.
### Drawbacks
- **Prominent Geographical Features**: If an image contains a single prominent geographical feature such as a lake or an island, and the region itself has more than one prominent feature of that type, then TerraByte generally resorts to predicting the most prominent of those locations that may result in inaccuracy.
- **Distance from ISS**: If the region depicted in the image is quite far from the ISS location (>1500-2000 miles), then it may struggle to take into account locations so far away, unless the features visible are quite unique.

# Conclusion and Future Work:

The Neural Network (NN) pipeline, has demonstrated a commendable capacity for geolocating images from the ISS. Through rigorous testing on over 140 diverse images, the NN has shown a high success rate, with a large majority of images accurately matched to their corresponding geographical features. The pipeline effectively handled a variety of challenges inherent in space-based photography, such as varying scales, cloud cover, and other noise factors in the images. Moving forward, implementing advanced image preprocessing techniques could mitigate the effects of image noise, such as cloud cover and artifacts, which currently pose challenges to the model's accuracy.

TerraByte is a powerful tool for ISS image analysis, offering insights into Earth's geography from an orbital perspective. Whether for educational, research, or curiosity purposes, TerraByte provides a unique way to explore our planet from above. It also provides a detailed description of the image that may be useful for further analysis or research. Since TerraByte can narrow down possible options very well, training it on small detailed maps of the world may significantly enhance its capabilities for identifying locations correctly.