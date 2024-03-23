'''
Version: v-1.0.0
Author: Liang Hongbin
Email: 1036578411@qq.com
Date: 2023-06-02 14:06:54
LastEditTime: 2023-06-02 17:06:52
LastEditors: Liang Hongbin<-->1036578411@qq.com
Description: 图像和文本的预处理模块
FilePath: \TorchDemo\models\utils.py
READY TO EDIT
'''

import os 
import psutil
import base64
import numpy as np 
from typing import Any, Union, List, Dict

import requests 
from bs4 import BeautifulSoup 
from datasets import load_dataset, load_dataset_builder
import torch 
import torch.nn as nn 
import torch.nn.functional as F 
from torch.nn import Tensor 
from torch.utils.data import Dataset, DataLoader 
import torchvision.transforms as tfs 
from einops import rearrange, reduce, repeat 

# 文件遍历
from glob import glob 

# 图像预处理相关imports
import matplotlib.pyplot as plt 
from PIL import Image 
import kornia
import cv2 
# 文本预处理相关imports 
import re 
import jieba 
import tokenizers 


class ImageDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
    
    def __getitem__(self, index) -> Any:
        return super().__getitem__(index)
    
    def __len__(self,):
        pass 


class TextDataset(Dataset):
    def __init__(self) -> None:
        super().__init__()
    
    def __getitem__(self, index) -> Any:
        return super().__getitem__(index)
    
    def __len__(self,):
        pass 
    
def img_collate_fn(examples):
    pass 

def text_collate_fn(examples):
    pass 

def img_transform():
    pass 

def text_transform():
    pass 

def get_dataloader(sample_mode='image',training_mode='train'):
    pass 