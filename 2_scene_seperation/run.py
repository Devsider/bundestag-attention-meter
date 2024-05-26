from scenedetect import detect, AdaptiveDetector, split_video_ffmpeg

video = '../videos/7611359_h264_1920_1080_5000kb_baseline_de_5000.mp4'

scene_list = detect(video, AdaptiveDetector())

print(scene_list)
split_video_ffmpeg(video, scene_list, show_output=True, output_dir='output', video_name='output')