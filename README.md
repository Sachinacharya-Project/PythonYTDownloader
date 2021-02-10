# YouTube Video Downloader
This Small package download video and audio from YouTube with Given URL or Given Name
## Instruction
**We can download Video or Audio from Very Famous Platform YouTube. This Package is capable of downloading Video(S) or Audio(S) From YouTube PlayList or Individual Video with Just a Video URL or With Just the Name or say, title of a Video**
## Packages Used
*If you wanna download package explicitly then use following command*
````
pip install pytube
pip install requests
````
## USAGE
*Method Used to Download Video(s) or Audio(s).*
*First of all Import "ytdownload" from Package and use as given syntax:*
````
ytdownload(video_url, video_format, video_src_type, [optional])
````
## Parameters
*"ytdownload" accepts 3 or 4 parameterz 3 are positional means mandatory parameters and last one is optional and this function returns True or False*.

* **video_url:**: This argument represent the actual URL of Video Or PlayList (i.e. YouTube URL). It is of two type
* **video_format:**: This argument represent the format, you wanna download as. It is of Two Type 'video' or 'audio'
* **video_src_type**: This argument represent source type of video. It of Three type
  1. *'single'*: This is passed when single video or say, particular video is to be downloaded
  PlayList URL cannot be passed in the function if single src type is using but single video url can be passed

  2. *'playlist'*: This is passed when multiple video or say, PlayList of video is to be downloaded
  PlayList URL is to be passed not single video url

  3. *'name'*: This is passed when single video with just name say, a video without videoUrl but with name is to be downloaded
  Any sort of URL is not accepted but a string of video Name is Accepted
* **optional**: This argument represent the path where files are to be stored. If passed, File will be stored in the given path
like: C:\Users\username\Music which is a Default path for Audio and
C:\Users\username\Video which is a Default path for Videos incase path is not given
If path is given, Video and Audio will be stored in given PATH inside Videos and Music Folder resp.
syntax:
    ytdownload(video_url, video_format, video_src_type, path='C:\\Users\\')

## Example
````python
import PythonYTDownloader # or from PythonYTDownloader import ytdownload
data = PythonYTDownloader.ytdownload('falling by harry styles', 'video', 'name') # Downlading using only name 
# This data returm True or False according to downloaded or not
