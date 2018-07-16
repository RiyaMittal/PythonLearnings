#!/usr/bin/python27

import os
import re
import fnmatch


word_list=[]
word_count=[]
word_dic={}
for dirName,subDirName,fileList in os.walk('C:\home'):
    print ("Found Directory: %s"%dirName)
    print ("subdirectory: %s" %subDirName)
    #print fileList
    for fname in fileList:
        #fnmatch.filter(fname,"*Riya*")
        word_list=[]
        file_path_1=os.path.join ( dirName, fname )
        #file_path=os.path.abspath(fname)
        print "file name :{0} \t path is :{1}".format(fname,file_path_1)
        fh=open(file_path_1,'r')
        #print "File Found",fname
        for lines in fh:
            words=lines.split()
            for word in words:
                word_list.append(word)
        fh.close()
        count_of_words=int(len(word_list))
        word_dic[fname]=count_of_words
        #print word_dic
        print "file name :{0} \t count of words is :{1}".format ( fname, count_of_words )

            



