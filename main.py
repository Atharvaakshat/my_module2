import moviepy.editor
import shutil 
import sys 

audio_extensions = ['mp3', 'wav', 'aac', 'flac', 'ogg', 'wma', 'm4a', 'aiff', 'opus', 'mid', 'amr', 'au', 'ra', 'ac3', 'ape']

# taking the inputs 
video_input = input("Enter the video: ")
dsr_audio_input = input("Enter the audio extension: ")

if dsr_audio_input not in audio_extensions:
    sys.exit("Sorry We don't use this extension!")
    
video_input_latest = f"{video_input.split('.')[0]}.mp4"

# copying the input
src_path = video_input
destination_path = f"videos/{video_input_latest}"
shutil.copy(src_path, destination_path)

# converting 
video = moviepy.editor.VideoFileClip(destination_path)
audio = video.audio
audio.write_audiofile(f'audios/{video_input.split(".")[0]}.{dsr_audio_input}')