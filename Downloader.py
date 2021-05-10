from __future__ import unicode_literals
from pytube import YouTube
import os

class Downloader(object):
  """simple youtube mp3 downloader"""
  default_savepath = str(os.path.join(os.path.expanduser("~"),"Downloads"))

  def __init__(self, url, save_path = default_savepath, no_playlist = True):
      self.url = url
      self.save_path = save_path
      self.no_playlist = no_playlist

  def opts(self):
      return {
          "verbose" : False,
          "fixup"   : "detect_or_warn",
          "format"   : "bestaudio/best",
          "postprocessors" :[{
              "key" : "FFmpegExtractAudio",
              "preferredcodec"   : "mp3",
              "preferredquality" : "1411"
         }],
         "extarctaudio" : True,
         "outtmpl"      : self.save_path + "/%(title)s.%(ext)s",
         "noplaylist"   : self.no_playlist
     }

  def download(self):
      download_object = youtube_dl.Youtube(self.opts())
      download_object.download([self.url])

if __name__ == "__main__":
    while True:
        os.system("cls")
        print("""
    ;
    ;;
    ;';.
    ; ;;
    ;  ;;
    ;   ;;
    ;   ;;
    ;  ;'
    ;  '
,;;;,; [ Youtube Mp3 Downloader ]
;;;;;; [0] EXIT
';;;;' [1] DOWNLOAD SINGLE
       [2] DOWNLOAD MULTIPLE
    """)
        selection = input("  >>  ")
        if selection == "0":
            break
        elif selection == "1":
            url = input(r"Enter URL to song >> ")
            Downloader(url, no_playlist = True).download()
        elif selection == "2":
            url = input(r"Enter URL to playlist  >> ")
            Downloader(url, no_playlist = False).download()
        else:
            continue
          
           
