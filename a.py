import glob
dir = 'C:\\Users\\parks\\Desktop\\carplate_detect\\yolo\\yolov5\\runs\\train'

print('\\'.join(glob.glob(dir+"\\*")[-1].split("\\")[-3:]))