from os import listdir
from os.path import isfile, isdir
import xbmc


def play(playlist_file: str) -> bool: # ... audio/video files!
    if playlist_file != '' and isfile(playlist_file):
        xbmc.log("[script.video.autoplay] Starting playlist '%s'" % playlist_file, xbmc.LOGINFO)
        xbmc.executebuiltin('PlayMedia("%s", noresume)' % playlist_file)
        xbmc.executebuiltin("PlayerControl(RepeatAll)") #loop media player
        return True
    else:
        return False


def show(slideshow_dir: str, subdirs: bool, random: bool) -> bool: # ... photos!
    if slideshow_dir != '' and isdir(slideshow_dir):
        options = ''
        
        if subdirs:
            options += ", recursive"
        
        if random:
            options += ", random"
        else:
            options += ", notrandom"
        
        xbmc.log("[script.video.autoplay] Starting slideshow '%s' with options '%s'" % (slideshow_dir, options), xbmc.LOGINFO)
        xbmc.executebuiltin('SlideShow("%s"%s)' % (slideshow_dir, options))
        return True
    else:
        return False
