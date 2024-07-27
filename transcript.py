import os
import whisper
import torch
import json
import librosa
import numpy as np
from tqdm import tqdm

# Check if CUDA is available and set the device accordingly
device = "cuda" if torch.cuda.is_available() else "cpu"
# Check if a local GPU is available
if torch.cuda.is_available():
    print("GPU is available.")
    print(f"GPU device name: {torch.cuda.get_device_name(0)}")
    print(f"Number of GPUs available: {torch.cuda.device_count()}")
else:
    print("No GPU available. Using CPU.")

# Load the Whisper model
model = whisper.load_model("base").to(device)

def extract_audio_features(audio_path):
    y, sr = librosa.load(audio_path)
    
    # Extract features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    mel = librosa.feature.melspectrogram(y=y, sr=sr)
    contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
    
    # Compute statistics
    features = {
        "mfcc_mean": np.mean(mfccs, axis=1).tolist(),
        "mfcc_var": np.var(mfccs, axis=1).tolist(),
        "chroma_mean": np.mean(chroma, axis=1).tolist(),
        "mel_mean": np.mean(mel, axis=1).tolist(),
        "contrast_mean": np.mean(contrast, axis=1).tolist(),
        "tonnetz_mean": np.mean(tonnetz, axis=1).tolist(),
        "zero_crossing_rate": float(librosa.feature.zero_crossing_rate(y).mean()),
        "spectral_centroid": float(librosa.feature.spectral_centroid(y=y, sr=sr).mean()),
        "spectral_rolloff": float(librosa.feature.spectral_rolloff(y=y, sr=sr).mean()),
    }
    
    return features

# Custom callback function to update progress bar
def progress_callback(progress):
    pbar.update(progress - pbar.n)

# Directory containing audio files
audio_dir = './audios'

# Ensure the transcriptions directory exists
transcriptions_dir = './transcriptions'
os.makedirs(transcriptions_dir, exist_ok=True)

# Get list of audio files
audio_files = [f for f in os.listdir(audio_dir) if f.endswith('.mp3')]

# Process all audio files in the ./audios folder
for audio_file in audio_files:
    audio_path = os.path.join(audio_dir, audio_file)
    print(f"\nProcessing {audio_file}...")
    
    # Initialize progress bar for transcription
    pbar = tqdm(total=100, desc="Transcribing", unit="%")
    
    # Transcribe audio with progress callback
    # Use fp16=False for CPU, and fp16=True for GPU to improve performance
    result = model.transcribe(audio_path, verbose=False, fp16=(device == "cuda"))
    
    # Close the progress bar
    pbar.close()
    
    print("Extracting audio features...")
    # Extract audio features
    audio_features = extract_audio_features(audio_path)
    
    # Prepare the data to be saved
    transcript_data = {
        "filename": audio_file,
        "text": result["text"],
        "segments": result["segments"],
        "language": result["language"],
        "audio_features": audio_features
    }
    
    # Initialize progress bar for transcription
    pbar = tqdm(total=100, desc="Extracting Audio Features", unit="%")

    # Save the transcript and features as JSON
    transcript_file = os.path.join(transcriptions_dir, f"{os.path.splitext(audio_file)[0]}.json")
    with open(transcript_file, 'w', encoding='utf-8') as f:
        json.dump(transcript_data, f, ensure_ascii=False, indent=2)
    
    # Close the progress bar
    pbar.close()
    
    print(f"Transcription and features saved to {transcript_file}")

print("All audio files have been transcribed.")