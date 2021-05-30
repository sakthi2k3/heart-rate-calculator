import imageio
import numpy as np
fps=30
red=[]
def hearbeat(filename):
    video = imageio.get_reader(filename)
    for frames in video:
        lp=np.mean(frames,axis=(0,1))
        red.append(lp[0])

    m=max(red)
    hr=m*fps/60-30
    """" 30 has been subracted to get the value more accurate"""
    return round(hr,2)

