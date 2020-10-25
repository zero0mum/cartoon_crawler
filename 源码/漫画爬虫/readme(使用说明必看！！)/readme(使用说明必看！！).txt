本爬虫爬取的网站为 
【1】“百年漫画：https://www.bnmanhua.com/”
【2】“漫画呗：https://www.manhuabei.com/”
【3】“武侠漫画网：https://www.wuxiamh.com/list/rexue/”

1.安装python3 不会的看  https://blog.csdn.net/weixin_43790276/article/details/89439352(安装时记得勾选添加PATH环境变量)，
如果之前装过python3没有添加PATH的可以自行手动添加(不会的看 https://www.jianshu.com/p/986c1d04c5bf)，
或者重装一次，并记得安装时勾选上添加PATH环境变量。

2.安装好python3后点击  点我依赖库下载.bat ，运行成功一次就好了，以后不用再点了。
来安装 漫画爬虫.py所需几个依赖库BeautifulSoup, tqdm, requests ,lxml, selenium, pydub, ffmpeg, simpleaudio。

3.
可以先到漫画网站上寻找想看的漫画再来打开爬虫爬取。
双击打开 漫画爬虫.py 
	(1)先输入你想看的漫画名称。
	(2)输入漫画序号 如输入数字 2	   //不建议输入太长的名称。
	(3)建议把解压出来的整个文件夹放在方便查看处，漫画爬虫.py运行完毕后会在 自身所在目录生成名为你所选漫画名的文件夹 ，
文件夹里包含三个文件分别为 漫画地址.txt；章节名称.txt ；漫画名.html
	(4)进入漫画文件夹后点击 漫画名字看漫画，分别点击打开的网页左上角的两个选择文件按钮分别选择那两个对应的.txt文件，
	(5)选择完后 点击两次 读取全部文件按钮即可。

//浏览器驱动程序默认下载好的对应 浏览器版本号（如果和你的浏览器版本与默认不同请到浏览器驱动文件夹的下载地址中下载对应版本驱动替换该文件夹中驱动程序）： 
 msedgedriver.exe>新Edge 84.0.522.44；   chromedriver.exe>谷歌Chrome 84.0.4147；   MicrosoftWebDriver.exe>旧Edge 6.17134

//在漫画爬虫爬取过程中不要点击正在加载的进度条，点了进度条会停住不动。
//方向键盘左右键分别控制翻向上一章和下一张，如果左右键翻页失效，点一下漫画图片，再试试。
//如果浏览器有安装油猴脚本类插件建议对本漫画网页关闭插件，避免出bug。