# Garbage Image Classification

## Description

Garbage image classification using PyTorch transfer learning pretrained model Resnet152 with FastAPI for API based application. This model will classification 6 class: cardboard, glass, metal, paper, plastic, trash (other).

## Installation

```bash
$ git clone https://github.com/hafidh561/Garbage-Image-Classification.git
```

### Installation Python

```bash
# Python version 3.6
$ git clone https://github.com/nodefluxio/vortex.git
$ cd vortex/ && git checkout drop-enforce
$ pip install ./src/runtime[onnxruntime] && cd../
$ pip install -r requirements.txt
$ python download_models.py
```

### Installation Docker

```bash
# Newest docker version
$ docker build -t hafidh561/garbage-image-classification:1.0 .
```

## Usage

### Usage Python

```bash
$ uvicorn app:app --port <YOUR PORT>
# Example
$ uvicorn app:app --port 6969
```

### Usage Docker

```bash
$ docker run --rm -p <YOUR PORT>:<YOUR PORT> hafidh561/garbage-image-classification:1.0
# Example
$ docker run --rm -p 6969:6969 hafidh561/garbage-image-classification:1.0
```

### Usage API

1. After you run app use python or docker, open your web browser and go to path `/docs` for looksing some documentation.
2. Now it's time to testing API, open your application for testing API. I'll use Postman for testing API.
3. Set up postman like this.

    ![postman_body](screenshots/ss1.png)

4. Press button "Select Files" to select image you want to classification.
5. Press "Send" button and waiting for response.
6. Now open response body and look object response member "class" and search for highest value.

#### Example Test API

![metal](./test_model/glass.jpg)

```json
{
	"filename": "glass.jpg",
	"contentype": "image/jpeg",
	"class": "glass",
	"confidence": "0.99995697"
}
```

## License

[MIT LICENSE](./LICENSE)

© Developed by [hafidh561](https://github.com/hafidh561) - Internship at Nodeflux
