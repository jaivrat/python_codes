import torch
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
import PIL
from PIL import Image
from torchvision.transforms.transforms import Grayscale, Resize

import io


# 1. load model
# 2. image -> tensor
# 3. predict


#--------------------- 1. load model : Start --------------------------- 
# We copy same model from tut13
# Fully connected neural network with one hidden layer
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.input_size = input_size
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size, num_classes)  
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        # no activation and no softmax at the end
        return out

# Hyper-parameters 
input_size = 784 # 28x28
hidden_size = 500 
num_classes = 10
model = NeuralNet(input_size, hidden_size, num_classes)

# then we load state dict to this model
PATH = "../mnist_ffn.pth"
model.load_state_dict(torch.load(PATH))
model.eval()
#--------------------- 1. load model : End --------------------------- 




#--------------------- 2. image -> tensor : Start ---------------------------
def transform_image(image_bytes):
    # we copied from the same file where we produced the file mnist_ffn.pth
    # Note we add first two as our mnist images are in grayscale and 28x28
    transform = transform = transforms.Compose([
                                transforms.Grayscale(num_output_channels=1),
                                transforms.Resize((28,28)),
                                transforms.ToTensor(), 
                                transforms.Normalize((0.1307,),(0.3081,))])
    image = Image.open(io.BytesIO(image_bytes))
    return transform(image).unsqueeze(0)

#--------------------- 2. image -> tensor : End   --------------------------- 



#--------------------- 3. predict : Start ---------------------------
def get_prediction(image_tensor):
    images = image_tensor.reshape(-1, 28*28)
    outputs = model(images)
    # max returns (value ,index)
    _, predicted = torch.max(outputs.data, 1)
    return predicted
#--------------------- 3. predict : End   ---------------------------