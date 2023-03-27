import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data

import torchvision.transforms as transforms
import torchvision.datasets as datasets

import copy
import random
import time
import rospkg

class MLP(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()

        self.input_fc = nn.Linear(input_dim, 250)
        self.hidden_fc = nn.Linear(250, 100)
        self.output_fc = nn.Linear(100, output_dim)

    def forward(self, x):

        # x = [batch size, height, width]

        batch_size = x.shape[0]

        x = x.view(batch_size, -1)

        # x = [batch size, height * width]

        h_1 = F.relu(self.input_fc(x))

        # h_1 = [batch size, 250]

        h_2 = F.relu(self.hidden_fc(h_1))

        # h_2 = [batch size, 100]

        y_pred = self.output_fc(h_2)

        # y_pred = [batch size, output dim]

        return y_pred, h_2


class Net(nn.Module):
    #This defines the structure of the NN.
    def __init__(self):
        super(Net, self).__init__()
        # input is 28x28
        # padding=2 for same padding
        self.conv1 = nn.Conv2d(1, 32, 5, padding=2)
        # feature map size is 14*14 by pooling
        # padding=2 for same padding
        self.conv2 = nn.Conv2d(32, 64, 5, padding=2)
        # feature map size is 7*7 by pooling
        self.fc1 = nn.Linear(64*7*7, 1024)
        self.fc2 = nn.Linear(1024, 10)
        
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, 64*7*7)   # reshape Variable
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x), "hehe"
    

def predict(model, image, device):
    model.eval()

    with torch.no_grad():
        # 480*640
        y_pred, _ = model(image)
        # print(y_pred)
        top_pred = y_pred.argmax(1, keepdim=True)

    return int(top_pred)


def run(image):
    # INPUT_DIM = 480 * 640
    INPUT_DIM = 28 * 28
    OUTPUT_DIM = 10

    # model = MLP(INPUT_DIM, OUTPUT_DIM)
    model = Net()
    optimizer = optim.Adam(model.parameters())
    criterion = nn.CrossEntropyLoss()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    criterion = criterion.to(device)
    
    rospack = rospkg.RosPack()
    path = rospack.get_path("duckiebot_detection") 
    model_path = str(path)+"/src/cropped_cnn_model2.pt"

    model.load_state_dict(torch.load(model_path, map_location=device))
    

    test_transforms = transforms.Compose([
                            transforms.Grayscale(1),
                            transforms.Resize((28,28)),
                            transforms.ToTensor(),
                                        ])
  
    image = transforms.ToPILImage()(image)
    image = test_transforms(image)
        
    digit = predict(model, image, device)
    print(f'Predicted digit: {digit}')
    return digit

    