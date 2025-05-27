# exercises/normalize.py
"""
练习：数据标准化 (Normalization)

描述：
实现数据标准化功能，将输入数据缩放到指定范围。

请补全下面的函数 `normalize`。
"""
import numpy as np

def normalize(x, min_val=0.0, max_val=1.0):
    """
    将输入数据标准化到[min_val, max_val]范围。

    Args:
        x (np.array): 输入数组
        min_val (float): 标准化后的最小值，默认为0.0
        max_val (float): 标准化后的最大值，默认为1.0

    Return:
        np.array: 标准化后的数组
    """
    # 请在此处编写代码
    # 提示：
    # 1. 计算输入数据的最大值和最小值
    # 2. 执行线性变换：(x - min) / (max - min) * (new_max - new_min) + new_min
    # 3. 处理除零情况(当max-min=0时)
    # 计算输入数据的最大值和最小值
    x_min = np.min(x)
    x_max = np.max(x)
    
    # 处理除零情况(当所有值相同时)
    if x_max == x_min:
        return np.full_like(x, (min_val + max_val) / 2)
    
    # 执行线性变换
    normalized = (x - x_min) / (x_max - x_min) * (max_val - min_val) + min_val
    
    return normalized
