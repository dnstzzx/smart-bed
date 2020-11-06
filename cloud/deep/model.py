import torch.nn as nn
import torch
from torch.nn.modules.dropout import Dropout
from torch.nn import functional as F

try:
    from deep import GENet
except ImportError:
    import GENet

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


backbone = GENet.genet_small(pretrained=True).to(device)
#backbone = regnet.RegNetY_400MF().to(device)


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.backbone = backbone
        self.fc = nn.Sequential(
                            nn.Linear(1000 ,256, bias=True),   
                            nn.ReLU(),
                            Dropout(0.4),
                            nn.Linear(256, 4)
                        ).to(device)
    
    def forward(self, x):
        x = self.backbone(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x