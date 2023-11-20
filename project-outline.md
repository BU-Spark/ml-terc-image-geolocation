# Project Outline

## *Vedika Srivastava, Hemant Singh, Jaisal Singh, 2023-October-06 v0.0.1-dev*

## Overview

The Windows on Earth Image Geolocation project aims to revolutionize the geolocation process of images captured from the International Space Station (ISS). By harnessing the power of image recognition and machine learning in conjunction with a virtual world simulator (Cesium), our mission is to automate the task of determining the precise geographical coordinates of these images.

At its core, this project addresses a critical challenge faced by the Windows on Earth program. While we know the location of the ISS when each photo is taken, we lack information about the specific subject of the image. Typically, the subject lies within a 300-mile radius of the ISS location. Our objective is to predict this subject's location with high accuracy.


### A. Manual Geolocation Process: Challenges and Opportunities for Automation

The existing workflow relies heavily on manual processes. The process can be outlines as follows:

1. Receiving photos from the ISS.
2. Noting down the ISS location from the EXIF data of the photo.
3. Deciding the appropriate search area based on coordinates of the ISS.
4. Categorize the image as a city, desert, mountain, lake, sea, coastal island, etc.
5. Refining the search areas based on the image category.
6. Manually comparing and matching the image's distinct features (like coastlines, lakes, rivers) with Cesium 3D map.
7. Assigning a probable geolocation coordinate to the image.
8. Validate the identified location using Google maps coordinate.

The current manual process is resource-intensive, time-consuming, and prone to human error, limiting the efficiency and scalability of geolocating ISS images. Automating this workflow through AI and machine learning aims to streamline these steps and significantly improve the process's speed and accuracy.


### B. Machine Learning Approach for Automated Geolocation of ISS Images

Given an image captured from the ISS and its associated metadata, the problem statement can be defined as follows:

*The project seeks to construct a multi-faceted machine learning framework to automate the geolocation of images.*

To address this challenge, we propose a technical solution that encompasses of the following major steps:

- Categorizing the image into distinct geophysical classes (e.g., cityscapes, deserts, mountains, lakes, seas, coastal islands) based on the ISS location.
- Narrowing down potential geographical zones.
Correlating and matching discernible terrestrial features of the image with a 3D Earth simulation provided by Cesium.
- Pinpointing a precise geolocation coordinate for the image subject while accounting for variations in external parameters such as lighting, cloud cover, view direction, and atmospheric perspectives.


### C. Checklist for project completion

**Deliverable 1 (PLC Phase 3):**

1. Data Acquisition and Structuring:
    -  Successfully import the images from the ISS and extract relevant EXIF data.
    - Implement data validation checks to ensure the integrity of the imported data.
    - Organize metadata, with a specific focus on extracting and structuring the ISS location for each image.

2. Dataset and Cesium exploration:
    - Implement image pre-processing techniques to enhance the visibility of features and landmarks within the ISS images.
    - Explore techniques like contrast adjustment, noise reduction, and sharpening to improve image quality.
    - Read Cesium documentation, explore the Cesium library in python and experiment with a couple of plots.

**Deliverable 2 (PLC Phase 4):**

3. Cesium Map Interaction:
    - Develop python script to interact with the Cesium virtual world simulator.
    - Generate views from Cesium based on ISS coordinates, taking into account variations in altitudes, angles, and perspectives.
    - Create algorithms to capture views from Cesium as image in relevant format.
    - Ensure to handle different scales, orientations, and lighting conditions present in Cesium views.
    - Implement error handling mechanisms to ensure seamless data retrieval from Cesium.
    - Ensure accurate extraction and storage of these images for further matching.

4. Template Matching Mechanism:
    - Implement a template matching algorithm,initially by deploying available frameworks like OpenCV otherwise by developing our own NeuralNet, considering the unique challenges of aligning ISS images with Cesium views.
    - Incorporate advanced image comparison techniques, such as feature point detection and matching, to improve accuracy.
    - Define and achieve a specified accuracy or confidence threshold (e.g., 50% match confidence) when aligning the ISS image with the Cesium view.

**Deliverable 3 (PLC Phase 5):**

5. Refinement and Localization:
    - Explore algorithms to refine the geolocation based on matched templates, aiming for precision in pinpointing the subject's location.
    - Implement feedback mechanisms to assess the certainty or confidence of each match.
    - Update and improve the refinement process based on performance analysis.

6. Validation and Testing:
    - Cross-reference the identified geolocations with actual known locations or other mapping sources,like google earth or geo-spatial datasets released publicly for that location, to validate the system's predictions.
    - Test the template matching system on these sets of photos to ensure robustness and versatility.
    - Consider diverse sets of images, including those with varying lighting conditions, atmospheric perspectives, and cloud cover.

