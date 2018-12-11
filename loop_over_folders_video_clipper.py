#pip install moviepy
#pip install ffmpeg
import os
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
rootdir = '/home/cso/Downloads/videos'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		full_path = os.path.join(subdir, file)
		converted_name = os.path.join(subdir, '%s_conv.mp4' % (file.replace('.mp4', '')))
		x264_name = os.path.join(subdir, '%s_x264.mp4' % (file.replace('.mp4', '')))
		if full_path.endswith('.mp4'):
			ffmpeg_extract_subclip(full_path, 0, 5, targetname=converted_name)
			cmds = ['ffmpeg', '-i', converted_name, '-c:a', 'copy', '-c:v', 'libx264', x264_name]
			subprocess.Popen(cmds)
