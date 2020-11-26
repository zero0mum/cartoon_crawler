# Cartoon crawler

#### Description
[CSDN blog address](https://blog.csdn.net/zero_mumu/article/details/107852060)
A Python crawler that crawls and downloads comics

1. Comic books can be downloaded locally in chapters
2. The web page can adjust the width of the cartoon
3. Scroll down and read
4. Local comics can be read and downloaded from local websites
Software architecture
Software Architecture Description
5. Through the cartoon packaging tool, each chapter of the downloaded cartoon can be packed into a zip compression package, which is convenient to use in the local cartoon function of (布卡漫画app)Buka comics.


#### Software Architecture
Software architecture description

#### Installation

Python3.8 and related dependent libraries need to be installed in the source folder (as described in the file)

The packaged exE file does not need to be installed, download the comic crawler. Zip unzip click the comic crawler.exe to run.

#### Instructions

You can go to the comic website to find the comic you want to see and then open the crawler to crawl.
Double click to open comic crawler.py

 1. First enter the name of the comic you want to see.// Long names are not recommended.
 2. Enter the comic serial number, such as the number 2
 3. It is suggested to put the extracted entire folder in a convenient place for viewing, comic crawler.py will generate a folder named the name of your selected comic in its own directory after running. The folder contains three files for the cartoon address.
Cartoon address.txt; chapter name.txt; cartoon name.html
 4. After entering the comic folder, click the comic name to read the comic, respectively click the two select file buttons in the upper left corner of the open web page to select the two corresponding.txt file.
 5. After the selection, ** click ** to read all files twice. 
 
 4. Cartoon packaging tool program:
You need to put the cartoon packing tool program in the same directory as the comic address. Txt and chapter name. Txt files in the comics to be packed, and then double-click to execute. After execution, a file called "packed up!" will be generated in the "downloaded comics" folder Each chapter of the downloaded comics is packaged into a zip package, which is convenient to read in other software, such as the local cartoon function of 布卡漫画app(Buka comic app).

Google chrome is recommended for crawling. IE11 is unstable.
If you are using IE browser during crawling, please enter the Settings of IE before crawling;>
Safety>All four items in security check the start protection mode and apply

// The browser version number of the downloaded browser driver by default is as follows (if the browser version is different from the default version, please download the corresponding version driver from the download address of the browser driver folder and replace the driver in this folder) 

* IEDriverServer.exe>Internet Explorer 11;   Chromedriver.exe>Google Chrome 84.0.4147;*

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
