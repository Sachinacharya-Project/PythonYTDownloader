from setuptools import setup

description_long = """
This Program is Capable of Downloading Videos From YouTube.
    This Program can download video From PlayList or Individual Video with just
    URL (PlayList or YouTube URL) and Video Name(Single Video at a time).
    This Package is Created By Sachin Acharya under MIT license
"""
setup(
    name= "PythonYTDownloader",
    version= '0.1.2',
    author= "Sachin Acharya",
    author_email= "acharyaraj71@gmail.com",
    license="MIT",
    keywords= "Downloader YouTube PlayList Single PyTube",
    description= "YouTube Video Downloader",
    long_description= description_long,
    packages=['PythonYTDownloader'],
    install_requires=['pytube', 'requests']
    )

# python .\setup.py sdist bdist_wheel
# Import PythonYTDownloader