import numpy as np
import torch.nn as nn
import torch
import math


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, head_num):
        super().__init__()
        self.hidden_size = hidden_size
        self.head_num = head_num
        self.head_dim = hidden_size // head_num
        
        self.query = nn.Linear(self.hidden_size, self.hidden_size)
        self.key = nn.Linear(self.hidden_size, self.hidden_size)
        self.value = nn.Linear(self.hidden_size, self.hidden_size)
        
        self.out_proj = nn.Linear(self.hidden_size, self.hidden_size)


    def forward(self, hidden_states):
        batch_size, seq_len, _ = hidden_states.shape
        
        Q = self.query(hidden_states) # (B, L, H)
        K = self.key(hidden_states)
        V = self.value(hidden_states)
        
        # (B, L, H) -> (B, L, num_heads, head_dim)
        Q = Q.view(batch_size, seq_len, self.head_num, self.head_dim)
        K = K.view(batch_size, seq_len, self.head_num, self.head_dim)
        V = V.view(batch_size, seq_len, self.head_num, self.head_dim)
        
        Q = Q.transpose(1, 2)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim) # score (B, head_num, L, L)
        attn_weights = torch.softmax(scores, dim=-1)
        
        out = torch.matmul(attn_weights, V)
        out = out.transpose(1, 2).contiguous()
        out = out.view(batch_size, seq_len, self.hidden_size) # (B, L, H)
        
        out = self.out_proj(out)
        
        return out