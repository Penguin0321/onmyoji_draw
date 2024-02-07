# -*- coding: utf-8 -*-
import random
from tqdm import tqdm

prob_ssp = 1.25 / 100 # 抽到ssr/sp黑屏的概率

# 各挡位黑屏抽到新式神的概率，SSR的概率更高。每60抽挡位+1，450抽保底出新式神
sp_prob  = [0.10, 0.12, 0.14, 0.18, 0.25, 0.40, 0.55, 0.8]
ssr_prob = [0.15, 0.17, 0.19, 0.25, 0.35, 0.45, 0.60, 0.8]


def is_ssp(prob) -> bool: # 模拟一次抽卡，是否为SSR/SP
    return random.random() < prob

def is_target(prob) -> bool: # 模拟一次黑屏，是否为新式神
    return random.random() < prob

def simulate(target_is_ssr, start=0) -> int: # 模拟一轮抽卡，直至出新式神
    """
    target_is_ssr: 新式神是否为ssr
    start: 已抽票数，默认为0
    """
    
    not_ssp = 0 # 记录非SSR/SP的次数
    for i in range(start, 450):
        if not_ssp == 60 or is_ssp(prob_ssp): # 60抽保底黑屏
            not_ssp = 0
            if target_is_ssr:   # 根据新式神稀有度和已抽卡数对黑屏抽到新式神的概率赋值
                prob_target = ssr_prob[i // 60]
            else:
                prob_target = sp_prob[i // 60]
            
            if is_target(prob_target):
                break
        else:
            not_ssp += 1

    return i + 1 # 返回出货时抽卡数

if __name__ == "__main__":
    n = 1000000
    total = 0
    for i in tqdm(range(n)):
        total += simulate(1, 100)
    
    print('\n', total / n)
        
        