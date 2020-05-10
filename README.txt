The procedure to install and run PyTorch IW-SSIM is provided below.

Note: This implementation is based on the Matlab version IW-SSIM. The Matlab
version IW-SSIM can be found here: https://ece.uwaterloo.ca/~z70wang/research/iwssim/

**********************************
INSTALLATION
**********************************
You may follow the installation guide (May. 2020) that we provide below for installing the dependencies:

1. Install Anaconda3 (A distribution of Python3, please see https://www.anaconda.com/distribution/)
2. Create a new virtual environment:
    2.1. Open terminal (Ubuntu)
    2.2. Run "conda create -n envname python=3.6"
    2.3. Install packages:
        2.3.1 numpy     "conda install -c anaconda numpy"
        2.3.2 pillow    "conda install -c anaconda pillow"
        2.3.3 scipy     "conda install -c anaconda scipy"
        2.3.4 pyrtools  "pip install pyrtools" 
        2.3.5 easydict  "conda install -c conda-forge easydict"
        2.3.6 PyTorch   "conda install pytorch==1.2.0 torchvision==0.4.0 cudatoolkit=10.0 -c pytorch"

We have tested the code on Ubuntu 18.04 with both CPU and GPU mode.

**********************************
PyTorch IW-SSIM USAGE
**********************************
1. Open terminal (Ubuntu)
2. Activate the virtual environment: "conda activate envname"
3. Run PyTorch IW-SSIM, run "python test.py"
    3.1. If you are using GPU, add "--use_cuda" to your command above.
    3.2. If you want a more precise result add "use_double" to your command above.

Note: PyTorch IW-SSIM requires RGB Color images as input and will convert it to grayscale itself.

**********************************
PyTorch IW-SSIM Time Analysis
**********************************
We compare PyTorch version IW-SSIM with Matlab version IW-SSIM with regard to time. The results are 
provided below. We run the test on Ref.bmp and Ref2.bmp, and we use a machine with 3.6GHz Intel Core 
i9-9900K processor, 32GB RAM, GeForce GTX 1660 GPU and Ubuntu 18.04 operating system. For one test we 
run 100 times. The same test is run 10 times and we take the average to get the following results. 

Method             Execution Time       Execution time(Relative to Python GPU version)

Python(GPU)        0.1912s/image        1.00      
Matlab             0.3148s/image        1.65  
Python(CPU)        0.3572s/image        1.87     

Note: The provided results are given when using single data type.

**********************************
PyTorch IW-SSIM Performance Analysis
**********************************
We compare PyTorch version IW-SSIM with Matlab version IW-SSIM with regard to performance. 
The results are provided below. We use three database (LIVE2, TID2013, LIVEMD) to test the 
PyTorch IW-SSIM. 

Database          Python version        Matlab version
                  PLCC    SRCC          PLCC    SRCC

LIVE2             0.9522, 0.9567        0.9522, 0.9567    
TID2013           0.8319, 0.7779        0.8319, 0.7779
LIVEMD            0.9109, 0.8836        0.9109, 0.8836

The scatter plots are put in the result folder. 

Note: The provided results are given when using single data type.

**********************************
Citation
**********************************
### references
We are making the PyTorch IW-SSIM model available to the research community free of charge. 
If you use this model in your research, we kindly ask that you reference our papers listed below:

Zhou Wang and Qiang Li, "Information Content Weighting for Perceptual Image Quality Assessment," 
IEEE Transactions on Image Processing, vol. 20, no. 5, pp. 1185-1198, May 2011.

@article{wang2010information,
  title={Information content weighting for perceptual image quality assessment},
  author={Wang, Zhou and Li, Qiang},
  journal={IEEE Transactions on image processing},
  volume={20},
  number={5},
  pages={1185--1198},
  year={2010},
  publisher={IEEE}
}







