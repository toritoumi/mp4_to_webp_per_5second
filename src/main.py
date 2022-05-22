import os
import ffmpeg
import math
import subprocess
import sys

def editVideo(fname,time,width,fps):
    basename=os.path.basename(fname)[:-4]
    dir='../output/'+basename
    try:
        os.makedirs(dir)
    except FileExistsError:
        print('folder exists')
    try:
        os.makedirs(dir+'/mp4')
    except FileExistsError:
        print('folder exists')
    try:
        os.makedirs(dir+'/webp')
    except FileExistsError:
        print('folder exists')
    video_info = ffmpeg.probe(fname)
    duration = float(video_info['streams'][0]['duration'])
    fnames_after=[]
    for i in range(math.floor(duration/time)+1):
        stream = ffmpeg.input(fname, ss=i*time, t=time)
        audio_stream = stream.audio
        fname_after=dir+'/mp4/'+basename+'_'+str(i)+'.mp4'
        stream = ffmpeg.output(stream, audio_stream, fname_after)
        stream=ffmpeg.overwrite_output(stream)
        fnames_after.append(fname_after)
        ffmpeg.run(stream)
    resolution=[video_info.get('streams')[0].get('width'),video_info.get('streams')[0].get('height')]
    for i in range(len(fnames_after)):
        allcommand=['ffmpeg','-y','-i',fnames_after[i], '-vcodec', 'libwebp','-filter:v','fps=fps='+str(fps),'-lossless','1','-compression_level','6','-loop','0','-preset','default','-an', '-vsync','0','-s',str(width)+':'+str(math.floor((width/resolution[0])*resolution[1])),dir+'/webp/'+basename+'_'+str(i)+'.webp']
        subprocess.run(allcommand)
        
if __name__=='__main__':
    args = sys.argv
    print(args)
    for i in range(4, len(args)):
        editVideo(args[i], int(args[1]), int(args[2]),int(args[3]))






