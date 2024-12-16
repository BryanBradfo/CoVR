import os

for i in range(0, 100):  # De 0 à 99 inclus
    command = f"python tools/embs/save_blip2_embs_imgs.py " \
              f"--image_dir datasets/CIRR/images/train/{i} " \
              f"--save_dir datasets/CIRR/blip2-coco-embs-large/train/{i} " \
              f"--batch_size 2"
    os.system(command)
