# Reactionary Models


| Backbone| Link |
|--------------|-------|
| vgg_seq2seq | https://drive.google.com/file/d/1-2ukNhfd_Wpg6qpmlFzKy6eXq1bqQgGz/view?usp=sharing|
| vgg_transformer |  https://drive.google.com/file/d/1-O7FnkW10WbHmXl51y2p-C9Q0b_kJ9Jw/view?usp=sharing|

# Capcha Models


| Backbone| Link |
|--------------|-------|
| vgg_seq2seq | https://drive.google.com/file/d/1tTVpjYEb46ZkxrX_JztmSQbXEzKim4HO/view?usp=sharing|
| vgg_transformer |  https://drive.google.com/file/d/1KFBlcJxZQ2u8uULyPIFRo-Y9-9CPPVqI/view?usp=sharing|

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
