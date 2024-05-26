from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg, save_images, open_video

# video = '../videos/7611359_h264_1920_1080_5000kb_baseline_de_5000.mp4'
# video = '../videos/7611359_h264_1920_1080_5000kb_baseline_de_5000_short.mp4'
video = '../videos/7611359_h264_1920_1080_5000kb_baseline_de_5000_shorter.mp4'

scene_list = detect(video, AdaptiveDetector(), show_progress=True)

print(scene_list)
video_stream = open_video(video)
save_images(
    scene_list,
    video_stream,
    num_images=1,
    frame_margin=10,
    output_dir='image_output',
    # image_name_template='image_$SCENE_NUMBER_$IMAGE_NUMBER_$VIDEO_NAME',
    show_progress=True
)

split_video_ffmpeg(
    video, 
    scene_list, 
    show_output=True, 
    output_dir='output', 
    # output_file_template='output_$SCENE_NUMBER_$START_TIME_$END_TIME_$START_FRAME_$END_FRAME_$VIDEO_NAME',
    show_progress=True
)