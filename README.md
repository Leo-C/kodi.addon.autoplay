# Autoplay for Kodi


## Introduction

**Autoplay for Kodi** is an Addon to play automatically media file and/or show photos (perfect for Kiosk mode).  

It plays in loop a media file or a playlist and / or shows photos  


## Configuration

In Setting Page some items help to customize behavior of Addon.

Two sections helps to activate a Media Playlist and / or a SlideShow
(note that if you activate Slideshow and and Audio Playlist, images are shown with a musical background)

* **Enable Audio / Video Media**: enable play of audio / video media
* **Media file or Playlist**: choose media file or playlist

* **Enable Slideshow**: Enable Slideshow
* **Slideshow folder**: Select Slideshow folder**
* **Use subfolders**: Show also images in subfolder of that choosen
* **Play images in random order**: reproduce images in alphabetical order or random

* **Start reproduction**: start Addon for testing (to stop simply stop video or get back)

If you want to start this Addon at Kodi boot, I suggest to use [Kodi Autoplay Addon](https://github.com/leo-c/service.autoexec.addon)
(check correct branch for your Kodi version)


## Compatibility

This Addon was tested on following platfoms (see branch compatibility on GitHub):
|   Kodi version  |       Distribution       |             HW             | Works | Branch | Notes |
| :-------------: | :----------------------: | :------------------------: | :--: | :----: | :---- |
| Kripton - 17.6 | LibreELEC-RPi.arm-8.2.5  | RasPi v1.2 model B+        |   Y   |  py2   |       |
| Leia - 18.9    | LibreELEC-RPi.arm-9.2.6  | RasPi v1.2 model B+        |   Y   |  py2   |       |
| Matrix - 19.1  | LibreELEC-RPi.arm-9.97.1 | RasPi v4 model B with 4GB  |   Y   |  py3   | Addon Icon not show |

If anyone tests this Addon on other HW platforms / SW distribution, I'll insert into list


## Installation

Unless this addon was not included in a Kodi repository, must be installed manually.
To do so:
1. download this github repository as .zip
2. transfer file on host with Kodi (via network, USB memory, etc.)
3. in addon section choose "Install from .zip file" and browse file location
   (remember - if not asked - to enable installation of .zip addon from Setings -> Addon -> unknown source)


## Localization

If you want to add other localizations, you're welcome!
(send me `string.po` file and Addon description in addon.xml or do a Pull Request)
