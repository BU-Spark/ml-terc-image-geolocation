# Porject Research Document

## Paper-1: [Find My Astronaut Photo](https://openaccess.thecvf.com/content/CVPR2023W/IMW/papers/Stoken_Find_My_Astronaut_Photo_Automated_Localization_and_Georectification_of_Astronaut_CVPRW_2023_paper.pdf)

Objective: Automated Localization and Georectification of Astronaut Photography and find a robust model for image matching.

Paper’s approach:

The authors estimate the visible Earth region from astronaut photo metadata like ISS position, discretize it into grid patches, and extract matching satellite images from a Landsat database to cover each corresponding geographic area in the grid. 

The SE2-LoFTR image matcher, utilizing MAGSAC homography fitting, efficiently identifies geometrically verified inlier matches between the astronaut photo and candidate Landsat images, enabling "early stopping" based on a threshold of 30 inliers for confident localization without exhaustive grid searching.

Georectification is done through homography estimation using the OpenCV implementation to compute the pixel-to-geographic coordinate transform for assigning latitude/longitude coordinates to all photo pixels.

Techniques which can be used for our project:

- We can  generate reference images from the Cesium virtual earth simulator, covering grid patches of the visible earth surface based on the ISS metadata. 
- These Cesium reference images can be matched against the astronaut photos using the SE2-LoFTR detector-free local feature matcher to find visual correspondences. 
- Inlier matches can be geometrically verified using MAGSAC homography fitting and used to determine if a Cesium reference matches the astronaut photo. 
- Once a match is found, indicating the location, tie points between the astronaut photo and the Cesium reference can be extracted using SE2-LoFTR and MAGSAC again. 
- A homography transform estimated on these tie points using OpenCV can then georectify the astronaut photo by assigning geographic coordinates to central pixel of the astronaut photo.

## Paper-2: [Fine-Grained Cross-View Geo-Localization Using a Correlation-Aware Homography Estimator](https://arxiv.org/pdf/2308.16906.pdf)
The paper introduces a novel approach to fine-grained cross-view geolocalization. The method aims to align ground images with corresponding GPS-tagged satellite images using homography estimation. It employs a differentiable spherical transform to align the perspective of the ground image with the satellite map, effectively reducing the problem to an image alignment task. Challenges such as occlusion, small overlapping range, and seasonal variations are addressed with a correlation-aware homography estimator. The proposed method achieves sub-pixel resolution and meter-level GPS accuracy, outperforming state-of-the-art techniques, reducing mean metric localization errors significantly.
Relevance to the Project:
The research paper is highly relevant to the project as it addresses the challenge of geolocating ground images from the International Space Station (ISS). Key points of relevance include:
- Fine-Grained Cross-View Geolocation: The paper deals with the precise localization of ground cameras, which aligns with the project's goal of accurately predicting the location of ISS photos.
- Alignment Using Homography: The paper introduces a method that uses homography estimation for aligning ground and satellite images. This aligns with the project's objective of aligning images to simulate the world, making it easier to compare and match image content.
- Challenges Addressed: The paper addresses challenges like occlusion, small overlapping range, and seasonal variations, which are relevant to the difficulties of matching ISS photos with the virtual earth simulator in the project.
- High Localization Accuracy: The research claims to achieve high localization accuracy, which is a critical requirement for the project's success in geolocating ISS images.
- Speed and Efficiency: The method in the paper operates at a speed of 30 FPS, which can be valuable for the project, especially if it needs to process a large number of images quickly.

Overall, the paper provides insights into techniques and methodologies that can be applied to improve the geolocation of ISS photos and aligns well with the project's objectives.

## Paper-3: [Image-to-GPS Verification Through A Bottom-Up Pattern Matching Network](https://arxiv.org/pdf/1811.07288.pdf)

The paper by Jiaxin Cheng, Yue Wu, Wael Abd-Almageed, and Prem Natarajan from the University of Southern California, presents a solution to the problem of verifying whether a given image was taken at a claimed GPS location. The authors approach this as an image verification problem, where they determine whether a query image matches a reference image retrieved from the claimed GPS location. The main contributions of the paper are as follows:

- Bottom-Up Pattern Matching Network (BUPM): The authors propose a novel custom deep neural network called BUPM to perform image-to-GPS verification. This network efficiently compares a query image with a panorama reference image, avoiding the need for multiple reference images with different angles and focal lengths.
- Crosschecking Query and Panorama Reference Image: The paper suggests directly comparing a single panorama reference image to a query image. This approach simplifies the verification process by eliminating the difficulties caused by unknown shooting angles and focal lengths.
- Dataset Creation: The authors collect and clean a dataset consisting of 30,000 pairs of query and reference images for training and evaluation.
- Performance: Experimental results demonstrate that the BUPM network outperforms existing solutions in both verification and localization tasks, achieving higher AUC and precision-recall scores. The BUPM network is capable of finding matched patches between query and reference images and reduces false alarms.

The relevance of this paper to our project could be significant as the project involves tasks related to image verification, location verification, or spatiotemporal analysis. The proposed BUPM network offers a novel approach to address these challenges, potentially improving accuracy and reducing the computational burden in cases involving image-to-GPS verification. 

