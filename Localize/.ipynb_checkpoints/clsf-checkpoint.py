# -*- coding: utf-8 -*-
from email import header
import os
import sys
import argparse
import csv
import pandas as pd
import numpy as np
import imageio
import cv2



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_name', type=str, help='video path')
    return parser.parse_args()

# def normalize_map(smap):
#     return (smap - smap.min())/(smap.max() - smap.min())

# def fix2sal(fixmap):
#     h = fixmap.shape[0]
#     s = h//2 
#     return (normalize_map(cv2.GaussianBlur(fixmap**2, (s,s), 40))*255).astype(np.uint8) #가우시안 필터링 함수 - cv2.GaussianBlur

def get_odvInfo(vid_pth, odv_name):
        vid = imageio.get_reader(os.path.join(vid_pth, odv_name + '.mp4'), 'ffmpeg')
        return vid.get_meta_data()


def hts_csv(hts_pth, vid_time):

    with open(hts_pth, newline='') as csvfile:
        hts_csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
        classify_res = [line[0].split(',')[:2] for line in hts_csv]
    
    classify_res = list(map(lambda x: list(map(lambda x: round(float(x), 2), x)), classify_res))
    classify_res.sort()

    return classify_res


def run(args):
    hts_pth = os.path.join('/wiset/hts/Result', args.video_name+'.csv')
    vid_pth= os.path.join("/wiset/Input", args.video_name)

    _img = imageio.imread(os.path.join('/wiset/Output/SSSL', args.video_name, 'fixations','salmap_f_' + str(0) + '.png'))
    vid_time = get_odvInfo(vid_pth, args.video_name)

    # hts_csv = pd.read_csv(hts_pth, header=None)
    classify_res = hts_csv(hts_pth, vid_time)

    print(vid_time)
    print(classify_res)    

    # for t in classify_res:
        # img_pth = os.path.join('/wiset/Output/SSSL', args.video_name, 'fixations','salmap_f_' + str(f) + '.png')
        # imageio.imwrite(img_pth, np.zeros((_img.shape[0], _img.shape[1])).astype(np.uint8))



if __name__ == "__main__":
    args = parse_args()
    run(args)
