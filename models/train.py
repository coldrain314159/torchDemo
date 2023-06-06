'''
Version: v-1.0.0
Author: Liang Hongbin
Email: 1036578411@qq.com
Date: 2023-06-02 14:08:08
LastEditTime: 2023-06-02 17:18:20
LastEditors: Liang Hongbin<-->1036578411@qq.com
Description: 模型训练逻辑实现 -- accelerate 训练框架实现
FilePath: \TorchDemo\models\train.py
READY TO EDIT
'''
import os 
import argparse
import logging 
from pathlib import path 
from tqdm.auto import tqdm 
import yaml 

import torch 
import torch.nn as nn 
import torch.nn.functional as F 
from accelerate import Accelerator 
from accelerate.utils import (
    is_bf16_available,
    is_tensorboard_available, 
    is_wandb_available,
    is_deepspeed_available,
    is_fp8_available,
    
)
from transformers import is_bitsandbytes_available
from transformers.utils import is_torch_tf32_available, is_torch_cuda_available



def parser_args():
    parser = argparse.ArgumentParser(description='模型训练参数')
    parser.add_argument('--load_train_config_path', default=None, type=str, 
        help=('训练参数yaml文件路径,当不为None，使用yaml文件内容配置args',
            '否则使用命令行模式传入可配置训练参数'))
    
    
    args = parser.parse_args()
    return args 

def main(args):
    pass 

def prepare_for_train():
    pass 

def train_epoch():
    pass 

def train_step():
    pass 

def evaluate_epoch():
    pass 

def valid_step():
    pass 

def save_checkpoint():
    pass 

if __name__ == '__main__':
    args = parser_args()
    main(args)
    