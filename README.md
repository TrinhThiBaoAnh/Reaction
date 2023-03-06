## Train 

```
!python3 train_ocr.py --config 'config_vgg_transformer.' \
                      --data-root './dataset/ocr/data_line/' \
                      --train 'train_line_annotation.txt' \
                      --test 'train_line_annotation.txt' \
                      --num-epochs 20000 \
                      --batch-size 32 \
                      --max-lr 0.0003 \
                      --export './weights/transformerocr.pth' \
                      --checkpoint './weights/transformerocr.pth'
 ```
 ## Test
 
 ```
!python3 train_ocr.py --config 'vgg_transformer' \
                      --data-root './dataset/ocr/data_line/' \
                      --test 'train_line_annotation.txt' \
                      --weight './vietocr/weights/transformerocr.pth'
 ```
 ## Infer
 
 ```
 python3 demo_ocr.py\
        --img ${Path_to_your_image}\
        --config ./config_vgg_transformer.yml \
        --weight ./vietocr/weights/vgg_transformer.pth
 ```
