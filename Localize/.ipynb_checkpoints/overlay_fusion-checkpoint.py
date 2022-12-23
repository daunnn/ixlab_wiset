# -*- coding: utf-8 -*-
# 알파 블렌딩 (blending_alpha.py)

import os
import cv2
import numpy as np
import natsort
import argparse
from tqdm import tqdm

alpha = 0.5 # 합성에 사용할 알파 값


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_name', type=str, help='name of data')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    frame_dir = '/sssl/_Input/'+args.video_name+'/frame_image/'
    overlay_dir = '/sssl/_Output_SSSL/_Output/fixations/' + args.video_name 

    
    output_dir = '/sssl/_Output_SSSL/_Map/' + args.video_name
    
    
    overlay_list = natsort.natsorted(os.listdir(frame_dir))    
    if '.ipynb_checkpoints' in overlay_list :
        img_list.remove('.ipynb_checkpoints')
        
    #---① 합성에 사용할 영상 읽기
    
    for num in tqdm(range(len(overlay_list)), desc="Mapping"):

        img1 = cv2.imread(frame_dir + '{0:04d}.jpg'.format(num+1))
        img2 = cv2.imread(overlay_dir + '/salmap_f_{}.png'.format(num))
        
        #img2 = cv2.resize(img2, (4096, 2048))
        img1 = cv2.resize(img1, (1080, 606))
        
        # ---② NumPy 배열에 수식을 직접 연산해서 알파 블렌딩 적용

        blended = img1 * alpha + img2 * (1-alpha)
        blended = blended.astype(np.uint8) # 소수점 발생을 제거하기 위함
        #cv2.imshow('img1 * alpha + img2 * (1-alpha)', blended)

        # ---③ addWeighted() 함수로 알파 블렌딩 적용
        # dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0) 
        # cv2.imshow('cv2.addWeighted', dst)

        respath = output_dir
        if not os.path.exists(respath):
            os.mkdir(respath)

        cv2.imwrite(respath + '/{}.jpg'.format(num), blended)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
