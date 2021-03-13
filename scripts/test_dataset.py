#! /usr/bin/env python3
## -*- coding: utf-8 -*-

from nscl.datasets import get_available_datasets, initialize_dataset, get_dataset_builder
from clevrer.dataset_clevrer import build_clevrer_dataset  
from opts import load_param_parser 

initialize_dataset(args.dataset, args.version)
args = load_param_parser()
train_dataset = build_clevrer_dataset(args, 'train')
train_dataloader = train_dataset.make_dataloader(args.batch_size, shuffle=False, drop_last=True, nr_workers=args.data_workers)

for cur_iter, sampled_batch in enumerate(train_dataloader): 
    print(cur_iter)
    print(sampled_batch)