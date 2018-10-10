# -*- coding: utf-8 -*-
#コーディング: utf-8
#------------------------------------------------------------------------------
import os,os.path
import re
import sys
import glob
import shutil

#------------------------------------------------------------------------------
"""
from ratetools.tools.archiveFiles.lib import rate_archiveFiles;reload(rate_archiveFiles)
rate_archiveFiles.saveMain(_path="",modeStr="_archive",modeDeco="_v")
"""
def splitPath(pathString=""):
    path,ext=os.path.splitext(pathString)
    scenesName=os.path.basename(path)
    scenesPath="/".join(path.split("/")[:-1])
    return list([scenesPath,scenesName,ext])

def folderItems(path):
    return sorted([os.path.basename(r) for r in glob.glob(path+"/*")])

def latestArchiveName(archiveItem):
    return max(archiveItem)

def savePath(scenesItem=[],category="",decoExt=True):
    if not decoExt:
        subFile=scenesItem[1]
    else:
        subFile=scenesItem[1:]
    return scenesItem[0]+"/"+category+"/"+"".join(subFile)

def saveItems(savepath=""):
    if not os.path.isdir(savepath):
        return None
    _items=folderItems(savepath)
    if not len(_items) :
        return None
    else :
        return _items

def currentVer(item,deco):
    itemNames=os.path.splitext(item)[0]
    itemName,itemNum=itemNames.split(deco)
    return itemNum

def nextSaveVer(verNum,verString=4):
    formatInt=verString
    nextVerInt=int(verNum)+1
    nextVerStr=("{0:0"+str(formatInt)+"d}").format(nextVerInt)
    return nextVerStr

def returnPrint(_pathA,_pathB):
    returnText=""

    pathAList=_pathA.split("/")
    pathBList=_pathB.split("/")

    padding=max(len(pathAList),len(pathBList))

    pathAList+=["" for x in range(padding-len(pathAList))]
    pathBList+=["" for x in range(padding-len(pathBList))]

    returnPath=[];returnA=[];returnB=[]

    for strA,strB in zip(pathAList,pathBList):
        if strA == strB:
            returnPath.append(strA)
        else :
            returnA.append(strA)
            returnB.append(strB)

    returnText+="\n"
    returnText+="/".join(filter(lambda s:s != '',returnPath))+"\n\n"
    returnText+="/".join(filter(lambda s:s != '',returnA))+"\n"
    returnText+="/".join(filter(lambda s:s != '',returnB))+"\n"

    return returnText
#------------------------------------------------------------------------------

def saveMain(_path="",modeStr="_archive",modeDeco="_v",modeExt=True):
    copyPath=_path.replace("\\","/")

    currentBaceName=splitPath(copyPath)[-2]
    currentBaceExt=splitPath(copyPath)[-1]

    _items=saveItems(savePath(splitPath(copyPath),category=modeStr,decoExt=modeExt))
    if _items is None:
        currentNum="0000"
    else :
        currentNum=currentVer(latestArchiveName(_items),modeDeco)

    saveVerName=currentBaceName+modeDeco+nextSaveVer(currentNum,verString=4)+currentBaceExt
    _savePath=savePath(splitPath(copyPath),category=modeStr,decoExt=modeExt)
    pastedpath=_savePath+"/"+saveVerName

    if not os.path.isdir(_savePath):
        os.makedirs(_savePath)
    shutil.copy2(copyPath,pastedpath)
    return returnPrint(copyPath,pastedpath)
