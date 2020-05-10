from argparse import ArgumentParser
from PIL import Image
import time

from IW_SSIM_PyTorch import IW_SSIM
from utils import *
from config import *


def main():

    iw_ssim = IW_SSIM(iw_flag=args.iw_flag, Nsc=args.Nsc, blSzX=args.blSzX,
                      blSzY=args.blSzY, parent=args.parent, sigma_nsq=args.sigma_nsq, 
                      use_cuda=args.use_cuda, use_double=args.use_double)
    
    iw_raw_scores = []
    for k in range(num_run):
        if k == 1:
            start = time.time()
        for i in range(num_imgs):
            iw_score = iw_ssim.test(rgb2gray(imgos[i]), rgb2gray(imgds[i]))    # test one image
    end = time.time()
    print('Avg time for one image', (end-start)/((num_run-1)*num_imgs), 's')
    print('Total time:', end-start, 's')

    
if __name__ == "__main__":

    parser = ArgumentParser(description='PyTorch IW-SSIM')
    parser.add_argument("--iw_flag", type=bool, default=cfg.iw_flag)
    parser.add_argument('--Nsc', type=int, default=cfg.Nsc,
                        help='iw-ssim scales (default: 5)')
    parser.add_argument('--blSzX', type=int, default=cfg.blSzX,
                        help='iw-ssim neighborhood size (default: 3)')
    parser.add_argument('--blSzY', type=int, default=cfg.blSzY,
                        help='iw-ssim neighborhood size (default: 3)')
    parser.add_argument('--parent', type=bool, default=cfg.parent,
                        help='incluse parent scale in neighborhood (default: True)')
    parser.add_argument('--sigma_nsq', type=float, default=cfg.sigma_nsq,
                        help='HVS noise (default: 0.4)')
    parser.add_argument('--use_cuda', type=bool, default=cfg.use_cuda,
                        help='use cuda (default: True)')
    parser.add_argument('--use_double', type=bool, default=cfg.use_double,
                        help='use_double (default: False)')

    args = parser.parse_args()

    # Time test
    img1 = np.asarray(Image.open('./images/Ref.bmp'))
    img2 = np.asarray(Image.open('./images/Ref2.bmp'))
    img3 = np.asarray(Image.open('./images/Dist.jpg'))
    img4 = np.asarray(Image.open('./images/Dist2.jpg'))
    imgos = [img2, img1]
    imgds = [img4, img3]
    mos = [1, 1]
    num_imgs = 2
    num_run = 100

    main()

    
