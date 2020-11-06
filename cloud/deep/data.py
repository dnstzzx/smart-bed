from os import terminal_size
import PIL
import numpy as np
from numpy.core.defchararray import index
import torch
from torch import Tensor
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms as tfs
import os
from PIL import Image
from torchvision import transforms
from torchvision.transforms.functional import to_pil_image
import cv2
from model import device

root = 'data'
cache = True
cache_pool = {}


os.listdir()


data_strengthen_rate = 49

img_strengthen =tfs.Compose([
                    tfs.RandomHorizontalFlip(),
                    tfs.RandomCrop(192),
                    tfs.ColorJitter(brightness=0.5, contrast=0.5, hue=0.5)
                ])


class MyDataSet(Dataset):
    def __init__(self, split='train'):
        self.root = root
        self.data = []
        self.split = split
        self.label = []
        self.to_tensor = transforms.ToTensor()
        
        for label in os.listdir(root):
            dir = root + '/' + label + '/' + split
            imgs = os.listdir(dir)
            for img in imgs:
                self.data.append(dir + '/' + img)
                self.label.append(label)
                
    def __len__(self):
        return len(self.data)

    def gen_item(self, index):
        rgb = self.data[index]
        rgb = cv2.imread(rgb)
        rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)
        
        tensor = self.to_tensor(rgb).to(device)
        label = int(self.label[index])
        return tensor, label

    def _get_item(self, index):
        if not cache:
            return self.gen_item(index)
        if index in cache_pool:
            return cache_pool[index]
        item = self.gen_item(index)
        cache_pool[index] = item
        return item

    def __getitem__(self, index):
        return self._get_item(index)

    




if __name__ == '__main__':
    a = MyDataSet('train')
    rgb, (l1, l2, l3) = a[0]
    
    to_pil_image(rgb.to('cpu')).save('data0.jpg')
    print(l1, l2, l3)

