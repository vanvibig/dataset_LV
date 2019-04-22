# -*- coding: utf-8 -*-

from underthesea import word_tokenize

data_new = open('data_Dang.txt', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

data_old = open('data25k.txt', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

data_new = [l.strip() for l in data_new if len(l) > 0]
data_old = [l.strip()  for l in data_old if len(l) > 0]

data_new = [l for l in data_new if len(l) > 0]
data_old = [l for l in data_old if len(l) > 0]

data_new = [word_tokenize(l, format='text') for l in data_new]
data_old = [word_tokenize(l, format='text') for l in data_old]

data_full = data_old + data_new
movie_lines_full_end = open('data_full_end_25k+newdata.txt', 'w', encoding='utf-8', errors='ignore')

#data_full = data_new
#movie_lines_full_end = open('data_full_end_only+newdata.txt', 'w', encoding='utf-8', errors='ignore')

num_lines = len(data_full)

data_full_new = []

for i in range(0,num_lines,2):
    a = data_full[i]
    b = data_full[i+1]
    if len(a.split(' ')) > 10 or len(b.split(' ')) > 10:
        continue
    data_full_new.append(a)
    data_full_new.append(b)

num_lines = len(data_full_new)

for i in range(0,num_lines):        
    movie_lines_full_end.write("L"+ str(i+1))
    movie_lines_full_end.write(" +++$+++ u0 +++$+++ m0 +++$+++ ")
    if i%2==0:
        movie_lines_full_end.write("BIANCA")
    else:
        movie_lines_full_end.write("CAMERON")
    movie_lines_full_end.write(" +++$+++ ")
    movie_lines_full_end.write(data_full_new[i])
    movie_lines_full_end.write("\n")

movie_lines_full_end.close()