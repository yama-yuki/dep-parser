### code from https://github.com/shanshantu/Dependence-Parsing/
### modified by yuki-yama

import sys

import torch
from torchsummary import summary

from parser_model import ParserModel
from utils.parser_utils import load_and_preprocess_data

if __name__ == "__main__":
    print("Start Parsing")
    #assert(torch.__version__ == "1.0.0"),  "Please install torch version 1.0.0"

    parser, embeddings, test_data, input_data, model_name = load_and_preprocess_data(mode='Parse')

    model = ParserModel(embeddings)
    parser.model = model
    #summary(model, (1, 28, 28))
    
    output_dir = "results/{0}/".format(model_name)
    output_path = output_dir + "model.weights"
    print('model name: '+str(output_path))

    parser.model.load_state_dict(torch.load(output_path))
    parser.model.eval()

    #print(test_data[:1])
    print(input_data)

    #sys.exit()

    dependencies = parser.parse(input_data, eval=False)
    print(dependencies)
    print("Done!")