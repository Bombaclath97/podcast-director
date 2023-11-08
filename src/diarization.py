import moviepy.editor as mp
import os
from dotenv import load_dotenv
from pyannote.audio import Pipeline

load_dotenv()

def extract_audio_from_video(video_path, audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

wide_angle_video_path = os.path.join('input', 'wide_angle.mp4')
wide_angle_audio_path = os.path.join('tmp', 'wide_angle_audio.wav')

extract_audio_from_video(wide_angle_video_path, wide_angle_audio_path)

token=os.getenv("TOKEN")
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.0",
    use_auth_token=token)

diarization_results = pipeline(wide_angle_audio_path)

with open(os.path.join("tmp", "segments.txt"), "+w") as f:
    for segment, _, speaker in diarization_results.itertracks(yield_label=True):
        f.write(f'{speaker} - {segment}\n')