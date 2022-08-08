import argparse
#options for the main function

parser = argparse.ArgumentParser(description="basic key initialzations")

parser.add_argument('--approach',type=str,default='Online_request')
parser.add_argument('--input',type=str,default='camera')
parser.add_argument('--inputDir',type=str)
parser.add_argument('--multithread',type=bool,default=True)
parser.add_argument('--show_img',type=bool,default=True)
args = parser.parse_args()