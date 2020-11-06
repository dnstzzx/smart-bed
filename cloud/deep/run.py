from os import path
import torch
import os.path as path
from torchvision import transforms
from .model import device
from torch.nn import functional as F

net = torch.load(path.dirname(path.abspath(__file__ )) + '/model.pth', map_location=torch.device(device))
net.eval()

to_pil_image = transforms.ToPILImage()
to_tensor = transforms.ToTensor()

def one_hot_to_label(one_hot):
    return torch.argmax(one_hot, dim= -1).cpu().item()

def run_one(cv_rgb):
    tensor = to_tensor(cv_rgb).to(device)
    x = tensor.unsqueeze(0) 
    y = net(x)
    y = one_hot_to_label(y)
    return y
