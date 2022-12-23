for video in 'in_test1'
do
    mkdir /wiset/hts/Data/
    mkdir /wiset/hts/Result/
    
    #1 sec Segments
    ffmpeg -i /wiset/Input/${video}/${video}.360  -map 0:6 /wiset/Input/${video}/${video}.wav
    ffmpeg -i /wiset/Input/${video}/${video}.wav -f segment -segment_time 1 -c copy /wiset/hts/Data/${video}_%04d.wav
    
    #ESC-50 format
    python ./esc50.py --video_name ${video}
    
    #config.py에 eval_dataset_path 확인 !
    python ../HTS-Audio-Transformer/main.py test
    
    #nonsilent detection
    python ./detect_nonsilent.py --video_name ${video}
    
    
    rm -rf /wiset/hts/Data/

done
    