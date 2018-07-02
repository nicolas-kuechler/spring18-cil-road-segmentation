import os
from PIL import Image
import argparse
import numpy as np
from core.submission import Submission
from postprocessing.average_config import Config

# parse argument
parser = argparse.ArgumentParser(description='Options for Postprocessing')
parser.add_argument('model_name1', metavar='Model Name', type=str,
                    help='Name of first model')
parser.add_argument('model_name2', metavar='Model Name', type=str,
                    help='Name of second model')

args = parser.parse_args()
m1 = args.model_name1
m2 = args.model_name2

base_dir = './../output/'
dir_name1 = base_dir + m1 + '/test_output/predictions'
dir_name2 = base_dir + m2 + '/test_output/predictions'

dir1 = os.listdir(dir_name1)
dir2 = os.listdir(dir_name2)

# set up submission and config
config = Config( m1 + '--' + m2 + '--avg' )
submission = Submission( config )

# average
for im1, im2 in zip(dir1, dir2):
    im1_id = im1.split('_')[1].split('.')[0]
    im2_id = im2.split('_')[1].split('.')[0]

    im1 = Image.open(dir_name1 + '/' + im1)
    im2 = Image.open(dir_name2 + '/' + im2)

    im1 = np.array(im1)/255
    im2 = np.array(im2)/255
    
    avg_prediction = ( im1 + im2 ) / 2
    submission.add(prediction=avg_prediction, img_id=int(im1_id))

submission.write()