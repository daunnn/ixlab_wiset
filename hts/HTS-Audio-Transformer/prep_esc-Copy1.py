# -*- coding: utf-8 -*-
import os 
import random
import numpy as np
import librosa
from natsort import natsorted
from tqdm import tqdm
# dataset_path = "./dataset/"
#meta_path = os.path.join(dataset_path, "meta", "esc50.csv")
#audio_path = os.path.join(dataset_path, "audio")

# 데이터 경로 정해주고 & fold 원하는 만큼 결정 

dataset_path = "/wiset/hts/HTS-Audio-Transformer/test_0_loso/"


import os


audio_list = os.listdir(dataset_path)
fold = 1

# for i in range(len(audio_list)):
#     filenames = os.listdir(dataset_path+audio_list[i]) 


#     for name in filenames:
#         src = os.path.join(dataset_path,audio_list[i],name)
# #         print("src",src)

#         dst=str(fold)+'_'+name
# #         print("dst1",dst)
#         dst = os.path.join(dataset_path,audio_list[i], dst)
# #         print("dst2",dst)
# #         print("---------------------") 
#         if fold < 6:             ###############################원하는 fold만큼 숫자 지정 
#             fold+=1
#             print(fold)
#         else:
#             fold = 1
#         os.rename(src,dst)


resample_path = "./audio_32k/" #저장


audio_list = os.listdir(dataset_path)
audio_list=natsorted(audio_list)
print(audio_list)

# prepare for the folder
# meta = np.loadtxt(meta_path , delimiter=',', dtype='str', skiprows=1)
# # resample
# for f in audio_list:
#     full_f = os.path.join(audio_path, f)
#     resample_f = os.path.join(resample_path, f)
#     print('sox ' + full_f + ' -r 32000 ' + resample_f)
#     os.system('sox ' + full_f + ' -r 32000 ' + resample_f)

# name fold target category esc10 srcfile take

output_dict = [[] for _ in range(7)]
for i in tqdm(range(len(audio_list))):
    filename = os.listdir(dataset_path+audio_list[i])  

    for j in range(len(filename)):
#         print(filename[j].split('_'))
#         fold = i % 5 + 1
        fold=filename[j].split('_')[0]
#         print(fold)
        y, sr = librosa.load(os.path.join(dataset_path,audio_list[i], filename[j]), sr = None)
        
        output_dict[int(fold) - 1].append(
            {
                "name": audio_list[i],
                "target":audio_list[i][0] ,
                "waveform": y
            }
        )
print(output_dict)

np.save(os.path.join(dataset_path,"esc-50-data.npy"), output_dict)

