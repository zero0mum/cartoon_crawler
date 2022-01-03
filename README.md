# 漫画爬虫

#### 介绍
写来玩的，看到的大佬点个watch, star还有博客上点个赞啥的鼓励一下我吧(๑•̀ㅂ•́)و✧

漫画爬虫阅读网页 预览地址：

[预览地址1.  https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)

[预览地址2.  https://zero0mum.github.io/web/](https://zero0mum.github.io/web/)



[码云项目地址](https://gitee.com/mumu_zero/cartoon_crawler)

[github项目地址](https://github.com/zero0mum/cartoon_crawler)

详细图文介绍和帮助请看：
[简书文章地址](https://www.jianshu.com/p/41f5b7e4baa5)
[CSDN博文地址](https://blog.csdn.net/zero_mumu/article/details/107852060)

一个阅读，爬取,导入和下载还有打包漫画的python爬虫

有**bug**可以在github或gitee上先新建一个**issue**然后邮箱联系我。

我的邮箱：mumuwyyx@163.com欢迎你来评论，提意见。

 1. **可分章节下载漫画**到本地
 2. 网页**可调节漫画宽度，可调节亮度**
 3. **上下滚动下拉式**阅读
  4. 可**导入下载的漫画**阅读
  5. 书架网页方便阅读，自动记录阅读位置，下次进入自动跳转
  6. 通过其中的**漫画打包工具**可将下载好的漫画每一章打包为一个zip压缩包，方便在comics++ 布卡漫画 tachiyomi等软件本地漫画功能中使用。
  7. 可通过本地网页阅读下载到本地的漫画

爬取过程:  ![mumu漫画爬虫](https://img-blog.csdnimg.cn/20200816122420888.gif#pic_center)



漫画阅读网页所有功能展开后：
![漫画爬虫功能全部展开](https://mumu_zero.gitee.io/others/漫画爬虫功能全部展开.jpg)



收起时：
![漫画爬虫功能全部收起](https://mumu_zero.gitee.io/others/%E6%BC%AB%E7%94%BB%E7%88%AC%E8%99%AB%E5%8A%9F%E8%83%BD%E5%85%A8%E9%83%A8%E6%94%B6%E8%B5%B7.jpg)



漫画删除打包导入工具：

![漫画导入](https://img-blog.csdnimg.cn/20210326132025741.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3plcm9fbXVtdQ==,size_16,color_FFFFFF,t_70#pic_center)

#### 软件架构
python3.8.X

依赖库：BeautifulSoup, tqdm, requests ,lxml, selenium, pydub, ffmpeg, simpleaudio

- 网页使用boostrap+mdui，左下角小人使用的是stevenjoezhang 的[live2d-widget](https://github.com/stevenjoezhang/live2d-widget)
- python GUI 编程使用pyside2
- 网页放大镜工具：作者：Jafar Akhondali 的 [lightzoom](https://github.com/JafarAkhondali/lightzoom)


#### 安装教程
源码文件夹中的需要安装python3.8和相关依赖库（文件内有说明有可以自动安装库的.bat批处理脚本，安装库前记得换成国内pip源，要不可能下载失败）

打包好的exe内文件不需要安装，下载其中.zip解压后点击漫画爬虫.exe运行即可。

#### 使用说明
[漫画爬虫网页 预览地址：https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)
详细请看：  [简书文章地址](https://www.jianshu.com/p/41f5b7e4baa5)           [CSDN博文地址](https://blog.csdn.net/zero_mumu/article/details/107852060)
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

并且将ie浏览器的缩放设置为100%

//默认下载好的浏览器驱动程序对应 浏览器版本号如下（如果和你的浏览器版本与默认不同请到浏览器驱动文件夹的下载地址中下载对应版本驱动替换该文件夹中驱动程序）： 
 *IEDriverServer.exe>IE11浏览器；   chromedriver.exe>谷歌Chrome 88.0.4324.150；*
#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
5.  提出你宝贵的意见
6.  [码云项目地址](https://gitee.com/mumu_zero/cartoon_crawler)
7.  [github项目地址](https://github.com/zero0mum/cartoon_crawler)