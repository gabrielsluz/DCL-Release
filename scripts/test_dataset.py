#! /usr/bin/env python3
## -*- coding: utf-8 -*-

from clevrer.dataset_clevrer import build_clevrer_dataset  
from opts import load_param_parser 

args = load_param_parser()
train_dataset = build_clevrer_dataset(args, 'train')
train_dataloader = train_dataset.make_dataloader(args.batch_size, shuffle=False, drop_last=True, nr_workers=args.data_workers)

for cur_iter, sampled_batch in enumerate(train_dataloader): 
    print(cur_iter)
    print(sampled_batch)