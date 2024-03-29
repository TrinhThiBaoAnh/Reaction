<h2> I. Prepared Envs and Data</h2>
<h3> 1. Envs </h3>

```
pip3 install paddlepaddle-gpu==2.4.2.post117 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html
pip3 install einops
pip3 install Levenshtein
pip3 install "paddleocr>=2.0.1"
```
<h3> 2. Data </h3>
  <h4> OCR dataset </h4>https://drive.google.com/drive/folders/17fhbv1tZdJNwwZCBqkBIJYmTsLAXKPDY?usp=sharing
  <h4> Detection dataset </h4>https://drive.google.com/drive/folders/1B7OzKDQD6mv8_A_ueKL3HuVTqYxWEvso?usp=sharing
  
<h3> 3. Pretrained Models </h3>
<h4> 3.1 OCR </h4>
Please put these models in ./vietocr/weights/

| Backbone| Link |
|--------------|-------|
| vgg_seq2seq | https://drive.google.com/file/d/1tTVpjYEb46ZkxrX_JztmSQbXEzKim4HO/view?usp=sharing|
| vgg_transformer |  https://drive.google.com/file/d/1KFBlcJxZQ2u8uULyPIFRo-Y9-9CPPVqI/view?usp=sharing|

<h4> 3.2 DET </h4>
Please put these models in ./pretrain_models/

| Backbone| Link |
|--------------|-------|
| MobileNetV3 | https://paddleocr.bj.bcebos.com/pretrained/MobileNetV3_large_x0_5_pretrained.pdparams|
| ResNet18 | https://paddleocr.bj.bcebos.com/pretrained/ResNet18_vd_pretrained.pdparams |
| ResNet50 |  https://paddleocr.bj.bcebos.com/pretrained/ResNet50_vd_ssld_pretrained.pdparams|

### Text Detection Algorithms

Supported text detection algorithms (More information [Here](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_en/algorithm_overview_en.md)):
- [x]  [DB && DB++]
- [x]  [EAST]
- [x]  [SAST]
- [x]  [PSENet]
- [x]  [FCENet]
- [x]  [DRRG]

Please put these model in ./output to use for inference process

