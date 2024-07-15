import torch
from utils import tokenize, bag_of_word
from neuralnets import NeuralNet
import json
import random

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

with open("intents.json", "r") as f:
        intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE, map_location=device)

input_size = data['input_size']
hidden_unit = data['hidden_unit']
output_size = data['output_size']
model_state = data['model_state']
all_words = data['all_words']
tags = data['tags']

savemodel = NeuralNet(input_size=input_size,
                          hidden_unit=hidden_unit,
                          output_size=output_size).to(device)
savemodel.load_state_dict(model_state)
savemodel.eval()

bot_name = "Ram"
def response(sentence):
        sentence = tokenize(sentence)
        X = bag_of_word(sentence, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).float().to(device)

        with torch.no_grad():
            y_test = savemodel(X)

        _, predict = torch.max(y_test, dim=1)
        tag = tags[predict.item()]

        probs = torch.softmax(y_test, dim=1)
        prob = probs[0][predict.item()]

        if prob.item() > 0.75:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    break
            else:
                print(f"{bot_name}: Sorry, I don't understand")
        else:
            print(f"{bot_name}: Sorry, I'm not sure about that")