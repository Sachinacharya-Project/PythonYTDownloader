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
ytdownload(video_url, video_format, [optional])
````
## Parameters
*"ytdownload" accepts 3 or 4 parameterz 3 are positional means mandatory parameters and last one is optional and this function returns True or False*.

* **video_url:**: This argument represent the actual URL of Video Or PlayList (i.e. YouTube URL). It is of two types
  1. **URL**: This a actual URL to YouTube Video or YouTube PlayList
  2. **name**: This is Title of Video or Common Name to the video, like 'Latest Python Packages reviews'. It cannot use title of PlayList but single video
* **video_format:**: This argument represent the format, you wanna download as. It is of Two Types 'video' or 'audio'
* **optional**: This argument represent the path where files are to be stored. If passed, File will be stored in the given path
like: C:\Users\username\Music which is a Default path for Audio and
C:\Users\username\Video which is a Default path for Videos, incase path is not given.
But if path is given, Video and Audio will be stored in given PATH inside Videos and Music Folder resp.
  syntax:
      ytdownload(video_url, video_format, path='C:\\Users\\')

## Example
````python
import PythonYTDownloader
data = PythonYTDownloader.ytdownload('falling by harry styles', 'video') # Downlading using only name 
# This data returns True or False according to downloaded or not
````
## Command-line
  **1. pyytdownloader -h**: Shows Helps
  **2. pyytdownloader video_url video_format --path PATH**: --path PATH is optional and all arguments are the samee as explained above