|Model|Backbone|Precision|Recall|Hmean|Download link|
| --- | --- | --- | --- | --- | --- |
|EAST|ResNet50_vd|88.71%|81.36%|84.88%|[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.0/en/det_r50_vd_east_v2.0_train.tar)|
|EAST|MobileNetV3|78.20%|79.10%|78.65%|[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.0/en/det_mv3_east_v2.0_train.tar)|
|DB|ResNet50_vd|86.41%|78.72%|82.38%|[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.0/en/det_r50_vd_db_v2.0_train.tar)|
|DB|MobileNetV3|77.29%|73.08%|75.12%|[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.0/en/det_mv3_db_v2.0_train.tar)|
|SAST|ResNet50_vd|91.39%|83.77%|87.42%|[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.0/en/det_r50_vd_sast_icdar15_v2.0_train.tar)|
|PSE|ResNet50_vd|85.81%|79.53%|82.55%|[trianed model](https://paddleocr.bj.bcebos.com/dygraph_v2.1/en_det/det_r50_vd_pse_v2.0_train.tar)|
|PSE|MobileNetV3|82.20%|70.48%|75.89%|[trianed model](https://paddleocr.bj.bcebos.com/dygraph_v2.1/en_det/det_mv3_pse_v2.0_train.tar)|
|DB++|ResNet50|90.89%|82.66%|86.58%|[pretrained model](https://paddleocr.bj.bcebos.com/dygraph_v2.1/en_det/ResNet50_dcn_asf_synthtext_pretrained.pdparams)/[trained model](https://paddleocr.bj.bcebos.com/dygraph_v2.1/en_det/det_r50_db%2B%2B_icdar15_train.tar)|

<h2> II. Quick started </h2>

<h3>Demo detection </h3>
<p> Please change your image path in demo_detect.py </p>

```
python3 demo_detect.py
```
| Input| Output |
|--------------|-------|
|<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/image/sample_det/333500806_1423207085151590_8835670948295859802_n.jpg?raw=true" width="350"> |<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/inference_results/det_res_333500806_1423207085151590_8835670948295859802_n.jpg" width="350">|

<h3>Demo OCR with vgg_transformer backbone </h3>

```
python3 demo_ocr.py\
        --img ${Path_to_your_image}\
        --config ./config_vgg_transformer.yml \
        --weight ./vietocr/weights/vgg_transformer.pth
``` 

<h3>Demo OCR with vgg_seq2seq backbone </h3>

```
python3 demo_ocr.py\
        --img ${Path_to_your_image}\
        --config ./config_vgg_seq2seq.yml \
        --weight ./vietocr/weights/vgg_seq2seq.pth
``` 

<h3> Demo E2E pineline </h3>

```
python3 end2end.py --det_algorithm=${Your_det_algorithm} \
                    --det_model_dir=${Your_det_model_directory} \
                    --image_dir=${Your_path_to_image_folder} \
                    --use_gpu=True \
                    --config ${Your_path_to_ocr_config_file} \
                    --weight-ocr ${Your_path_to_ocr_model}
```

Example:

```
python3 end2end.py --det_algorithm="DB" \
                    --det_model_dir="./output/en_PP-OCRv3_det_infer/" \
                    --image_dir="./image/sample_det" \
                    --use_gpu=True \
                    --config './config_vgg_transformer.yml' \
                    --weight-ocr './vietocr/weights/vgg_transformer.pth'

```
Result:
 
| Input| Output Detection| OCR | Classification |
|--------------|--------------|--------------|--------------|
|<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/image/image.jpeg" width=250px> |<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/image/res.jpg" width=250px>|TỔ CHỨC KHỦNGBO VIỆT TÂNĐỨACONLAIQUÁITHAI THỜI HẬU CHIẾN | Bình thường|
|<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/image/sample_det/viet-tan.jpg?raw=true" width=250px>|<img src="https://github.com/TrinhThiBaoAnh/Reaction/blob/main/inference_results/det_res_viet-tan.jpg?raw=true" width=250px>|ALLION KICH DONG DONG 310| Phản động|

<h2> III.Training</h2>
<h3> Train detection </h3>

```
!python3 tools/train.py -c configs/det/det_mv3_db.yml -o   \
         Global.pretrained_model=./pretrain_models/MobileNetV3_large_x0_5_pretrained  \
         Optimizer.base_lr=0.0001
```
<h3> Infer detection </h3>

```
!python3 tools/export_model.py -c configs/det/det_mv3_db.yml -o Global.pretrained_model="./output/det_mv3_pse/best_accuracy" Global.save_inference_dir="./output/det_mv3_pse_inference/"
```

```
!python3 tools/infer/predict_det.py --det_algorithm="DB" --det_model_dir="./output/en_PP-OCRv3_det_infer/" --image_dir="./image/sample_det" --use_gpu=True
```

<h3> Train OCR </h3>
<h3>Train OCR with vgg_transformer backbone </h3>

```
!python3 train_ocr.py --config 'vgg_transformer' \
                      --data-root './dataset/ocr/data_line/' \
                      --train 'train_line_annotation.txt' \
                      --test 'train_line_annotation.txt' \
                      --num-epochs 20000 \
                      --batch-size 32 \
                      --max-lr 0.0003 \
                      --export './weights/transformerocr.pth' \
                      --checkpoint './weights/transformerocr.pth'
```

<h3>Train OCR with vgg_seq2seq backbone </h3>

```
!python3 train_ocr.py --config 'vgg_seq2seq' \
                      --data-root './dataset/ocr/data_line/' \
                      --train 'train_line_annotation.txt' \
                      --test 'train_line_annotation.txt' \
                      --num-epochs 20000 \
                      --batch-size 32 \
                      --max-lr 0.001 \
                      --export './weights/seq2seqocr.pth' \
                      --checkpoint './weights/seq2seqocr.pth'
```
 