Technologies which can be used from paper 2 and 3:
- Transfer Learning
- Bottom-Up Pattern Matching Network (BUPM)
- https://docs.nvidia.com/vpi/algo_template_matching.html

## Paper-4: [Georeferencing Urban Nighttime Lights Imagery Using Street Network Maps](https://www.mdpi.com/2072-4292/14/11/2671)

This paper presents an automatic georeferencing method for high-resolution nighttime light (NTL) imagery acquired by astronauts from the International Space Station (ISS). Since these images are not naturally georeferenced, making them challenging to use in many remote sensing applications, such as change detection or fusion with other datasets, the authors propose an automatic processing chain for their georeferencing.

Objective:
- To georeference high-resolution urban NTL imagery.

Methodology:
1. Reference Image Generation: The proposed algorithm uses vector-based street network maps, such as those available from OpenStreetMap (OSM), to generate simulated reference NTL images. These simulated images act as a baseline for matching with the astronaut-acquired NTL imagery.
2. BRISK Keypoint Extraction: Binary Robust Invariant Scalable Keypoints (BRISK) is used for keypoint extraction, providing a foundation for the image-matching process. The algorithm considers multiple orientations, rotating the images in incremental steps to find the best match.
3. Keypoint Matching and Outlier Removal: Identified keypoints are matched, and outliers are removed to refine the alignment between the images and the reference street maps.
4. Original Imagery Rectification: Using the identified keypoints, the NTL images are rectified onto the coordinate system of the reference NTL images, completing the georeferencing process.

Results and Conclusion:
- The methodology was tested on nine astronaut photographs of urban areas, resulting in georeferencing accuracies between 2.03 px and 6.70 px.
- The authors concluded that the automatic georeferencing of high-resolution urban NTL imagery is feasible, even with limited attitude and orbit determination.
- They suggest that the algorithm could be particularly beneficial for future spaceborne NTL missions, enhancing their performance and applicability for various studies such as urbanization, energy consumption, and environmental impacts.

Relevance:
The proposed automatic processing chain offers a solution to the challenge of georeferencing ISS images by using terrestrial street networks as references.
It simplifies the manual and complex task of identifying tie points, providing a more efficient and automated process for georeferencing ISS imagery, particularly nighttime photos.

This paper directly addresses our problem by providing an innovative and automated way to georeference ISS imagery, specifically focusing on nighttime light imagery in urban areas. By leveraging the information from street network maps and a robust matching algorithm, it offers a practical approach to overcome the challenges posed by the limited geocoding information available in the manually captured astronaut photographs.

## Paper-5: [Large-scale Image Geo-Localization Using Dominant Sets](https://arxiv.org/pdf/1702.01238.pdf)

This paper presents a new approach to geo-localize images using a database of reference images that have known GPS coordinates. This technique could be useful for our problem of geo-referencing ISS photos, albeit with necessary adaptations considering the distinct environments (urban terrestrial scenes vs. space imagery). Here’s a breakdown of the methodology and its relevance:

 1. Feature Matching and Clustering
     - The algorithm starts by extracting local features from the query image.
     - Each feature is matched with multiple nearest neighbors (NN) from the reference images.
     - These matched features are then clustered using a method called Dominant Set Clustering (DSC).
  
2. Dominant Set Clustering (DSC)
     - DSC is used to form clusters that are coherent and compact, giving more reliable matching.
    - This method allows flexibility in handling outliers and variabilities in the number of nearest neighbors.
   
 3. Two-step Approach
    - Initially, local features are used to get a rough matching with reference images.
    - In the second step, global features and constraints are used to refine these matches, providing a more accurate geo-localization.

 4. Efficiency and Robustness
    - The approach is computationally efficient and robust, enabling it to handle a large-scale image database effectively.

 Relevance to ISS Photo Geo-referencing:

- Feature Extraction: We can apply similar feature extraction techniques to identify distinctive characteristics within the ISS images.
  
- Adaptation to Space Imagery: Adaptation will be necessary as the paper focuses on city-wide images. ISS images might have different types of features and patterns, like cloud formations, landforms, and water bodies, that require different handling.
  
- Large-Scale Handling: Since ISS images could be numerous, the efficiency and scalability of the approach in the paper could be beneficial.
  
- Clustering for Robustness: The two-level clustering approach helps in obtaining a more robust solution, which can be beneficial in handling the complexity and variability in space images.

In conclusion, while the paper's methodology focuses on urban environments, the principles, particularly the feature matching and clustering, can potentially be adapted and applied to geo-reference ISS images by recognizing unique geographic landmarks or patterns seen from space. Note that specific adaptations and considerations will be necessary to handle the distinct features and characteristics of space imagery.


## Relevant projects:
- https://natronics.github.io/ISS-photo-locations/
- https://github.com/natronics/ISS-photo-locations/
- https://github.com/nasa/georef
- https://github.com/nasa/ISS_Camera_Geolocate/tree/master

## Project Implementation trial
- We implemeted a dummy simuliation of the 3d world using Cesium library available with pip. However we feel that its rendering too slow so we would also like to explore more apis/tools.
- We also implemented https://github.com/nasa/ISS_Camera_Geolocate/tree/master, we are still in the process of understanding the code logic and system behind the implementaion and understanding how we can leverage it for our project.