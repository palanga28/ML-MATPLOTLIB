import torch
from torch import nn

class MPL(nn.Module):
    def __init__(self, entree=256, sortie=2):
        super().__init__()

        self.couches = nn.Sequential(
            nn.Linear(entree, 512),
            nn.ReLU(),

            nn.Linear(512, 256),
            nn.ReLU(),

            nn.Linear(256, sortie)
        )

    def forward(self, x):
        return self.couches(x)
