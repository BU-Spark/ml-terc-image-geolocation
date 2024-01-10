# Use an official Python runtime as a base image
FROM registry.access.redhat.com/ubi9/python-311:latest

USER root
RUN yum -y update && yum -y install libglvnd-glx

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the local directory to the working directory
COPY . .


RUN pip install --upgrade pip

RUN pip install jupyter

# # Change working directory to /root temporarily to generate Jupyter config
# WORKDIR /root

# # Configure Jupyter Notebook to run without a password or token
# RUN jupyter notebook --generate-config --allow-root \
#     && echo "c.NotebookApp.token = ''" >> /root/.jupyter/jupyter_notebook_config.py \
#     && echo "c.NotebookApp.password = ''" >> /root/.jupyter/jupyter_notebook_config.py


# Install dependencies specified in requirements.txt
RUN pip install -r requirements.txt



# Command to run the Jupyter notebook
CMD ["jupyter", "notebook", "--ip='*'", "--port=8080", "--no-browser", "--allow-root"] #port where the container will listen to
