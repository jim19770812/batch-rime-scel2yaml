# -*- coding:utf-8 -*-
import datetime
import os

from scel2rime import scel2rime

if __name__=="__main__":
    basedir= os.curdir+"/sougou_scels"
    outputDir=os.curdir+"/dict_yaml"
    list=os.listdir(basedir)
    version= datetime.datetime.now().strftime('%Y%m%d')  
    for f in list:
        fn=basedir+"/"+f
        dictName=os.path.split(fn);
        # print(temp)
        name=os.path.splitext(dictName[1])[0]
        fnOutputRimeConfig="{}/{}.dict.yaml".format(outputDir, name)
        scel2rime(fn, fnOutputRimeConfig, name, version)
        print("rime词库{}处理完成".format(fnOutputRimeConfig))
