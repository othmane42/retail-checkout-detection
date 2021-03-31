

import argparse
import sys
import os


checkpoint_path="./best.pt"

if __name__ == '__main__':
    
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str, default=checkpoint_path, help='model.pt path(s)')
    parser.add_argument('--source', type=str, default="0", help='source')

    opt = parser.parse_args()
    print(opt)
    command = f"python3 ./yolov5/detect.py --source {opt.source} --weights {opt.weights} --conf 0.5"
    try:
        os.system(command)
    except:
        command=command.replace("python3","python",1)
        os.system(command)
