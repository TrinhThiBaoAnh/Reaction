
FROM pytorch/pytorch:1.13.0-cuda11.6-cudnn8-devel
RUN pip3 install einops
RUN pip3 install gdown
RUN pip3 install matplotlib
RUN pip3 install imgaug
RUN pip3 install PyYAML
RUN git clone -b ocr https://github.com/TrinhThiBaoAnh/Reaction.git
WORKDIR /Reaction
RUN pip install -r requirements.txt

####  Adding OCR models ####
RUN mkdir -p /Reaction/vietocr/weights
ADD https://drive.google.com/uc?id=1nTKlEog9YFK74kPyX0qLwCWi60_YHHk4 /Reaction/vietocr/weights
ADD https://drive.google.com/uc?id=13327Y1tz1ohsm5YZMyXVMPIOjoOA0OaA /Reaction/vietocr/weights

