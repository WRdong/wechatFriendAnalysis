#_*_coding:utf-8_*_

import os
import itchat
from pyecharts import Pie
from pyecharts import Bar
import wordcloud
import jieba
import re

class Analysis:

    def __init__(self, friends):
        self.friends = friends

    def sex(self):
        """
        性别生成饼图
        :return:
        """
        boy = 0
        girl = 0
        other = 0
        for friend in self.friends:
            if friend.Sex == 1:
                boy += 1
            elif friend.Sex == 2:
                girl += 1
            else:
                other += 1

        attr = ['男', '女']
        val = [boy, girl]
        pie = Pie('')
        pie.add('', attr, val, is_label_show=True)
        file = 'tmp/sex.html';
        pie.render(file)
        print "\n总好友数: %d 人, 男: %d 人, 女: %d 人, 未设置性别: %d 人" % (boy + girl + other, boy, girl, other)
        print "性别数据饼图生成：    %s/%s" % (self.getCurrentDir(), file)
    def area(self, isCity = True):
        """
        城市或省份生成柱形图
        :param isCity: False 为省份
        :return:
        """
        dataDict = {}
        for friend in self.friends:
            if isCity:
                infoName = friend.City
            else:
                infoName = friend.Province
            if len(infoName) == 0:
                continue
            if dataDict.has_key(infoName):
                dataDict[infoName] += 1
            else:
                dataDict[infoName] = 1
        dataList = sorted(dataDict.items(), key=lambda item: item[1], reverse=True)
        x_axis = []
        y_axis = []
        for i in range(len(dataList)):
            if i > 5:
                break
            x_axis.append(dataList[i][0])
            y_axis.append(dataList[i][1])

        if isCity:
            bar = Bar('城市分布(前 6)', '')
            kwargs = dict(
                name='城市',
                x_axis=x_axis,
                y_axis=y_axis
            )

            bar.add(**kwargs)

            file = 'tmp/city.html';
            bar.render(file)
        else:
            bar = Bar('省份(前 6)', '')
            kwargs = dict(
                name='省份',
                x_axis=x_axis,
                y_axis=y_axis
            )

            bar.add(**kwargs)
            file = 'tmp/province.html'
            bar.render(file)
        #print [x_axis, y_axis]
        print "%s数据柱形图生成：  %s/%s" % ( '城市' if isCity else '省份', self.getCurrentDir(), file)

    def signature(self):
        """
        签名生成云图
        :return:
        """
        signatureList = []
        for friend in self.friends:
            signatureStr = friend.Signature
            if len(signatureStr) == 0:
                continue
            signatureStr = re.sub('<span.*>.*</span>', '', signatureStr)
            signatureStr = re.sub(' ', '', signatureStr)
            signatureStr = re.sub("\n", '', signatureStr)
            signatureStr = re.sub("n+", '', signatureStr)
            signatureStr = re.sub(r'1f(\d.+)', '', signatureStr)
            signatureStr = signatureStr.strip()

            signatureList.append(signatureStr)
            info = [friend.NickName, friend.RemarkName, signatureStr]
            #print ", ".join(info)

        txt = " ".join(signatureList)
        txt = ' '.join(jieba.cut(txt))
        w = wordcloud.WordCloud(
            font_path='fangsong.ttf',
            background_color='white',
            width=600,
            height=400
        )
        w.generate(text=txt)
        file = 'tmp/signature.png'
        w.to_file(file)
        print "\n签名数据云图生成：    %s/%s" % (self.getCurrentDir(), file)

    def run(self):
        self.signature()
        self.sex()
        self.area(isCity=False)
        self.area(isCity=True)

    def getCurrentDir(self):
        return os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    analysis = Analysis(friends)
    analysis.run()





