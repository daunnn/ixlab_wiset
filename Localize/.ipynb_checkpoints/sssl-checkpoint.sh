# -*- coding: utf-8 -*-
for video in "118_1m_talk_and_shout" # "601_yk_scream_move"
do
    mkdir /wiset/Output/SSSL/${video}
    mkdir /wiset/Output/SSSL/${video}/fixations 
        
    ffmpeg -i /wiset/Input/${video}/${video}.360  -map 0:6 /wiset/Input/${video}/${video}.wav
        
    octave -W /wiset/Localize/SSSL/mcsr/Main.m ${video}  #-> /Output/SSSL/video_name 안에 saliency.mat
    python /wiset/Localize/SSSL/scripts/main.py --video_name ${video}    #-> /Output/SSSL/video_name 안에 pred.csv

    python /wiset/Localize/SSSL/scripts/fixmap2salmap.py --video_name ${video}   #-> /Output/SSSL/video_name/fixations에 SSSL Map 저장
    #csv 파일로 수정
    python /wiset/Localize/clsf.py --video_name ${video}

    # ******************************************
    mkdir /wiset/Output/ViNet/${video}    
    
    python /wiset/Localize/ViNet/scripts/generate_result.py --video_name ${video} #/Output/ViNet/video_name 안에 ViNet Map 저장

    mkdir /wiset/Output/Fusion/${video}
    python /wiset/Localize/fusion.py --video_name ${video}   #-> /Output/Fusion/video_name에 fusion된 이미지 저장

    mkdir /wiset/Output/Final_Result/${video}
    mkdir /wiset/Output/Final_Result/${video}/Overlay
    
    #Overlay
    python /wiset/Localize/overlay.py --video_name ${video} #-> /Output/Final_Result/video_name/Overlay에 overlay 이미지 저장
    
    #frame image to video
    ffmpeg -f image2 -r 30 -i /wiset/Output/Final_Result/${video}/Overlay/%d.jpg -vcodec mpeg4 ./tmp.mp4

    # add audio
    ffmpeg -i /wiset/Input/${video}/${video}.mp4 -vn ./tmp.m4a
    
    #FINAL RESULT
    ffmpeg -i ./tmp.mp4 -i ./tmp.m4a -c copy /wiset/Output/Final_Result/${video}/${video}.mp4 #-> /Output/Final_Result/video_name에 저장   
        
    rm ./tmp.mp4 ./tmp.m4a

done
