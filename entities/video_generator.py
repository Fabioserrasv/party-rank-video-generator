# coding: utf8
from PIL import Image, ImageDraw, ImageOps
from entities.terminal_messages import TerminalMessages
from configs.config import Config
from configs.video_settings import VideoSettings
import os, json
from pathlib import Path
from moviepy.editor import *
import os.path
import time
class VideoGenerator:
  def __init__(self, songs: list):
    songs.sort(key=lambda x: x.get_average(), reverse=False)
    with open(Config.VIDEOS_JSON_PATH, 'r', encoding='utf-8') as f:
        clip_cut = json.load(f)
    for index, song in enumerate(songs):
      pos = str(index + 1)
      song.set_cut_time(clip_cut[pos]['cut_time'])
      song.set_image_path(str(clip_cut[pos]['image_path']))
      song.set_video_path(str(clip_cut[pos]['video_path']))
    self.__songs = songs
    self.__clips = []
    self.__time_video = 0
 
  def generate_video(self):
    if not self.__test_json():
      return

    for song in self.__songs:
      start = song.get_cut_time()[0]
      end = song.get_cut_time()[1]
      image = ImageClip(song.get_image_path()).resize((1920,1080)).set_duration(end-start).set_start(self.__time_video).fx(vfx.fadein,1).fx(vfx.fadeout,1)
      clip = VideoFileClip(song.get_video_path()).resize((1280,720)).set_position((50,88)).subclip(start,end).set_start(self.__time_video).fx(vfx.fadein,1).fx(vfx.fadeout,1)
  
      self.__clips.append(image)
      self.__clips.append(clip)
      self.__time_video = self.__time_video+(end-start)
    final_clip = CompositeVideoClip(self.__clips)
    final_clip.write_videofile(Config.VIDEO_PATH + '/' + VideoSettings.video_name + VideoSettings.ext, codec=VideoSettings.codec, threads=VideoSettings.threads, bitrate=VideoSettings.bitrate, ffmpeg_params=VideoSettings.ffmpeg_params)
    
  
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
      if(cut_time[1] - cut_time[0] < 3):
        TerminalMessages.error(f'Invalid time length: "{song.get_name()}", cut time has to be higher than 3 seconds.')
        t = 1
    return(True if t != 1 else False)