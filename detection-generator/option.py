import argparse


parser = argparse.ArgumentParser(description="basic key initialzations")

parser.add_argument('--approach',type=str,default='Online_request')
parser.add_argument('--input',type=str,default='video')
parser.add_argument('--inputDir',type='str')

args = parser.parse_args()