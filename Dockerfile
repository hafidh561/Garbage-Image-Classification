# Install Images
FROM python:3.6.15-slim

# Set working directory
WORKDIR /home/app

# Install packages
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends git && \
	apt-get install libsm6 libxrender-dev -y

# Copy all files into working directory
COPY app.py requirements.txt download_model.py /home/app/

# Download all packages python
RUN git clone https://github.com/nodefluxio/vortex.git && \
	cd vortex/ && git checkout drop-enforce && \
	pip install ./src/runtime[onnxruntime] && cd ../ && \
	pip install -r requirements.txt

# Download model
RUN python download_model.py

# (OPTIONAL) You can use you own port for expose port
EXPOSE 6969

# Run script
CMD ["python", "app.py"]