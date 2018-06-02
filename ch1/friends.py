# -*- coding: utf-8 -*-
# filename : friends.py
def display_friends(fr_list):
    print(fr_list)

def insert_friends(fr_list, name):
    fr_list.append(name)
    return fr_list

def delete_friends(fr_list, idx):
    del fr_list[idx]
    return fr_list

author = 'Tutorial 2'