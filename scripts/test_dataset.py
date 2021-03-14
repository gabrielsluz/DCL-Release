#! /usr/bin/env python3
## -*- coding: utf-8 -*-

from nscl.datasets import get_available_datasets, initialize_dataset, get_dataset_builder
from clevrer.dataset_clevrer import build_clevrer_dataset  
from opts import load_param_parser 

args = load_param_parser()
initialize_dataset(args.dataset, args.version)
train_dataset = build_clevrer_dataset(args, 'train')
train_dataloader = train_dataset.make_dataloader(args.batch_size, shuffle=False, drop_last=True, nr_workers=args.data_workers)

print("Dataset Train len = {}".format(len(train_dataset)))
train_iter = iter(train_dataloader)
cur_iter = 0
while True:
    try:
        feed_dict = next(train_iter)
    except StopIteration: 
        break
    except:
        print("Failed to load item {}".format(cur_iter))
    cur_iter += 1
        
"""
Failed to load item 991
Failed to load item 2146
Failed to load item 2280
Failed to load item 2527
Failed to load item 2768
Failed to load item 2955
"""

initialize_dataset(args.dataset, args.version)
train_dataset = build_clevrer_dataset(args, 'validation')
train_dataloader = train_dataset.make_dataloader(args.batch_size, shuffle=False, drop_last=True, nr_workers=args.data_workers)

print("Dataset Val len = {}".format(len(train_dataset)))
train_iter = iter(train_dataloader)
cur_iter = 0
while True:
    try:
        feed_dict = next(train_iter)
    except StopIteration: 
        break
    except:
        print("Failed to load item {}".format(cur_iter))
    cur_iter += 1
        

initialize_dataset(args.dataset, args.version)
train_dataset = build_clevrer_dataset(args, 'test')
train_dataloader = train_dataset.make_dataloader(args.batch_size, shuffle=False, drop_last=True, nr_workers=args.data_workers)

print("Dataset Test len = {}".format(len(train_dataset)))
train_iter = iter(train_dataloader)
cur_iter = 0
while True:
    try:
        feed_dict = next(train_iter)
    except StopIteration: 
        break
    except:
        print("Failed to load item {}".format(cur_iter))
    cur_iter += 1
        