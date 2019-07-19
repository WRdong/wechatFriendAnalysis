
## 分析微信好友数据
如今 itchat 很方便调用个人微信号接口，通过利用 itchat、pyecharts、jieba、wordcloud 库实现 分析微信好友数据的功能:
- 性别
- 省份
- 城市
- 通过好友的签名生成云词图

### 环境
python2.7

### 准备 
- 安装依赖库 itchat、pyecharts、jieba、wordcloud 
```
pip install itchat
pip install pyecharts==0.5.11
pip install jieba
pip install wordcloud
```

- 获取代码
```
git clone https://github.com/WRdong/wechatFriendAnalysis.git wechatFriendAnalysis
```

### RUN
```
cd wechatFriendAnalysis
python Analysis.py
```
运行后会弹出一个二维码，需通过微信扫码

### 结果
生成结果为 html 文件，在当前 tmp 目录下，用浏览器直接打开即可
```
./tmp/city.html
./tmp/province.html
./tmp/sex.html
./tmp/signature.png
```



