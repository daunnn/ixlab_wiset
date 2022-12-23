# -*- coding: utf-8 -*-
import os 
import random
import numpy as np
import librosa
from natsort import natsorted
from tqdm import tqdm
import argparse


def make_esc50(audio_dir):
    fold = 1
    
    audio_files = os.listdir(audio_dir)
    audio_files = natsorted(audio_files)

    output_dict = [[]]
    
    for file in tqdm(audio_files):
        if file[0]=='.': continue

        y, sr = librosa.load(os.path.join(audio_dir, file), sr = None)
        
        output_dict[int(fold)-1].append(
            {
                "name": file,
                "target": 0,
                "waveform": y
            }
        )

    np.save(os.path.join(dataset_path,"esc-50-data.npy"), output_dict)

if __name__ == '__main__':
    dataset_path = "/wiset/hts/Data/"
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_name', type=str, default='')
    
    args = parser.parse_args()   
    
    make_esc50(dataset_path)
    
