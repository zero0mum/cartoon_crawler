# Cartoon crawler

#### Description
When you see it, click watch, star and like it on the blog to encourage me(๑•̀ㅂ•́)و✧
Cartoon crawler reading page preview address:

[Preview address1. https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)

[preview address 2. https://zero0mum.github.io/web/](https://zero0mum.github.io/web/)



[gitee project address](https://gitee.com/mumu_zero/cartoon_crawler)

[github project address](https://github.com/zero0mum/cartoon_crawler)

Please see the detailed introduction and help：
[CSDN blog address](https://blog.csdn.net/zero_mumu/article/details/107852060)

A Python crawler that crawls and downloads and import comics

If you have **bug**, you can create a new **issue** on Gitub or Gitee and then contact me by email.

My email is mumuwyyx@163.com. You are welcome to comment.

1. **Comic books can be downloaded locally in chapters**
2. The web page **can adjust the width of the cartoon**, Adjustable brightness
3. Scroll down and read
4. You can **import downloaded comics** to view
5. Local comics can be read and downloaded from local websites file
6. Each chapter of the downloaded comics can be packaged into a zip package through the **comic packaging tool**, which is convenient for use in local comic functions of Comics ++, Buka Comics, Tachiyomi and other software.
7. The web page can automatically record the progress of comics reading (stored through the browser localStorage)

The crawl process：
  ![mumu漫画爬虫](https://img-blog.csdnimg.cn/20200816122420888.gif#pic_center)

Comic reading page after all features are deployed：
![](C:\Users\HASEE\Desktop\漫画爬虫csdn\漫画爬虫功能全部展开.jpg)

When you put it away：
![](C:\Users\HASEE\Desktop\漫画爬虫csdn\漫画爬虫功能全部收起.jpg)

delete, zip, import tool:

![漫画导入](https://img-blog.csdnimg.cn/20210326132025741.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3plcm9fbXVtdQ==,size_16,color_FFFFFF,t_70#pic_center)

#### Software Architecture

python3.8.X

Dependent libraries: BeautifulSoup,  tqdm, requests ,lxml, selenium, pydub, ffmpeg, simpleaudio

- web use boostrap + mdui, lower left SIMS use stevenjoezhang [live2d - widget] (https://github.com/stevenjoezhang/live2d-widget)
- Python GUI programming using Pyside2
- page magnifying glass tools: author: Jafar Akhondali of [lightzoom] (https://github.com/JafarAkhondali/lightzoom)

#### Installation

Python3.8 and related dependent libraries need to be installed in the source folder (as described in the file)

The packaged exe file does not need to be installed, download the comic crawler. Zip unzip click the comic crawler.exe to run.

#### Instructions
[Cartoon crawler page preview address：https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)
Please see:[CSDN Blog address](https://blog.csdn.net/zero_mumu/article/details/107852060)
You can go to the comic website to find the comic you want to see and then open the crawler to crawl.
Double click to open comic crawler.py
ONE.

 1. First enter the name of the comic you want to see.// Long names are not recommended.
 2. Enter the comic serial number, such as the number 2, and select......
 Some options wait after the crawl
 3. Click to open the bookshelf to start reading (you can also read by climbing)
 4. It is recommended to put the whole folder in a place convenient to view and use.
 (After running comic crawler. Py, the crawled directory, comic image address, and page number of each chapter will be stored in *dist* directory in the chapter name. Json, comic address. Json, pages.json* file.
 It is then merged into *data.json* for the browser to read.

 TWO. Cartoon packaging tool program:
Selecting the downloaded manga to be packaged will generate a "Packaged!" folder in the corresponding manga name folder in "Download".
Folder, and each chapter of the manga downloaded into a zip package into it, so that it is easy to read in other software, such as Comics ++;
tachiyomi app; 
The local cartoon function of the Buka Comics App.

Google chrome is recommended for crawling. IE11 is unstable.
If you are using IE browser during crawling, please enter the Settings of IE before crawling;>
Safety>All four items in security check the start protection mode and apply

And set the zoom of Internet Explorer to 100%

// The browser version number of the downloaded browser driver by default is as follows (if the browser version is different from the default version, please download the corresponding version driver from the download address of the browser driver folder and replace the driver in this folder) 

* IEDriverServer.exe>Internet Explorer 11;   Chromedriver.exe>Google Chrome 88.0.4324.150;*

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request
5.  Give your valuable advice
6.  [github project address](https://github.com/zero0mum/cartoon_crawler)
7.  [gitee project address](https://gitee.com/mumu_zero/cartoon_crawler)
