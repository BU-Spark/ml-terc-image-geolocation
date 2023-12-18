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

### [sliding_window_matcher_final_NN+SIFT.ipynb](notebooks/sliding_window_matcher_final_NN+SIFT.ipynb)
In our continued efforts to refine the geolocation pipeline, we ventured to combine the strengths of both [Neural Networks (NN)]((https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/Poc_pipeline_NN.ipynb)) and the [Scale-Invariant Feature Transform (SIFT)](https://github.com/BU-Spark/ml-terc-image-geolocation/blob/dev-patch-1/notebooks/sliding_window_matcher_final.ipynb) algorithms. Our objective was to enhance the robustness and accuracy of our pipeline by integrating these two powerful methods. Our idea was to extract features using VGG16 Imagenet weights and then compare using SIFT. However we encountered a fundamental compatibility challenge. The feature extraction process with VGG16 yields a high-dimensional representation of the image's content. This transformation results in the loss of the original pixel structure necessary for the SIFT algorithm, which operates on grayscale images and requires that pixel structure to identify and match key points.

### [Poc_pipeline_LoFTR.ipynb](notebooks/Poc_pipeline_LoFTR.ipynb)
Building upon the insights from our previous experiments, this notebook introduces the implementation of the LoFTR (Local Feature Transformer) algorithm, as detailed in the original [LoFTR](https://zju3dv.github.io/loftr/) paper. LoFTR leverages a transformer-based architecture to match features across images with wide baseline separations and varied viewpoints, making it well-suited for analyzing ISS photographs. Its ability to handle significant appearance changes and partial occlusions makes it a strong candidate for improving the accuracy of geolocating ISS photographs within the vast and visually diverse landscapes of Earth. Following are some results obtained by LoFTR: \
![Alt text](assets/images/image-8.png) \
![Alt text](assets/images/image-9.png) \
![Alt text](assets/images/image-10.png) \
As we can see, the algorithm is not able to detect the location accurately, it certainly performs slightly better on islands or continents however it struggles with more zoomed-in locations.

# Evaluations on the Pipelines:
## Pipeline 1 (NN):
![issues-pie](./assets/images/nn-1.png)

## Pipeline 2 (SIFT):

## Pipeline 3(GPT-4):

# TerraByte (based on GPT4 with Vision model)

## Introduction
TerraByte is a specialized AI model designed to analyze and geolocate images of Earth taken from the International Space Station (ISS). It identifies geographical and man-made features to predict the location depicted in the images. It is based on a customizable GPT4 model that is offered by OpenAI. It is publicly accessible with this link: [TerraByte](https://chat.openai.com/g/g-cGxe4cVEb-terrabyte) (requires GPT4 subscription for use).

## TerraByte: Evolution of Capabilities

### Initial Role and Configuration
TerraByte was initially designed as a geography expert, focusing on analyzing satellite imagery, particularly from the International Space Station (ISS). It was capable of identifying geographical features in these images, such as terrain types and visible infrastructure, using approximate ISS location data to estimate the depicted region of Earth.

### Capability Enhancements

#### Initial Configuration
- **Image Analysis**: Analyze Earth images from the ISS.
- **Feature Identification**: Identify major geographical features like mountains, rivers, and urban areas.
- **Location Estimation**: Use ISS's approximate coordinates to narrow down the potential region shown in the image.

#### Enhanced Feature Identification
- **Detection Improvement**: Enhanced ability to detect unique natural formations and notable man-made structures.
- **Detail Recognition**: Identify shapes of coastlines, mountain ranges, significant structures like bridges and airports.

#### Scale Assessment and Location Prediction
- **Image Scale Understanding**: Refined assessment of the scale of images for a better understanding of the area extent.
- **Precise Location Prediction**: Predict location more accurately, identifying general regions or specific places based on image detail.

#### Analytical Comparison and Naming of Features
- **Feature Analysis**: Analyze features for distinctiveness and orientation within the estimated region.
- **Feature Naming**: Begin naming identifiable landforms, bodies of water, and significant man-made structures.

#### Efficiency and User Interface Improvements
- **Processing Efficiency**: Focus on prioritizing processing efficiency.
- **Output Clarity**: Improve the clarity of output presentation with advanced pattern recognition and analytical capabilities.

#### Return to Geo Explorer Model
- **Educational Focus**: Briefly reverted to "Geo Explorer" configuration, focusing on providing educational geography and map analysis.

#### Reversion to TerraByte with Enhanced Context
- **Updated Context**: Reinstated with detailed processes for extracting geographical features, considering image scale, and predicting image location with enhanced accuracy and naming capabilities.

### Ongoing Improvements
Throughout these updates, TerraByte has remained a sophisticated tool for interpreting satellite imagery, continually improving in accuracy, efficiency, and user experience.



## How to Use TerraByte
### Step 1: Image Submission
- **Provide an Image**: Upload an image of Earth taken from the ISS for analysis.

### Step 2: ISS Location Information
- **Provide ISS Coordinates**: If available, include the approximate GPS coordinates of the ISS at the time the image was taken. This helps in narrowing down potential locations.

### Step 3: Analysis Request
- **Request Analysis**: Ask TerraByte to geolocate the image. You can include specific questions or details you're interested in, such as identifying particular geographical features or confirming a suspected location.

### Step 4: Review TerraByte's Analysis
- **Examine the Analysis**: TerraByte will extract and identify natural and man-made features visible in the image. It will then try to determine the region of Earth depicted in the image based on the analysis. If the exact location is uncertain, TerraByte will offer a list of likely locations. 

### Step 5: Follow-up Questions
- **Clarify and Explore Further**: Feel free to ask follow-up questions or request more details about any part of TerraByte's analysis.

## Tips for Best Results
- **Image Quality**: High-resolution images with distinct geographical markers yield better results.
- **ISS Coordinates**: Providing accurate ISS coordinates at the time of the image capture significantly enhances location prediction accuracy. However, if the location of the ISS is quite far from the location in the image, it might cause inaccurate identification.

## Sample Usage Screenshots

### 1. Input: Amur Darya basin in Uzbekistan
![image5](https://github.com/BU-Spark/ml-terc-image-geolocation/assets/118229570/1b472d8a-2491-4171-9110-bad6c93c0677)


**Output**: 
“The landscape in the image is quite distinctive and could be identified as part of the Amu Darya river basin, which fits the geography of Central Asia. The Amu Darya river is one of the major rivers of the region, flowing through countries like Tajikistan, Afghanistan, Turkmenistan, and Uzbekistan. It's known for creating fertile oases in an otherwise very arid region and for its meandering path, which seems to match the winding patterns in the image.

The large water bodies could potentially be man-made reservoirs, which are common in this region for irrigation and hydroelectric power generation. The presence of infrastructure such as roads or small settlements can be inferred from the patchy white spots, which may indicate human activity in an otherwise natural landscape.”

### 2. Input: Picture of Sinai Peninsula and Nile river in Egypt
![image3](https://github.com/BU-Spark/ml-terc-image-geolocation/assets/118229570/8d1d1d87-94b3-474e-bc8f-4342dd4783b1)

**Output**:
“The image shows a distinctive geological feature: a narrow waterway running through an arid region, separating two larger landmasses with varying terrain. The presence of cloud formations near the water indicates that the image was taken from a significant altitude, fitting the perspective of the International Space Station.

Given the ISS location at approximately 33.40787°N latitude and 22.99734°E longitude, this places the ISS above Northeast Africa. The waterway shown in the image is very likely the Suez Canal, a man-made canal in Egypt that connects the Mediterranean Sea to the Red Sea, allowing for direct maritime passage between Europe and Asia without navigating around Africa.

The image shows the canal running from the top left to the bottom right, with the Sinai Peninsula to the right and the Eastern Desert of Egypt to the left. The northern end of the Red Sea is visible at the bottom right corner, and the Mediterranean Sea would be out of the frame at the top left corner.”

### 3. Input: Picture of Jamaica
![image4](https://github.com/BU-Spark/ml-terc-image-geolocation/assets/118229570/c9d2fe5b-8ffa-4489-be0a-41a10a8ada61)

**Output**:
“The image features an island with a complex coastline, surrounded by the deep blue of the ocean. There are visible cloud formations, which are particularly dense in the top-left corner, but the island itself is clear. The variances in water color around the coastline suggest shallow waters, possibly coral reefs, which are typical in tropical regions.

The provided ISS coordinates are approximately 18.47024°N latitude and -80.37414°W longitude, which places the ISS above the Caribbean Sea. This region is known for its numerous islands, many of which are characterized by similar features to those visible in the image: lush vegetation, complex coastlines, and surrounding reef systems.

Given the latitude and the appearance of the island, it could potentially be one of the larger islands in the Greater Antilles, such as Cuba, Hispaniola (the island shared by Haiti and the Dominican Republic), Jamaica, or Puerto Rico. However, the size and shape of the island, as well as the specific reef patterns, would need to be compared with maps or satellite imagery to determine the exact island.”

### 4. Input: Picture of Lake Tanganyika in Central Africa
![image1](https://github.com/BU-Spark/ml-terc-image-geolocation/assets/118229570/7306f9b3-cc30-4212-899b-854bc62e8aa3)

**Output**:
“The image shows a vast water body with a highly irregular shoreline and cloud cover interspersed throughout the area. The water appears to have different shades, indicating varying depths or sediment levels. The land areas exhibit a range of colors, suggesting different soil types, vegetation densities, or perhaps even agricultural use.

The provided ISS coordinates are approximately 8.04204°S latitude and 30.28798°E longitude. This places the ISS over the African continent.

Considering the shape of the water body and the location, this image is likely depicting Lake Tanganyika, which is one of the African Great Lakes. Lake Tanganyika is known for its elongated shape, significant depth, and it borders several countries including Tanzania, the Democratic Republic of the Congo (DRC), Burundi, and Zambia.

The lake's distinctive features, such as its length and the surrounding topography, help in its identification. The northern end of the lake, which would be situated toward the upper part of the image, narrows and is bordered by mountainous regions, which is consistent with the geography of the area where the lake's shoreline comes close to the Rwenzori Mountains.

The scale of the image and the ISS's vantage point suggest that a large portion of Lake Tanganyika is visible, potentially spanning hundreds of kilometers from north to south.”


## Evaluation
Overall, TerraByte has performed really well, considering that the base GPT-4 model has been unable to even make a prediction on most images. TerraByte’s strength lies in the fact that it only requires an image upload and a rough ISS location. No extra prompting is required for it to get to work. The following chart depicts the performance of the TerraByte model:

![image2](https://github.com/BU-Spark/ml-terc-image-geolocation/assets/118229570/09325e54-d582-4214-b5fa-ad7c53234129)


We see that almost 90% of images can be approximately geolocated by the TerraByte model. It also correctly names the visible islands, rivers, lakes, and other prominent features visible in the image as well as describing the overall geography of the region. It can correctly identify the scale of the image as well.

## Drawbacks
- **Prominent Geographical Features**: If an image contains a single prominent geographical feature such as a lake or an island, and the region itself has more than one prominent feature of that type, then TerraByte generally resorts to predicting the most prominent of those locations that may result in inaccuracy.
- **Distance from ISS**: If the region depicted in the image is quite far from the ISS location (>1500-2000 miles), then it may struggle to take into account locations so far away, unless the features visible are quite unique.

## Conclusion
TerraByte is a powerful tool for ISS image analysis, offering insights into Earth's geography from an orbital perspective. Whether for educational, research, or curiosity purposes, TerraByte provides a unique way to explore our planet from above. It also provides a detailed description of the image that may be useful for further analysis or research.

This guide is designed to help users understand and utilize TerraByte to its full potential.

## Extension
Since TerraByte can narrow down possible options very well, training it on small detailed maps of the world may significantly enhance its capabilities for identifying locations correctly.


# Future Work and Suggestions:
