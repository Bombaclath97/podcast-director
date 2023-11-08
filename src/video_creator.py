from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
import time

default_video = VideoFileClip(os.path.join("input", "wide_angle.mp4"))
host_angle = VideoFileClip(os.path.join("input", "host_angle.mp4"))
guest_angle = VideoFileClip(os.path.join("input", "guest_angle.mp4"))

# Read video information from the input text file
video_segments = []
with open(os.path.join("tmp", "segments.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split(" - ")

        # Define the video for the speaker
        speaker = parts[0]
        
        # Define the segment
        time_range = parts[1].strip("[]").split(" --> ")
        start_time = time_range[0].strip()
        end_time = time_range[1].strip()

        video_segments.append((speaker, start_time, end_time))

video_segments.sort(key=lambda x: x[1])

subclips = []

current_end_time = "00:00:00.000"
full_duration = time.strftime("%H:%M:%S", time.gmtime(default_video.duration)) + ".000"
for speaker, start_time, end_time in video_segments:
    if start_time >= full_duration:
        break
    elif end_time >= full_duration:
        end_time = full_duration
        
    video_clip = None
    subclip = None
    if speaker == "SPEAKER_00":
        video_clip = host_angle
    else:
        video_clip = guest_angle

    # Case 1: We are using a clip from a single speaker
    if start_time >= current_end_time:
        subclip = video_clip.subclip(start_time, end_time)
        subclips.append(subclip)
        current_end_time = end_time

    # Case 2: there is overlapping 
    elif end_time > current_end_time:
        # Overlapping segment, but extends beyond the current_end_time
        overlap_duration = current_end_time
        subclip = video_clip.subclip(overlap_duration, end_time)
        subclips[-1] = concatenate_videoclips([subclips[-1], subclip])
        current_end_time = end_time
    

# Fill gaps with wide angle
if video_segments[0][1] != "00:00:00.000":
    filler = default_video.subclip("00:00:00.000", video_segments[0][1])
    subclips.insert(0, filler)

# Fill in gaps with video_d
for i in range(len(subclips) - 1):
    gap_duration = subclips[i + 1].start - subclips[i].end
    if gap_duration > 0:
        filler = default_video.subclip(subclips[i + 1].start, subclips[i].end)
        subclips.insert(i + 1, filler)

final_video = concatenate_videoclips(subclips)
final_video.write_videofile(os.path.join("output", "output.mp4"))