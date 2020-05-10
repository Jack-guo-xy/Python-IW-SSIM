from easydict import EasyDict as edict

__C = edict()

# cfg is treated as a global variable. 
# Need add "from config import cfg" for each file to use cfg.
cfg = __C

# Include IW pooling
__C.iw_flag = True
# number of scales
__C.Nsc = 5
# neigborhood size
__C.blSzX = 3
__C.blSzY = 3
# use parent scale
__C.parent = True
# noise level
__C.sigma_nsq = 0.4
# CUDA config
__C.use_cuda = False
# Data type (True: more similar to Matlab version but will be slower)
__C.use_double = False

