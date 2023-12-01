import torch.nn as nn

class HandNetwork(nn.Module):
    def __init__(self, classes):
        super(HandNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(42, 120)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(120, 100)
        self.fc3 = nn.Linear(100, len(classes))
    def forward(self, x):
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x