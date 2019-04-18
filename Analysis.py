#_*_coding:utf-8_*_

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
                other += 0

        attr = ['男', '女']
        val = [boy, girl]
        pie = Pie('')
        pie.add('', attr, val, is_label_show=True)
        pie.render('tmp/sex.html')
        print [boy, girl]

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
            bar.render('tmp/city.html')
        else:
            bar = Bar('省份(前 6)', '')
            kwargs = dict(
                name='省份',
                x_axis=x_axis,
                y_axis=y_axis
            )

            bar.add(**kwargs)
            bar.render('tmp/province.html')
        print [x_axis, y_axis]


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
            print ", ".join(info)

        txt = " ".join(signatureList)
        txt = ' '.join(jieba.cut(txt))
        w = wordcloud.WordCloud(
            font_path='fangsong.ttf',
            background_color='white',
            width=600,
            height=400
        )
        w.generate(text=txt)
        w.to_file('tmp/signature.png')
        return txt

    def run(self):
        self.sex()
        self.area(isCity=False)
        self.area(isCity=True)
        self.signature()

if __name__ == "__main__":

    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends()
    analysis = Analysis(friends)
    analysis.run()




