import os 

import numpy as np
from PIL import Image, ImageEnhance



dst_size = 192
# 分集
import shutil
root = 'pre'
for label in os.listdir(root):
    imgs = os.listdir(root +  '/' + label)
    os.makedirs(root + '/' + label+ '/' + 'train')
    os.makedirs(root + '/' + label + '/' + 'test')
    # 系统抽样
    for i in range(len(imgs)):
        split = 'test' if i % 4 == 0 else 'train'
        shutil.move(root + '/' + label + '/' + imgs[i], root + '/' + label + '/' + split + '/' + imgs[i])

# 缩放
root = 'pre'
dst_root = 'sized'
splites = ['train', 'test']

for label in os.listdir(root):
    for split in splites:
        dir = root + '/' + label + '/' + split
        dst_dir = dst_root + '/' + label + '/' + split
        os.makedirs(dst_dir)
        imgs = os.listdir(dir)
        for img in imgs: 
            rgb = Image.open(dir + '/' + img)
            rgb = rgb.resize((dst_size, dst_size))
            rgb.save(dst_dir + '/' + img)


# 数据增强
from torchvision import transforms as tfs
root = 'sized'
dst_root = 'data'
splites = ['train', 'test']

str_rate = 9    # 训练集1个原始样本9个增强增强样本
def img_strengthen(img):
    img = tfs.RandomOrder([
        tfs.RandomHorizontalFlip(),
        tfs.RandomCrop(192),
        tfs.RandomRotation(10),
        tfs.ColorJitter(brightness=0.5, contrast=0.5, hue=0.5)
    ])(img)
    return img

                    
for label in os.listdir(root):
    for split in splites:
        dir = root + '/' + label + '/' + split
        dst_dir = dst_root + '/' + label + '/' + split
        os.makedirs(dst_dir)
        imgs = os.listdir(dir)
        for img in imgs: 
            rgb = Image.open(dir + '/' + img)
            rgb.save(dst_dir + '/' + img)
            print(dir + '/' + img)
            if split == 'train':
                for i in range(str_rate):
                    name = img.split('.')[0] + f'str_{i}_' + '.jpg'
                    nimg = img_strengthen(rgb)
                    nimg.save(dst_dir + '/' + name)
            