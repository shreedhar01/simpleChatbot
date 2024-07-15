import torch.nn as nn 

class NeuralNet(nn.Module):
  def __init__(self, input_size, hidden_unit, output_size):
    super().__init__()
    self.block1 = nn.Sequential(nn.Linear(in_features=input_size, out_features=hidden_unit),
                                nn.ReLU(),
                                nn.Linear(in_features=hidden_unit, out_features=hidden_unit),
                                nn.ReLU()
                                )
    self.last = nn.Linear(in_features=hidden_unit, out_features=output_size)

  def forward(self, x):
    x = self.block1(x)
    return self.last(x)