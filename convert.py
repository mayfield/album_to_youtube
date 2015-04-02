from pydub import AudioSegment
import moviepy.editor as mpy
import glob
import youtube_upload.main as ytup
# import scipy


class MusicVid(object):
    def __init__(self, title, description, category, tags, privacy, location, file):
        self.title = title
        self.description = description
        self.category = category
        self.tags = tags
        self.privacy = privacy
        self.location = location
        self.file = file

mvid = MusicVid("TestTitle", "This is a test", "Music", "", "unlisted", "=", 'output.mp4')
ytup.upload_video("client_secret.json", mvid, "output.mp4", 1, 1)


# # Set location of ffmpeg
# AudioSegment.ffmpeg = "/usr/local/bin/ffmpeg"
#
# # Search for all mp3 files in directory
# playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob.glob("*.mp3")]
#
# # Combine all songs into one file
# combined = AudioSegment.empty()
# for song in playlist_songs:
#     combined += song
#
# # Export the mp3 as merge.mp3
# combined.export("merge.mp3", format="mp3", bitrate="320k")
#
# # Prepare the video's audio track to be merge.mp3
# audio_track = mpy.AudioFileClip('merge.mp3')
#
#
# # Look for an image file to use in the video
# artwork = sorted(glob.glob("*.jpg"))
# if len(artwork) > 0:
#     # Choose the first image file found in the directory
#     picture = mpy.ImageClip(str(artwork[0]))
#     # Center the image on black background
#     picture = picture.on_color(size=(1280, 720), color=(0, 0, 0))
# else:
#     # Create plain black video
#     picture = mpy.ColorClip(size=(1280, 720), col=(0, 0, 0))
#
# picture = picture.set_audio(audio_track)
# picture = picture.set_duration(audio_track.duration)
#
# picture.write_videofile("output.mp4", fps=24, codec='mpeg4')
#
#
