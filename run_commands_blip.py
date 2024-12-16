import os

for i in range(0, 100):  # De 0 à 99 inclus
    command = f"python tools/embs/save_blip_embs_imgs.py " \
              f"--image_dir datasets/CIRR/images/train/{i} " \
              f"--save_dir datasets/CIRR/images/blip-embs-large/train/{i} " \
              f"--batch_size 32 --num_workers 4"
    os.system(command)
