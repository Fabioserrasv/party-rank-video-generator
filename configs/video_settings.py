class VideoSettings:
  video_name = 'teste_refatoracao'
  ext = '.wmv'
  codec = 'mpeg4'
  threads = '4'
  bitrate = '6350k'
  ffmpeg_params = ['-tile-columns', '6', '-frame-parallel', '0',
                   '-auto-alt-ref', '1', '-lag-in-frames', '25', '-g',
                   '128', '-pix_fmt', 'yuv420p', '-row-mt', '1']