# 漫画爬虫

#### 介绍
看到的点个watch, star还有博客上点个赞啥的鼓励一下我吧(๑•̀ㅂ•́)و✧
[漫画爬虫阅读网页 预览地址：https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)
详细图文介绍请看：
[CSDN博文地址](https://blog.csdn.net/zero_mumu/article/details/107852060)

爬取过程：
![mumu漫画爬虫](https://img-blog.csdnimg.cn/20200816122420888.gif#pic_center)

漫画阅读网页所有功能展开后：
![漫画爬虫网页所有功能](https://mumu_zero.gitee.io/assets/%E5%9B%BE/%E5%A4%A7%E6%A6%82.jpg)

收起时：
![正常](https://mumu_zero.gitee.io/assets/%E5%9B%BE/%E6%AD%A3%E5%B8%B8.jpg)

一个阅读，爬取和下载还有打包漫画的python爬虫
我的邮箱：mumuwyyx@163.com欢迎你来评论，提意见。

 1. 可分章节下载漫画到本地
 2. 网页可调节漫画宽度，可调节亮度
 3. 上下滚动阅读
 4. 书架网页方便阅读，自动记录阅读位置，下次进入自动跳转
 5. 通过其中的漫画打包工具可将下载好的漫画每一章打包为一个zip压缩包，方便在comics++ 布卡漫画 tachiyomi等软件本地漫画功能中使用。
 6. 可通过本地网页阅读下载到本地的漫画
#### 软件架构
python3.8.X

依赖库：BeautifulSoup, tqdm, requests ,lxml, selenium, pydub, ffmpeg, simpleaudio


#### 安装教程
源码文件夹中的需要安装python3.8和相关依赖库（文件内有说明，还有安装库前记得换成国内pip源，要不可能下载失败）

打包好的exe内文件不需要安装，下载其中漫画爬虫.zip解压点击漫画爬虫.exe运行即可。

#### 使用说明
[漫画爬虫网页 预览地址：https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)
详细请看：[CSDN博文地址](https://blog.csdn.net/zero_mumu/article/details/107852060)
一.爬取
可以先到漫画网站上寻找想看的漫画再来打开爬虫爬取。
双击打开 漫画爬虫.py 或.exe

 1. 先输入你想看的漫画名称。//不建议输入太长的名称。
 2. 输入漫画序号 如输入数字 2选择......一些选择后等待爬取
 3. 点击打开 书架 即可开始阅读（爬取中也可以阅读）
 4. 建议把整个文件夹放在方便查看处 ，方便使用。
(漫画爬虫.py运行完毕后会将爬取到的目录，漫画图片地址，每章节页数的数据分别储存在*dist*目录下的 *章节名称.json，漫画地址.json，pages.json*文件内。然后合并为*data.json*供浏览器读取。)


二.漫画打包工具程序：
	选择需要打包的已下载的漫画执行后会在”Download“文件夹中对应的漫画名称文件夹下生成一个叫做 “打包好啦！”的文件夹，并将下载的漫画每一章打包成为一个zip压缩包放入其中，从而方便在其它软件中阅读，比如comics++; tachiyomi app;  布卡漫画app的本地漫画功能。

爬取中推荐使用谷歌chrome浏览器，IE11浏览器不稳定。
爬取中若使用IE浏览器请在爬取前进入IE的 *设置>Internet选项>安全>安全中四项* 都勾选启动保护模式或全部关闭保护模式并应用

//默认下载好的浏览器驱动程序对应 浏览器版本号如下（如果和你的浏览器版本与默认不同请到浏览器驱动文件夹的下载地址中下载对应版本驱动替换该文件夹中驱动程序）： 
 *IEDriverServer.exe>IE11浏览器；   chromedriver.exe>谷歌Chrome 88.0.4324.150；*
#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
5.  提出你宝贵的意见

6.  https://gitee.com/gitee-stars/)