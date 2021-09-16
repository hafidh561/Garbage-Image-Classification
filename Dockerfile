# Install Images
FROM python:3.6.15-slim

# Set working directory
WORKDIR /home/app

# Install packages
RUN apt-get update -y && apt-get upgrade -y

# Copy all files into working directory
COPY app.py requirements.txt download_models.py /home/app/

# Instal python libraries
RUN pip install -r requirements.txt

# Download models
RUN python download_models.py

# Move Main Model
COPY saved_model.pth /home/app/

# Move Pretrained Model
COPY resnet152-394f9c45.pth /root/.cache/torch/hub/checkpoints/

# Expose Port
EXPOSE 80

# Run script
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]