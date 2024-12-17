import torch


device = torch.device('cuda')  # 设置为 CUDA 设备
x = torch.randn(3, 3).to(device)  # 创建一个 tensor 并移到 GPU 上
print("CUDA is available, operation successful!")

"""
请你创建一个大小为 torch.size([1,1,3]) 的tensor, 并且将该tensor 拼接在x 的后面，形成一个大小为 torch.size([1,4,3]) 的tensor
"""