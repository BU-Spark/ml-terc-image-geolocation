# Instructions

## Build
- using the following command to build `docker build -t windows-on-earth .`

## General instructions
- Creat and Run the docker container using the following command `docker run -p 8080:8080 windows-on-earth`
- open the link to the browser once the container is running or paste `http://localhost:8080/tree` in the browser
- if you had previously created the container do `docker start <replace by container id>` and open `http://localhost:8080/tree`

## How to run Pipeline-1-(NN)
- upload you query image in the [query_images](./query_images/) folder
- run the notebook [Poc_pipeline_NN.ipynb](./pipeline-1-(NN)/Poc_pipeline_NN.ipynb)
- enter the query image file name when prompted
- enter the mapbox access token when prompted

## How to run Pipeline-2-(SIFT)
- upload you query image in the [query_images](./query_images/) folder
- add the name of the query image in `Image` column of [results_SIFT_v2_csv.csv](./pipeline-2-(SIFT)/results_SIFT_v2_csv.csv)
- run the notebook [sliding_window_matcher_final_v3.ipynb](./pipeline-2-(SIFT)/sliding_window_matcher_final_v3.ipynb)
- enter the Google Maps API token when prompted
- view the identified location in [results_SIFT_v2_csv.csv](./pipeline-2-(SIFT)/results_SIFT_v2_csv.csv)