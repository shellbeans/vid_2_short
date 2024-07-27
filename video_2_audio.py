import os
import glob
from moviepy.editor import VideoFileClip

# Directory paths
videos_dir = './videos'
transcriptions_dir = './transcriptions'

# Ensure transcriptions directory exists
os.makedirs(transcriptions_dir, exist_ok=True)

# Get all video files in the videos directory (both .mp4 and .mp4.webm)
video_files = glob.glob(os.path.join(videos_dir, '*.mp4*'))

for video_path in video_files:
    # Get the base filename without extension(s)
    base_filename = os.path.basename(video_path).split('.')[0]
    # Ensure audios directory exists
    audios_dir = './audios'
    os.makedirs(audios_dir, exist_ok=True)
    
    # Extract audio
    audio_path = os.path.join(audios_dir, f"{base_filename}.mp3")
    
    # Check if audio file already exists
    if os.path.exists(audio_path):
        print(f"Audio file for {base_filename} already exists. Skipping conversion.")
        continue
    
    # Convert video to audio
    try:
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(audio_path)
        print(f"Audio extraction for {base_filename} completed and saved.")
    except Exception as e:
        print(f"Error processing {video_path}: {str(e)}")
    finally:
        # Close the video file
        if 'video' in locals():
            video.close()
