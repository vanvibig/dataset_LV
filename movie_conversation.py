# -*- coding: utf-8 -*-

data_origin = open('data_full_end_25k+newdata.txt', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

data_origin = [l.strip() for l in data_origin if len(l) > 0]

movie_conversations_vn = open('movie_conversations_full_25k+newdata.txt', 'w', encoding='utf-8', errors='ignore')

num_lines = len(data_origin)

for i in range(0,num_lines,2):
    if i + 2 > num_lines:
        break
    movie_conversations_vn.write("u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L")
    movie_conversations_vn.write(str(i+1) + "', 'L" + str(i+2) + "']")
    movie_conversations_vn.write("\n")
    
movie_conversations_vn.close()