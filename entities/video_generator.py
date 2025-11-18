# coding: utf8
from PIL import Image, ImageDraw, ImageOps
from entities.terminal_messages import TerminalMessages
from configs.config import Config
from configs.video_settings import VideoSettings
import os
from pathlib import Path
from moviepy.editor import *
import os.path
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_resize

class VideoGenerator:
  def __init__(self, songs: list):
    self.__songs = songs
    self.__clips = []
    self.__time_video = 0
    self.__preview = False
    self.__only_ten = False
    
  def generate_video(self):
    if not self.__test_json():
      return

    self.__cut_videos();


    if self.__preview:
      i = 0
    
    for song in self.__songs:
      if self.__only_ten:
        i += 1
        if i > 10:
          continue
      start = song.get_cut_time()[0]
      end = song.get_cut_time()[1]
      
      size_video1 = (1920,1080)
      size_video2 = (1280,720)
      
      if self.__preview:
        size_video1 = (155,155)
        size_video2 = (155,155)
      
      image = ImageClip(song.get_image_path()).resize(size_video1).set_duration(end-start).set_start(self.__time_video)
      clip = VideoFileClip(song.get_video_path()).resize(size_video2).set_position((50,88)).set_start(self.__time_video)

      clip = clip.crossfadein(1).crossfadeout(1)
      image = image.crossfadein(1).crossfadeout(1)
      
      self.__clips.append(image)
      self.__clips.append(clip)
      self.__time_video = self.__time_video+(end-start)
    final_clip = CompositeVideoClip(self.__clips)
    final_clip.write_videofile(Config.VIDEO_PATH + '/' + VideoSettings.video_name + VideoSettings.ext, codec=VideoSettings.codec, threads=VideoSettings.threads, bitrate=VideoSettings.bitrate, ffmpeg_params=VideoSettings.ffmpeg_params, fps=VideoSettings.fps)
  
  def __cut_videos(self):
    i = 0;
    
    for song in self.__songs:
      if self.__only_ten:
        if i > 10:
          continue
      if Config.google:
        target = Config.CUT_VIDEO_PATH + (str(song.get_id()) + ".mp4")
      else:
        target = Config.CUT_VIDEO_PATH + "\\" + (str(song.get_id()) + ".mp4")
        if self.__preview:
          target2 = Config.CUT_VIDEO_PATH + "\\" + (str(song.get_id()) + "asd.mp4")
      print(target)
      if not os.path.isfile(Path(target)):
        start = song.get_cut_time()[0]
        end = song.get_cut_time()[1]
        ffmpeg_extract_subclip(song.get_video_path(), start, end, targetname=target)
        song.set_video_path(target)
        if self.__preview:
          ffmpeg_resize(target, target2, [40,40])
          song.set_video_path(target2)
      else:
        song.set_video_path(target)
        if self.__preview:
          song.set_video_path(target2)
      i += 1
  
  def __test_json(self):
    t = 0
    for song in self.__songs:
      cut_time = song.get_cut_time()
      image = song.get_image_path()
      video = song.get_video_path()
      if not os.path.isfile(Path(image)):
        TerminalMessages.error(f'Did not found image: "{image}".')
        t = 1
      if not os.path.isfile(video):
        TerminalMessages.error(f'Did not found video file: "{video}".')
        t = 1
      if(cut_time[0] > cut_time[1]):
        TerminalMessages.error(f'Invalid time length: "{song.get_name()}".')
        t = 1
      if(cut_time[1] - cut_time[0] < 1):
        TerminalMessages.error(f'Invalid time length: "{song.get_name()}", cut time has to be higher than 3 seconds.')
        t = 1
    return(True if t != 1 else False)