7. Optimization:
    - Enhance the speed and efficiency, by tuning hyperparameters, of the template matching process, aiming for real-time or near-real-time results if possible.
    - Introduce machine learning techniques, such as deep learning-based feature extraction, that can improve match accuracy

8. Documentation:
    - Prepare comprehensive documentation that provides in-depth insights into the technical aspects of the template matching process.
    - Detail the interactions with Cesium, algorithms utilized, and any machine learning models or AI techniques integrated.
    - Create user guides and manuals tailored for stakeholders or end-users, ensuring clarity in understanding and utilization.

**Deliverable 4 (PLC Phase 6):**

9. Stakeholder Presentation:
    - Showcase the developed system to stakeholders, emphasizing its template matching capabilities, efficiency, and potential applications.
    - Gather feedback for potential refinements or enhancements.

10. Deployment and Handover:
    - Package the system for deployment, ensuring all dependencies, scripts, and interfaces are bundled.
    - Hand over the completed system, documentation, and any related tools to the project stakeholders.

### D. Deployment for Geolocation Tool

The tool produced by this project can be operationalized as a web-based application (e.g., Django, Flask, Plotly) in the Windows on Earth website. Windows on earth admin can upload ISS images regularly and can get the real coordinates of those images. Users browsing the website can check the image and visit the location through Google maps link to explore more.

## Resources

### Data Sets

- [Google Drive](https://drive.google.com/drive/folders/17k9OTFAdbD2-rZO64MyodMbzHfF6fXbx)

### References

- https://www.windowsonearth.org/ 
- https://cesium.com/
- http://www.acgeospatial.co.uk/template-matching-eo/
- https://pythonprogramming.net/template-matching-python-opencv-tutorial/


## Weekly Meeting Updates

[PM Meeting Link](https://bostonu.zoom.us/j/92945921675?pwd=WVgvbHFUWE5oYy9ja1BIVEp6cmJidz09)
- Scheduled Tuesday 10th Oct 11:45am to 12:30pm
- Scheduled on Mondays 11:45am to 12:30pm


Client Meeting Link
- Kick Off -Monday 16th Oct 2023 ([link](https://bostonu.zoom.us/j/93413092114?pwd=b3UzSkVYY3lzaERpWW1LV1NEaDV3Zz09))
- Bi-weekly meeting 30th Oct 2023 ([link](https://bostonu.zoom.us/j/93413092114?pwd=b3UzSkVYY3lzaERpWW1LV1NEaDV3Zz09))


### **PM Meeting Notes - Tuesday - 10th Oct**

- Introductions
- Ensured access to google drive and slack channel
- Shared questions seeking clarifications on some aspects of the project
- Emphasis laid on scheduling client meeting as soon as possible

### **Meeting with Prof. Gardos - Friday - 13th Oct**

- Clarrified project goal, which is getting the location of the image
- Discussed how to proceed

    - go for the exif -> extract metadata -> take longitude, latitude and altitude -> do lens optics -> get the Field of View
    - study ISS statelite positing and image capture
    - also try cesium statelite tracker

### **PM Meeting Notes - Monday - 16th Oct**
- Discussed what exactly was to be dicussed in the client meeting

### **Client Kick-Off Meeting Notes - Monday - 16th Oct**
- Introductions
- Client gave a brief description of the problem and the bigger picture
- Cleared some questions
- Agreed on date and time for next meeting

### **PM Meeting Notes - Monday - 23rd Oct**
- Gave progress update
- Assigned tasks for the week

### **PM Meeting Notes - Monday - 30th Oct**
- Meeting cancelled

### **Client Meeting Notes - Monday - 30th Oct**
- Meeting cancelled

### **PM Meeting Notes - Monday - 6th Nov**
- Short Meeting dicussed what to present in client meeting

### **Client Meeting Notes - Monday - 6th Nov**
- Presented EDA in client meeting

### **PM Meeting Notes - Monday - 12th Nov**
- Discussed what to present in client meeting

### **Client Meeting Notes - Monday - 12th Nov**
- Presented Poc in client meeting
- Discussed some problems related to cloud cover and general client expectation
- Found suitable date to reshedule the next client meeting

### **Meeting with Prof. Gardos - Friday - 17th Nov**
- Discussed about the shortcomes of current pipelines - SIFT and Corelate2D
- Demostarted the Chatgpt-4 pipeline
- Discussed what should be submitted as deliverables on Gradescope.

### **PM Meeting Notes - Monday - 20th Nov**
- Gave an update on what we are working on and how are we going to progress
- Planned out the schedule for future meetings.

### **PM Meeting Notes - Monday - 4th Dec**
- 

### **Client Meeting Notes - Wednesday - 6th Dec**
-