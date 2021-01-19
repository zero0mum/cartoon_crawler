详细使用教程：https://blog.csdn.net/zero_mumu/article/details/107852060
码云项目地址：https://gitee.com/mumu_zero/cartoon_crawler
欢迎你来评论，提意见。

本爬虫爬取的网站为 
【1】“百年漫画：https://www.bnmanhua.com/”
【2】“漫画呗：https://www.manhuabei.com/”目前网站挂了
【3】“古风漫画网: https://www.gufengmh8.com/”

1.安装python3 可以参考https://blog.csdn.net/weixin_43790276/article/details/89439352(安装时记得勾选添加PATH环境变量)，
如果之前装过python3没有添加PATH的可以自行手动添加(可以参考https://www.jianshu.com/p/986c1d04c5bf)，
或者重装一次，并记得安装时勾选上添加PATH环境变量。

2.安装好python3后点击  点我依赖库下载.bat （安装库前记得换成国内pip源，要不可能下载失败，运行成功一次就好了。）
来安装 漫画爬虫.py所需几个依赖库BeautifulSoup, tqdm, requests ,lxml, selenium, pydub, ffmpeg, simpleaudio。

3.
可以先到漫画网站上寻找想看的漫画再来打开爬虫爬取
双击打开 漫画爬虫.py 
	(1)先输入你想看的漫画名称。//不建议输入太长的名称。
	(2)输入漫画序号 如输入数字 2
爬取完成后双击 书架开始阅读（别点阅读）


//浏览器驱动程序默认下载好的对应 浏览器版本号（如果和你的浏览器版本与默认不同请到浏览器驱动文件夹的下载地址中下载对应版本驱动替换该文件夹中驱动程序）： 
 chromedriver.exe>谷歌Chrome 86.0.4240.183；IEDriverServer.exe>ie11浏览器

//在漫画爬虫爬取过程中不要点击正在加载的进度条，点了进度条可能会停住不动。
//方向键盘左右键分别控制翻向上一章和下一张，如果左右键翻页失效，点一下漫画图片，再试试。