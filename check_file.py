import os

base_dir = "/CoVR/datasets/CIRR/blip2-coco-embs-large/train/"
filename = "train-13013-0-img1.pth"
found = False

for i in range(100):
    dir_path = os.path.join(base_dir, str(i))
    target_path = os.path.join(dir_path, filename)
    print(f"Checking directory {i}: {target_path}")
    if os.path.exists(target_path):
        print(f"Found file: {target_path}")
        found = True
        break

if not found:
    print("File not found in any directory from 0 to 99.")
