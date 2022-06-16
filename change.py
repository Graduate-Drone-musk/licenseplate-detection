import glob
import os

main_dir = 'C:\\Users\\parks\\Desktop\\carplate_detect\\yolo\\yolov5\\data\\labels'
train_d = os.path.join(main_dir, 'train')
test_d = os.path.join(main_dir, 'valid')

tr_folder_file = glob.glob(train_d+"\\*.txt")
te_folder_file = glob.glob(test_d+"\\*.txt")
for file in te_folder_file:
    with open(file, 'r') as f:
        lines = f.readlines()
        
        result = []
        for line in lines:
            line = '0' + line[-37:]
            result.append(line)
    
    with open(file, 'w') as f:
        f.write(''.join(result))