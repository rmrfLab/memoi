#coding=utf-8
import memoi
from ruamel import yaml         # pip3 install ruamel
import os

try:
    os.mkdir('libs')
except FileExistsError:
    pass
libPath = 'libs\\'

def getLibs():
    return [i.name for i in os.scandir(libPath) if i.name[-4:]=='.yml']
def loadLib(libName):
    f = open(libPath+libName+'.yml', 'r', encoding='utf-8')
    ls = yaml.load(f.read(), Loader=yaml.Loader)
    f.close()
    cards = []
    for i in ls:
        cards.append(memoi.Cards(i['front'], i['back'], i['hstrSum'], i['hstrCrct']))
    return cards
def saveLib(cards, libName):
    ls = []
    for i in cards:
        ls.append({'front':i.front, 'back':i.back, 'hstrSum':i.hstrSum, 'hstrCrct':i.hstrCrct})
    f = open(libPath+libName+'.yml', 'w', encoding='utf-8')
    yaml.dump(ls, f, Dumper=yaml.RoundTripDumper)
    f.close()
    return
