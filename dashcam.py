from moviepy.editor import *
import os

current_files=os.listdir()

current_filesB=os.listdir("D:/DashCam/Movie_B")

for filenameA in os.listdir("D:/DashCam/Movie_A"):
    filename_list=filenameA.split('_')
    number=filename_list[3]
    number_B=int(number)+1
    filename_list[3]=f"{number_B:03d}"
    filename_list[4]='B.MP4'
    filenameB='_'.join(filename_list)
    print(filenameB)

    filename_list_alt=filename_list
    number=filename_list_alt[2]
    number_B=int(number)+1
    filename_list_alt[2]=f"{number_B:06d}"
    filenameBalt = '_'.join(filename_list_alt)
    print(filenameBalt)
    videoB=None
    videoA=None     

    try:
        if not filenameB in current_filesB:
            print("Matching B Filename not found, trying alt name")
            filenameB=filenameBalt
            if not filenameB in current_filesB:
                print("Matching B Filename not found")
                raise Exception
        final_name=filenameA[:-6]+'.mp4'
        if final_name in current_files:
            print("video already completed, deleting existing clips")
            os.remove("D:/DashCam/Movie_A/"+filenameA)
            os.remove("D:/DashCam/Movie_B/"+filenameB)
        else:
            videoA = (VideoFileClip("D:/DashCam/Movie_A/"+filenameA).resize(0.33).set_position(('center','bottom'))).without_audio()
            videoB = VideoFileClip("D:/DashCam/Movie_B/"+filenameB)
            final_clip=CompositeVideoClip([videoB,videoA]).write_videofile(final_name,threads = 8, fps=24)
            #final_clip.close()#not sure if needed? pretty sure its giving me a 'NoneType' object has no attribute 'close' error

    except Exception as e:
        print(e)
        with open('somefile.txt', 'a') as the_file:
            the_file.write('Could not convert video '+filenameA+'\n')

    finally:
        if videoA:        
            videoA.close()
        if videoB:
            videoB.close()
