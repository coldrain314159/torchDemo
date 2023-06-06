'''
Version: v-1.0.0
Author: Liang Hongbin
Email: 1036578411@qq.com
Date: 2023-06-02 14:06:36
LastEditTime: 2023-06-02 17:24:08
LastEditors: Liang Hongbin<-->1036578411@qq.com
Description: construct completed model  构建完整模型
FilePath: \TorchDemo\models\model.py
READY TO EDIT
'''

import yaml 
import torch 
from torch import nn, Tensor 
import torch.nn.functional as F 
import numpy as np 


# 预训练模型
# 文本预训练
import transformers
# 图像预训练
import timm
import torchvision
import vit_pytorch 
# 多模态预训练
import diffusers 


class Model(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
    def forward(self):
        pass 
    
    

if __name__ == '__main__':
    test_in = None 
    model = Model()
    