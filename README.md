
## 分析微信好友数据
如今 itchat 很方便调用个人微信号接口，通过利用 itchat、pyecharts、jieba、wordcloud 库实现 分析微信好友数据的功能:
- 性别
- 省份
- 城市
- 通过好友的签名生成云词图

### 准备
安装依赖库  itchat、pyecharts、jieba、wordcloud 自行百度
pyecharts 升级到 V1版本，与原来 V0.5X版本不兼容，安装 pyecharts 库需指定版本安装

`pip install pyecharts==0.5.11`

### Run
`python Analysis.py`



