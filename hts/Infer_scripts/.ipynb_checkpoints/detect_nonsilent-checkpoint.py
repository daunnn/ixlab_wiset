import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import csv
import argparse
import os 
from pydub import AudioSegment, silence

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_name', type=str, help='video_name')
    parser.add_argument('--place', type=str, help='recorded place (in/out)')
    return parser.parse_args()


def pydub_seg(file_name, video_name, place):

    with open("/wiset/hts/Result/"+video_name+".csv") as f:
        reader = csv.reader(f)
        data = list(reader)
   
    wf = open("/wiset/hts/Result/Final_"+video_name+".csv",'a', newline='')
    wr = csv.writer(wf)
    
    
    myaudio = AudioSegment.from_wav("/wiset/hts/Data/"+file_name)

    if place == "in":
        nonsilence = silence.detect_nonsilent(myaudio, min_silence_len=450, silence_thresh=-40)
    else : 
        nonsilence = silence.detect_nonsilent(myaudio, min_silence_len=450, silence_thresh=-32) #out_test2
        #nonsilence = silence.detect_nonsilent(myaudio, min_silence_len=450, silence_thresh=-27) #out_tests1
        
    for start, stop in nonsilence:
        file_start_time = int(file_name[-8:-4])
        
        start_time = start/1000 + file_start_time
        end_time = stop/1000 + file_start_time
        
        for d in data:
            if file_name == d[0] : cls_label = d[1]
        
        wr.writerow([start_time, end_time, cls_label])


if __name__ == "__main__":     
    args = parse_args()
    
    for file in sorted(os.listdir("/wiset/hts/Data/")):
        if file[0] == "e": continue
        pydub_seg(file, args.video_name, args.place)

