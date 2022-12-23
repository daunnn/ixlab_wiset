# -*- coding: utf-8 -*-
# Ke Chen
# knutchen@ucsd.edu
# HTS-AT: A HIERARCHICAL TOKEN-SEMANTIC AUDIO TRANSFORMER FOR SOUND CLASSIFICATION AND DETECTION
# The configuration for training the model

#####################################################################################################################################
# 이 부분 전체적으로 수정하고 train/test #

#1.ckpt 빼고 checkpoint 폴더명 
exp_name = "/wiset/hts/HTS-Audio-Transformer/cfg/wiset_train/balanced_audio_5_fold_aug" # the saved ckpt prefix name of the model 

workspace = "/wiset/hts/HTS-Audio-Transformer" # the folder of your code

dataset_path = "/wiset/hts/HTS-Audio-Transformer/final_dataset/balanced_wiset_dataset/" # the dataset path
eval_dataset_path = "/wiset/hts/HTS-Audio-Transformer/final_dataset/balanced_speaker_eval/"

#confusion 용
cm_path="/wiset_train/4/"

dataset_type = "esc-50" # "audioset" "esc-50" "scv2"
esc_fold = 0

# trained from a checkpoint, or evaluate a single model 
resume_checkpoint = "/wiset/hts/HTS-Audio-Transformer/cfg/wiset_train/balanced_audio_speaker_final/l-epoch=62-acc=0.959.ckpt"

classes_num = 7 # esc: 50 | audioset: 527 | scv2: 35

fl_dataset = "/wiset/hts/HTS-Audio-Transformer/final_dataset/balanced_speaker_eval/esc-50-data.npy"  
fl_class_num = [
    "0","1","2","3","4","5","6"
]


#######################################################################################################################################

 # just for esc dataset, select the fold you need for evaluation and (+1) validation

random_seed = 1009 #970131 # 19970318 970131 12412 127777 1009 34047
batch_size = 32  # batch size per GPU x GPU number , default is 32 x 4 = 128  #여기 중요 !!! 잘 맞춰서 넣어줘야함 !! 
learning_rate = 1e-3 # 1e-4 also workable 
max_epoch = 50
num_workers = 1
lr_scheduler_epoch = [10,20,30]
lr_rate = [0.02, 0.05, 0.1]




desed_folder = "/wiset/hts/DESED" # the desed file
index_type = "full_train" # only works for audioset
# balanced_data = True # only works for audioset

loss_type = "clip_ce" # 
# AudioSet & SCV2: "clip_bce" |  ESC-50: "clip_ce" 
debug = False


# these data preparation optimizations do not bring many improvements, so deprecated
enable_token_label = False # token label
class_map_path = "class_hier_map.npy"
class_filter = None 
retrieval_index = [15382, 9202, 130, 17618, 17157, 17516, 16356, 6165, 13992, 9238, 5550, 5733, 1914, 1600, 3450, 13735, 11108, 3762, 
    9840, 11318, 8131, 4429, 16748, 4992, 16783, 12691, 4945, 8779, 2805, 9418, 2797, 14357, 5603, 212, 3852, 12666, 1338, 10269, 2388, 8260, 4293, 14454, 7677, 11253, 5060, 14938, 8840, 4542, 2627, 16336, 8992, 15496, 11140, 446, 6126, 10691, 8624, 10127, 9068, 16710, 10155, 14358, 7567, 5695, 2354, 8057, 17635, 133, 16183, 14535, 7248, 4560, 14429, 2463, 10773, 113, 2462, 9223, 4929, 14274, 4716, 17307, 4617, 2132, 11083, 1039, 1403, 9621, 13936, 2229, 2875, 17840, 9359, 13311, 9790, 13288, 4750, 17052, 8260, 14900]
token_label_range = [0.2,0.6]
enable_time_shift = False # shift time
enable_label_enhance = False # enhance hierarchical label
enable_repeat_mode = False # repeat the spectrogram / reshape the spectrogram



# for model's design
enable_tscam = True # enbale the token-semantic layer

# for signal processing
sample_rate = 32000 # 16000 for scv2, 32000 for audioset and esc-50
clip_samples = sample_rate  # audio_set 10-sec clip
window_size = 1024
hop_size = 320 # 160 for scv2, 320 for audioset and esc-50
mel_bins = 64
fmin = 50
fmax = 14000
shift_max = int(clip_samples * 0.5)

# for data collection

patch_size = (25, 4) # deprecated
crop_size = None # int(clip_samples * 0.5) deprecated

# for htsat hyperparamater
htsat_window_size = 8
htsat_spec_size =  256
htsat_patch_size = 4 
htsat_stride = (4, 4)
htsat_num_head =[4,8,16,32]
htsat_dim = 96 
htsat_depth = [2,2,6,2]

swin_pretrain_path = None
# "/home/Research/model_backup/pretrain/swin_tiny_c24_patch4_window8_256.pth"

# Some Deprecated Optimization in the model design, check the model code for details
htsat_attn_heatmap = False
htsat_hier_output = False 
htsat_use_max = False


# for ensemble test 

ensemble_checkpoints = []
ensemble_strides = []


# weight average folder
# wa_folder = "/wiset/hts/HTS-Audio-Transformer/cfg/HTSAT_ESC_exp=1_fold=0_acc=0.970/lightning_logs/version_1/"
# # weight average output filename
# wa_model_path = "l-epoch=8-acc=0.984.ckpt"

# esm_model_pathes = [
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_1.ckpt",
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_2.ckpt",
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_3.ckpt",
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_4.ckpt",
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_5.ckpt",
#     "/home/Research/model_backup/AudioSet/HTSAT_AudioSet_Saved_6.ckpt"
# ]

# for framewise localization
heatmap_dir = "/wiset/hts/HTS-Audio-Transformer/Research/heatmap_output"
test_file = "htsat-test-ensemble"
fl_local = False # indicate if we need to use this dataset for the framewise detection


# map 527 classes into 10 classes
# fl_audioset_mapping = [
#     [0,1,2,3,4,5,6,7],
#     [366, 367, 368],
#     [364],
#     [288, 289, 290, 291, 292, 293, 294, 295, 296, 297],
#     [369],
#     [382],
#     [310, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402],
#     [81, 82, 83, 84, 85],
#     [74, 75, 76, 77, 78, 79],
#     [377]
# ]
