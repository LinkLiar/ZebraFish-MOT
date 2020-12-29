import numpy as np
import cv2
import glob
import os

WSI_MASK_PATH = 'D:\\bishe\\3DZeF20\\3DZeF20\\train\\ZebraFish-01\\gt_F\\'#存放图片的文件夹路径
paths = glob.glob(os.path.join(WSI_MASK_PATH, '*.png'))
paths.sort()

fourcc =cv2.VideoWriter_fourcc('M','J','P','G')   # 保存视频的编码
out = cv2.VideoWriter("ZebraFish-01.avi", fourcc, 60.0, (2704, 1520))

for path in paths:
    videoPlay = cv2.imread(path)
    out.write(videoPlay)
    print(path)

out.release()
print("Done")