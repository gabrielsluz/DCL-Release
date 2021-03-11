#from shutil import copyfile #copyfile(src, dst)
import sys
import os
import os.path


'''
How is the dataset formatted:
sub_img_folder = 'image_'+str(sub_idx).zfill(2)+'000-'+str(sub_idx+1).zfill(2)+'000'
img_full_folder = os.path.join(self.args.frm_img_path, sub_img_folder) 
img_full_path = os.path.join(img_full_folder, 'video_'+str(scene_idx).zfill(5), str(frm_id+1)+'.png')

The code above generates something like:
../clevrer/image_00000-00001/video_00000/1.png

Therefore, we must extract the video frames.
Use ffmpeg
ffmpeg -i /datasets/video_07011.mp4 -vf fps=25 ./tst/out%d.png
'''

#Transverses the expected Clevrer format and returns the video paths
def list_videos_in_dir(dir_path):
    video_path_l = []
    for video_dir in os.listdir(dir_path):
        video_dir_path = os.path.join(dir_path, video_dir)
        if os.path.isfile(video_dir_path):
            continue
        for video_file in os.listdir(video_dir_path):
            video_file_path = os.path.join(video_dir_path, video_file)
            if os.path.isfile(video_file_path) and video_file_path.endswith('.mp4'):
                video_path_l.append(video_file_path)
    return video_path_l

def gen_new_from_old_paths(old_video_path_list, new_dir):
    new_video_path_list = []
    for old_path in old_video_path_list:
        video_dir, video_file = old_path.split("/")[-2:]
        new_image_dir = "image_" + video_dir.split("_")[1]
        new_video_dir = video_file.split(".")[0]
        new_video_path_list.append(os.path.join(new_dir,new_image_dir,new_video_dir))
    return new_video_path_list


if __name__=='__main__':
    old_dir = sys.argv[1] #clevrer/
    new_dir = sys.argv[2] #dcl_clevrer/
    fps = sys.argv[3] #
    set_dir = sys.argv[4] # video_train, video_validation or video_test
    #List all video_paths in old_dir, train, test and validation, then extract the frames.
    old_video_path_list = []
    old_video_path_list += list_videos_in_dir(os.path.join(old_dir, set_dir))
    
    #Create the video_dir_paths for the new format
    new_video_path_list = gen_new_from_old_paths(old_video_path_list, new_dir)
    
    for old_path, new_path in zip(old_video_path_list, new_video_path_list):
        print(old_path, new_path)
        if os.path.isdir(new_path):
            print("Skipped")
            continue
        #os.makedirs(new_path, exist_ok=True)
        #os.system("ffmpeg -i " +old_path + " -vf fps=" + str(fps) + " " + new_path + "/%d.png -hide_banner -loglevel warning")
