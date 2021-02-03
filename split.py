import os
import shutil

def split(xml_list,xml_dir,output_dir):
    list_fp = open(xml_list,'r')
    for line in list_fp:
        line = line.strip()
        line += '.png'
        src = os.path.join(xml_dir,line)
        print(line)
        print("Processing %s"%(line))
        out = os.path.join(output_dir,line)
        print(output_dir)
        shutil.copyfile(src,out)

if __name__ == '__main__':
    list_fp = 'E://datasets//VOC//ImageSets//Main/train.txt'
    output = 'E://datasets//luna_train'
    xml_dir = 'E://datasets//VOC//JPEGImages'
    split(list_fp,xml_dir,output)