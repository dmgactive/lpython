# coding: utf-8


import os
#os.system一次执行多个命令

os.system('cd path-to-repo && svn ci')
os.system('cd path-to-repo; svn ci')

