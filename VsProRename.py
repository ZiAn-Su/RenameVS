# -*- coding: utf-8 -*-
"""
https://github.com/ZiAn-Su/RenameVS

"""

from ast import Try
import os
from time import sleep
import chardet

def iter_files(old_kw, new_kw, root_dir):
    """
    遍历根目录
    :param old_kw: 旧词
    :param new_kw: 新词
    :param root_dir: 目录的绝对路径
    :return:
    """
    Postfixs={'cpp': 1,'h':1, 'sln':1, 'vcxproj':1, 'c':1,'rc2':1,'rc':1}
    #替换根文件夹名
    pos=root_dir.rfind('/')
    if(pos>=0):    
        root_dirname=root_dir[pos+1:]
        new_dir_path=root_dir[0:pos+1]+new_kw
        if(root_dirname==old_kw): 
            ldir=root_dir[0:pos]   
            if(os.path.exists(root_dir) and (not os.path.exists(new_dir_path))):
                os.rename(root_dir, new_dir_path)
            root_dir=new_dir_path
    #遍历如果文件名为旧名的则替换；如果文件为旧名的替换；打开.cpp .h .sln .vcxproj .c
    for root, dirs, files in os.walk(root_dir,topdown=False):
        #1 替换文件夹名称
        for dir_name in dirs:
            old_dir_path = os.path.join(root, dir_name)
            # 如果被替换的字符串在文件夹的名中，则替换成新的
            if old_kw in dir_name:
                new_dir_name = dir_name.replace(old_kw, new_kw)
                new_dir_path = os.path.join(root, new_dir_name)  
                #替换前，确认老文件/文件夹存在，并且新文件/文件夹不存在 
                if(os.path.exists(old_dir_path) and (not os.path.exists(new_dir_path))):           
                    os.rename(old_dir_path, new_dir_path)
        
        #2  如果后缀名在目标范围内，则替换内容     
        for file_name in files:  
            #确定后缀名
            ipos=file_name.rfind('.')          
            if(ipos<0):
                continue
            postfix=file_name[ipos+1:]
            #如果后缀名在目标范围内，则替换内容
            if(Postfixs.get(postfix,0)==0):
                continue
            old_file_path = os.path.join(root, file_name)
            old_file_path = old_file_path.replace('\\', '/')
            file_data = ""
            try:
                # 读该文件编码格式
                with open(old_file_path, 'rb')as file:
                    data=file.read()
                    curr_encode = chardet.detect(data)['encoding']    
                if(not '.db' in old_file_path):
                    # 如果被替换的字符串在文件内容中，先按行读出来，在替换
                    with open(old_file_path, 'r', encoding=curr_encode, errors='ignore') as f:
                        for line in f.readlines():
                            new_line = line.replace(old_kw, new_kw)
                            file_data += new_line
                    with open(old_file_path, 'w', encoding=curr_encode, errors='ignore') as f:
                        f.write(file_data)
            except:
                print(old_file_path+'cant open!')
                continue    
        
        #3 替换文件名称； 
        for file_name in files:
            # 如果被替换的字符串在文件的名中，则替换成新的
            if old_kw in file_name:
                old_file_path = os.path.join(root, file_name)
                new_file_name = file_name.replace(old_kw, new_kw)
                new_file_path = os.path.join(root, new_file_name)
                if(os.path.exists(old_file_path) and (not os.path.exists(new_file_path))):  
                    os.rename(old_file_path, new_file_path)          

def run():
    print('@ https://github.com/ZiAn-Su/RenameVS')
    print('@ 输入项目文件夹绝对路径')
    path = input()  
    #path = ''
    path = path.replace('\\', '/')
    path = path.replace('//', '/')
    print('@ 输入原项目名称')
    old_project_name = input()
    #old_project_name = ''
    print('@ 输入新项目名称')
    new_project_name = input()
    #new_project_name = ''
    print('@ 重命名中....')
    iter_files(old_project_name, new_project_name, path)
    print('@ 重命名完成！')
    sleep(5)

if __name__ == '__main__':
    run()
    
