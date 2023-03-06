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
 ```
 ## Infer
 
 ```
 ```
