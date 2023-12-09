# Project Description

The Windows on Earth program receives astronaut photos from the International Space Station (ISS). We know the location of the ISS when the photo was taken, but not what the photo is of. This project seeks to use image recognition/machine learning to attempt to geolocate the images automatically. We have a website at [Windows on Earth](https://www.windowsonearth.org/). Our goal is to accurately "predict" the location of the image.

# Instructions to run the Final Pipelines

## Build and run a docker container (only for Pipeline-1 and Pipeline-2)
- use the following command to build `docker build -t windows-on-earth .` the docker container. we need to build the code only once.
- run the docker container using the following command `docker run -p 8080:8080 windows-on-earth`.
    ```
    Note: How to run container without building
    - pull the image from dockerhub using the command `docker pull vedikasrivastavr/woe-6dec`
    - now run the container `docker run -p 8080:8080 vedikasrivastavr/woe-6dec`
    ```
- open the link to the browser once the container is running or paste `http://localhost:8080/tree` in the browser.
- if you had previously created the container do `docker start <replace by container id>` and open `http://localhost:8080/tree`.


## How to run [Pipeline-1-(NN)](./pipeline-1-(NN)/)
### For single images
- upload you query image in the [query_images](./query_images/) folder.
- run the notebook [Poc_pipeline_NN_singleimage.ipynb](./pipeline-1-(NN)/Poc_pipeline_NN_singleimage.ipynb).
- enter the query image file name when prompted.
- enter the mapbox access token when prompted.

### For multiple images 
- upload your images as a folder in [query_images](./query_images/) folder.
- run the notebook [Poc_pipeline_NN_multipleimages.ipynb](./pipeline-1-(NN)/Poc_pipeline_NN_multipleimages.ipynb).
- enter the name of the folder containing your images when prompted.
- enter the mapbox access token when prompted.
- find the predicted location in [NN_multipleimages_results.csv](./pipeline-1-(NN)/NN_multipleimages_results.csv).

## How to run [Pipeline-2-(SIFT)](./pipeline-2-(SIFT)/)
- upload you query image in the [query_images](./query_images/) folder.
- add the name of the query image in `Image` column of [results_SIFT_v2_csv.csv](./pipeline-2-(SIFT)/results_SIFT_v2_csv.csv).
- run the notebook [sliding_window_matcher_final_v3.ipynb](./pipeline-2-(SIFT)/sliding_window_matcher_final_v3.ipynb).
- enter the Google Maps API token when prompted.
- view the identified location in [results_SIFT_v2_csv.csv](./pipeline-2-(SIFT)/results_SIFT_v2_csv.csv) in appropriate columns.


## How to run [Pipeline-3-(TerraByte)](https://chat.openai.com/g/g-cGxe4cVEb-terrabyte)
```
NOTE: requires GPT4 subscription for use
```
- Upload an image of Earth taken from the ISS for analysis.
- If available, include the approximate GPS coordinates of the ISS at the time the image was taken. This helps in narrowing down potential locations.
- Ask TerraByte to geolocate the image. You can include specific questions or details you're interested in, such as identifying particular geographical features or confirming a suspected location.
- TerraByte will extract and identify natural and man-made features visible in the image. It will then try to determine the region of Earth depicted in the image based on the analysis. If the exact location is uncertain, TerraByte will offer a list of likely locations. 
- Feel free to ask follow-up questions or request more details about any part of TerraByte's analysis.

Tips for Best Results
- Image Quality: High-resolution images with distinct geographical markers yield better results.
- ISS Coordinates: Providing accurate ISS coordinates at the time of the image capture significantly enhances location prediction accuracy. However, if the location of the ISS is quite far from the location in the image, it might cause inaccurate identification.


# Find a detailed account of the researh, experimentation and evaluations at [dev/README.md](./dev/README.md)


# [Project Members](./COLLABORATORS)

- Hemant Kumar Singh
- Jaisal Singh
- Vedika Srivastava