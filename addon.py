import xbmc
import xbmcaddon
from resources.lib.autoplay import play, show


#read config values
playlist_en:str = xbmcaddon.Addon().getSetting("playlist_en")
playlist_file:str = ""
if playlist_en == "true":
    playlist_file = xbmcaddon.Addon().getSetting("playlist_file")

slideshow_en:str = xbmcaddon.Addon().getSetting("slideshow_en")
if slideshow_en == "true":
    slideshow_dir:str = xbmcaddon.Addon().getSetting("slideshow_dir")
    
    slideshow_subdir_str:str = xbmcaddon.Addon().getSetting("slideshow_subdir")
    slideshow_subdir:bool = False #default
    if slideshow_subdir_str == "true":
        slideshow_subdir = True

    slideshow_random_str:str = xbmcaddon.Addon().getSetting("slideshow_random")
    slideshow_random:bool = False #default
    if slideshow_random_str == "true":
        slideshow_random = True
else:
    slideshow_dir = ""

#start playlist and / or slideshow
if playlist_file != "":
    if play(playlist_file):
        xbmc.sleep(1000)
if slideshow_dir != "":
    show(slideshow_dir, slideshow_subdir, slideshow_random)
