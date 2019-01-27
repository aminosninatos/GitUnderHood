Repair m4a file
------------------------------
------------------------------


Using FFmpeg  to fix M4a Audio Files
-----------------------------------------------------------------------------------
> ffmpeg.exe -i myAudioFile.m4a -c copy myAudioFile_REMUX.m4a

 
Recovering corrupted m4a recordings
---------------------------------------------------------------------
> dd ibs=1 skip=44 if=yourfilename.m4a of=raw.m4a
>  faad -a newname.m4a raw.m4a


Recover_mp4
-----------------------------------------------------------------------------------------------------------------------------------------
Step 1: Use any good previous file with the same resolution and bitrate to generate the header files, for example

>recover_mp4.exe good.mp4 --analyze
It will create files 'video.hdr' and 'audio.hdr' in the current directory and print instructions (ffmpeg options, etc.).

Step 2: Recover streams from the corrupted file, for example
>recover_mp4.exe bad.mp4 recovered.h264 recovered.aac

Note: Files 'video.hdr' and 'audio.hdr' must be exist.
Probably you need to add a specific option (look at instructions from step 1).

Step 3: Use any other utility (Yamb, ffmpeg or mp4box for exmaple) 
to recreate the MP4/MOV file from the streams (recovered.h264 and recovered.aac).

>ffmpeg.exe -r 30 -i recovered.h264 -i recovered.aac -bsf:a aac_adtstoasc -c:v copy -c:a copy recovered.mp4

Note MP4 does not support PCM sound, you must create MOV in this case:

>ffmpeg.exe -r 30 -i recovered.h264 -i recovered.wav -c:v copy -c:a copy recovered.mov

In case of ADPCM audio:

>ffmpeg -r 30 -i recovered.h264 -i recovered.wav -c:v copy -c:a adpcm_ima_wav recovered.mov

Note: 30 is FPS in these examples. Specify your correct value.
In case of 29.97 I suggest to specify 30000/1001 instead.


Fix atoom mov not found
------------------------------------------------------------------------------------------
1) Install some libraries with this command:
sudo apt-get install libavformat-dev libavcodec-dev libavutil-dev

2) Download the source code for Untrunc from the github repo:
wget https://github.com/ponchio/untrunc/ar...

3) Unzip the source code:
unzip master.zip

4) Go into the directory where it's been unzipped:
cd untrunc-master

5) Compile the source code using this command (all one line):
g++ -o untrunc file.cpp main.cpp track.cpp atom.cpp mp4.cpp -L/usr/local/lib -lavformat -lavcodec -lavutil

Then you can actually fix the video. You need both the broken video and an sample working video from the same stream.
like this video was a screen capture using OBS so I took a similar video of small size tkane with OBS with same settings like 60fps and 1920 x 1080.
or if you are using video, it should be from the same camera & have the same resolution. 

Run this command in the folder where you have unzipped and compiled Untrunc and then replace the path with your real path
./untrunc /path/to/working-video.mp4 /path/to/broken-video.mp4
