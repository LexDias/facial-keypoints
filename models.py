## TODO: define the convolutional neural network architecture

import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        # the output Tensor for one image, will have the dimensions: (32, 220, 220)
        self.conv1 = nn.Conv2d(1, 32, 5)        
        
        # maxpool layer
        # pool with kernel_size=2, stride=2
        # after one pool layer, this becomes (32, 110, 110)
        self.pool = nn.MaxPool2d(2, 2)
        
        # second conv layer: 32 inputs, 64 outputs, 3x3 conv
        # the output tensor will have dimensions: (64, 108, 108)
        # after another pool layer this becomes (64, 54, 54);
        self.conv2 = nn.Conv2d(32, 64, 3)
        
        # 64 outputs * the 54*54 filtered/pooled map size
        # 68*2 output channels (x,y for 68 keypoints)
        self.fc1 = nn.Linear(64*54*54, 68*2)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        # conv/relu + pool layer(s)
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        
        # prep for linear layer
        # flatten the inputs into a vector
        x = x.view(x.size(0), -1)
        
        # one linear layer
        x = self.fc1(x)
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x
