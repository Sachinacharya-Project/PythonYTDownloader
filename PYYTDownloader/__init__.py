from pytube import YouTube, Playlist
from pytube.cli import on_progress
import os, requests

# Exceptions Classes
class DownloaderExceptions(Exception):
    def __init__(self):
        print('Exception: DownloaderException')
class VideoUrlException(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return "VideoUrlException: {}".format(self.__message)
class VideoFormatError(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoFormatError: {}'.format(self.__message)
class VideoExistError(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoFormatError: {}'.format(self.__message)
class VideoSrcType(DownloaderExceptions):
    def __init__(self, message):
        self.__message = str(message).capitalize()
    def __str__(self):
        return 'VideoSrcType: {}'.format(self.__message)

# On Complete Print Check Sign
def on_complete():
    "Don't Use this, throws error"
    print(u'\u2713')
def getVideoUrl(topic):
    "Don't Use this, throws error"
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        try:
            raise VideoExistError("No Video Found with that name")
        except VideoExistError as e:
            print(e)
            return False
    return "https://www.youtube.com"+lst[count-5]

def checkExistence(name, path, **kargs):
    "Don't Use this, throws error"
    unwanted = ['/', '\\', '*', ':', '?', '"', '<', '>', '|', '#']
    name = str(name)+str(".mp3")
    cbType = kargs.get('get', '__default')
    for item in unwanted:
        if item in name:
            name = name.replace(item, '')
    path = os.path.join(path, 'Music')
    if cbType == '__default':
        return os.path.exists(os.path.join(path, name))
    else:
        return name
def rename(direc):
    "Don't Use this, throws error"
    direc = direc.replace('/', '\\')
    source = direc
    direc = direc.replace(".mp4", ".mp3")
    path = direc
    try:
        os.rename(source, path)
        on_complete()
    except FileExistsError:
        print("\nFile Already Exist")
class YouTubeVideoDownloader():
    def downloader(self ,video_url, video_format, **kargs):
        takenPath = kargs.get('path', '__default')
        if takenPath == '__default':
            takenPath = os.environ.get('USERPROFILE')
        if video_url == '':
            try:
                raise VideoUrlException("Video URL cannot be Empty String")
            except VideoUrlException as e:
                print(e)
                return False
        elif video_url == None:
            try:
                raise VideoUrlException('Video URL cannot be of NoneType')
            except VideoUrlException as e:
                print(e)
                return False
        else:
            video_format = video_format.lower()
            if video_format != 'video' or video_format != 'audio':
                ytd = YouTube(video_url, on_progress_callback=on_progress)
                video_title = ytd.title
                if video_format == 'audio':
                    if kargs.get('type'):
                        result = checkExistence(video_title, takenPath, get='playlist')
                    else:
                        result = checkExistence(video_title, takenPath)
                    if result == True:
                        print("Audio \"{}\"\nAlready Exist in \"{}\\Music\"\nTry Changing Path, if you wanna download anyway".format(video_title, takenPath))
                        return False
                    elif result == False:
                        print("Downloading Audio {}.mp3\n".format(video_title))
                        cb = ytd.streams.get_audio_only().download(f"{takenPath}\\Music")
                        ytd.register_on_complete_callback(rename(cb))
                        return True
                    else:
                        return result
                else:
                    print("Downloading Video {}.mp4\n".format(ytd.title))
                    ytd.streams.get_highest_resolution().download(f"{takenPath}\\Videos")
                    ytd.register_on_complete_callback(on_complete())
                    return True
            else:
                try:
                    raise VideoFormatError("Only Audio or Video format allowed")
                except VideoFormatError as e:
                    print(e)
                    return False
    def ytdownload(self, video_url, video_format, **kargs):
        """
        Download YouTube Video in Audio or Video Formate as Specified
        Takes Two Positional Arguments and one Optional Arguments
        1. video_url
            It is a Actual Video URL from YouTube. It may either be URL of
            Single Video or PlayList
        2. video_format
            It is a Format in which download should be taken place
            'audio' for Audio and 'video' for Video
        3. path='PATH'
            It is optional.
            It specifies where the files should be downloaded.
            By Default
                {}/Musics for Audio
                {}/Video for Video
            But by providing argument as
                path='certain_path' video or audio will be downloaded in certain_path
        eg:
        ytdownload(video_url, 'audio', path='C:/Users/root/Musics')
        """.format(os.environ.get('USERPROFILE'), os.environ.get('USERPROFILE'))
        path = kargs.get('path', '__default')
        video_src_type = ''
        if str(video_url).startswith('https://www.youtube.com'):
            if str(video_url).startswith('https://www.youtube.com/playlist'):
                video_src_type = 'playlist'
            else:
                video_src_type = 'single'
        else:
            video_src_type = 'name'
        if video_url == '' or None:
            try:
                raise VideoUrlException('Empty string or NoneType is not acceptable as VideoUrl')
            except VideoUrlException as e:
                print(e)
                return False
        else:
            if video_src_type == 'name':
                url = getVideoUrl(video_url)
                if video_format == 'video':
                    if self.downloader(url, 'video', path=path):
                        return True
                    else:
                        return False
                elif video_format == 'audio':
                    if self.downloader(url, 'audio', path=path):
                        return True
                    else:
                        return False
                else:
                    try:
                        raise VideoFormatError('Only Audio or Video format in allowed')
                    except VideoFormatError as e:
                        print(e)
                        return False
            elif video_src_type == 'single':
                if video_format == 'video':
                    if self.downloader(video_url, 'video', path=path):
                        return True
                    else:
                        return False
                elif video_format == 'audio':
                    if self.downloader(video_url, 'audio', path=path):
                        return True
                    else:
                        return False
                else:
                    try:
                        raise VideoFormatError('Only Audio or Video format in allowed')
                    except VideoFormatError as e:
                        print(e)
                        return False
            elif video_src_type == 'playlist':
                get_url = Playlist(video_url).video_urls
                if video_format == 'video':
                    for item in get_url:
                        if self.downloader(item, 'video', path=path):
                            pass
                        else:
                            return False
                    else:
                        return False
                elif video_format == 'audio':
                    collection = []
                    for item in get_url:
                        result = self.downloader(item, 'audio', path=path)
                        if result:
                            pass
                        else:
                            collection.append(result)
                    for item in collection:
                        if item == False:
                            return False
                        else:
                            return True
                    else:
                        return False
                else:
                    try:
                        raise VideoFormatError('Only Audio or Video format in allowed')
                    except VideoFormatError as e:
                        print(e)
                        return False
            else:
                try:
                    raise VideoSrcType('VideoSrcType Error: Only YouTube video can be downloaded')
                except VideoSrcType as e:
                    print(e)
                    return False