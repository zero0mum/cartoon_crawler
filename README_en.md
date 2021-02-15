# Cartoon crawler

#### Description
When you see it, click watch, star and like it on the blog to encourage me(๑•̀ㅂ•́)و✧
[Cartoon crawler page preview address：https://mumu_zero.gitee.io/](https://mumu_zero.gitee.io/)
[CSDN blog address](https://blog.csdn.net/zero_mumu/article/details/107852060)
A Python crawler that crawls and downloads comics
My email is mumuwyyx@163.com. You are welcome to comment.

1. Comic books can be downloaded locally in chapters
2. The web page can adjust the width of the cartoon, Adjustable brightness
3. Scroll down and read
4. Local comics can be read and downloaded from local websites
5. Each chapter of the downloaded comics can be packaged into a zip zip package through the comic packaging tool, which is convenient for use in local comic functions of Comics ++, Buka Comics, Tachiyomi and other software.
6. The web page can automatically record the progress of comics reading (stored through the browser localStorage)


#### Software Architecture
Software architecture description

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

// The browser version number of the downloaded browser driver by default is as follows (if the browser version is different from the default version, please download the corresponding version driver from the download address of the browser driver folder and replace the driver in this folder) 

* IEDriverServer.exe>Internet Explorer 11;   Chromedriver.exe>Google Chrome 88.0.4324.150;*

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request
5.  Give your valuable advice


#### Gitee Feature

1.  You can use Readme\_XXX.md to support different languages, such as Readme\_en.md, Readme\_zh.md
2.  Gitee blog [blog.gitee.com](https://blog.gitee.com)
3.  Explore open source project [https://gitee.com/explore](https://gitee.com/explore)
4.  The most valuable open source project [GVP](https://gitee.com/gvp)
5.  The manual of Gitee [https://gitee.com/help](https://gitee.com/help)
6.  The most popular members  [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
