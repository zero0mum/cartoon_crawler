#!/usr/bin/env python
import requests,time,os,shutil,sys,shutil,urllib
from pydub import AudioSegment
from pydub.playback import play
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.ie.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
caps = DesiredCapabilities().INTERNETEXPLORER

options = webdriver.IeOptions()
options.page_load_strategy = 'eager'#ie无图

chrome_options = webdriver.ChromeOptions()
prefs = {
      'profile.default_content_setting_values': {
          'images': 2,
          'permissions.default.stylesheet':2,
          'javascript': 1
      }
    }
chrome_options.add_experimental_option("prefs",prefs)

fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")

def song(path):
  global filepath
  song = AudioSegment.from_wav(filepath+"\\"+"assets\\"+path)
  play(song)
#重启程序
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
def wbd1():
  bro = wbd1.a
def wbd():
    #get直接返回，不再等待界面加载完成
  #desired_capabilities = DesiredCapabilities.CHROME
  #desired_capabilities["pageLoadStrategy"] = "none"
  # caps["pageLoadStrategy"] = "normal"

  # options = webdriver.ChromeOptions()
  # options.page_load_strategy = 'eager'
  # desired_capabilities = DesiredCapabilities.CHROME
  # desired_capabilities["pageLoadStrategy"] = "none"
  # chrome_options.add_argument('--headless')#无头模式
  webs_driver = ['【1】IE浏览器','【2】谷歌Chrome','【3】旧版Edge']
  for x in range(2):
    print(webs_driver[x])
  wc = int(input('请输入希望使用浏览器对应的序号：'))
  print('你选择的是'+webs_driver[wc-1]+'\n')
  # options = Options()
  # chrome_options = Options()
  # chrome_options.add_argument('--headless')
  # bro = webdriver.Chrome(chrome_options=chrome_options)
  fpath = sys.argv[0]
  fpath = os.path.split(fpath)#获取当前.py文件工作目录
  filepath = fpath[0].replace("/","\\")

  if(wc==1 and wc1==0):
    wbd1.a = webdriver.Ie(executable_path=filepath+r'\各种浏览器驱动\IEDriverServer.exe')
    # print('youtu')
  elif(wc==1 and wc1==1):
    wbd1.a = webdriver.Ie(executable_path=filepath+r'\各种浏览器驱动\IEDriverServer.exe',options = options)
    # print('wutu')
  elif(wc==2 and wc1==0):
    #bro = webdriver.Chrome(filepath+r'\各种浏览器驱动\chromedriver.exe')
    wbd1.a = webdriver.Chrome(executable_path=filepath+r'\各种浏览器驱动\chromedriver.exe')
    print(wc1)
    # print('youtu')
  elif(wc==2 and wc1==1):
    #bro = webdriver.Chrome(filepath+r'\各种浏览器驱动\chromedriver.exe')
    wbd1.a = webdriver.Chrome(executable_path=filepath+r'\各种浏览器驱动\chromedriver.exe',chrome_options=chrome_options)
    print(wc1)
    # print('wutu')

  # else:
  #   wbd1.a = webdriver.Edge(executable_path=filepath+r'\各种浏览器驱动\MicrosoftWebDriver.exe',options = optionse)
  # #PhantomJS(r'D:\HK\python3.82\Scripts\phantomjs-2.1.1-windows\bin\phantomjs.exe')
os.system("cls")
print('建议先在浏览器内打开这几个漫画网站进行漫画的搜索选择，再进行爬取')
webcho = ['【1】百年漫画网: https://www.bnmanhua.com/page/all.html','【2】漫画呗: https://www.manhuadai.com/','【3】古风漫画网: https://www.gufengmh8.com/','【4】动漫之家']
for x in range(3):
  print(webcho[x])
webchoice = int (input('请输入想使用的漫画网站的序号：'))
print('你选择的是'+webcho[webchoice-1]+'\n')
if(webchoice==1):
  pclass="+'.jpg'"
  pclass1="https"
  uclass="https"
  web="(百年漫画)"
elif(webchoice==2):
  pclass="+'.jpg'"
  pclass1="https"
  uclass="https"
  web="(漫画呗)"
  wc1=1
  wbd()
  wbd1()
  bro = wbd1.a
  wbd1.a.set_window_size(400,200)#窗口大小
  wbd1.a.set_window_position(470,0)#位置

elif(webchoice==4):
  pclass="+'.jpg'"
  pclass1="https"
  uclass="https"
  web="(动漫之家)"
  wc1=1
  wbd()
  wbd1()
  wbd1.a.minimize_window()
else:
  pclass="+'.jpg '"
  pclass1="https"
  uclass="https"
  web="(古风漫画)"
  wc1=1
  wbd()
  wbd1()
  wbd1.a.set_window_size(400,200)#窗口大小
  wbd1.a.set_window_position(470,0)#位置


url_bn = "https://www.bnmanhua.com"
url_bn1 = "https://www.bnmanhua.com/search.html"
url_mh1 = 'https://www.manhuadai.com/search/?keywords='
url_dm1 = 'https://www.dmzj.com/dynamic/o_search/index'
url_gf1 = 'https://www.gufengmh8.com/search/?keywords='

headers_bn = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.bnmanhua.com',
    'Referer': 'https://www.bnmanhua.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}

headers_bn1 = {
    'Content-Type': 'text/html; charset=utf-8',
    'Referer': 'https://www.bnmanhua.com/search.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
headers_mh1 = {
    'Referer': 'https://www.manhuadai.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
headers_dm = {
    'Cookie': '__music_index__=2; history=0%7C%E5%96%9C%E6%AC%A2%E7%9A%84; show_tip_1=0; PHPSESSID=5069f828d6ac62762c53b7b910393a38; KLBRSID=7c8f49a0a4b09e102426ab9ef05e7c0a|1595471217|1595471101',
    'Referer': 'https://www.dmzj.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
headers_dm1 = {
    'Cookie': ' __music_index__=2; show_tip_1=0; __music_index__=2; display_mode=1',
    'Referer': 'https://www.dmzj.com/dynamic/o_search/index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
headers_wx = {
    'Cookie': 'click-6780=1; PHPSESSID=0ne608c42rvd6n6s027iu2emmg; _csrf=BlCpgJEFPFc0wbQWnu-vzSIS8m0lmfqa; click-8346=1; popularity-8346=1',
    'Referer': 'https://www.gufengmh8.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}


def remove_file(path):
  if os.path.exists(path):
    shutil.rmtree(path)
  else:print('文件已不存在！')
def remove_list():
  global chapter,names
  for i in range(j):
    rm.append(i)
  # print(rm)
  chapter = [ chapter[i] for i in range(len(chapter)) if (i not in rm)]#按索引删除章节list
  names = [ names[i] for i in range(len(names)) if (i not in rm)]#按索引删除章节list
  # [ names.remove(cElement) for cElement in [names[k] for k in rm]]#按索引删除章节名称list

def create_file(path,msg):#内容写成文本文件
    f=open(path,'a',encoding="utf-8")
    f.write(msg)
    f.close
def create_filewb(path,msg):#图片内容写文件
    f=open(path,'wb')
    f.write(msg)
    f.close
def first_chaperro():#起始章节数报错
  global i,j,chapter,filepath,names,web
  if (j>len(chapter)):
    print('起始章节数输入错误！！,因该漫画收录不全,只收录了从 {}，{}...到 {} 的内容\n(比如网站只收集了123~500话的内容(缺失前123话),而你想爬取200话之后的所有内容,则应该输入200-123=77,即77作为起始章节数输入,而非200。)'.format(chapter[0],chapter[1],chapter[-1]))
    remove_file(filepath+"\\"+names[i-2]+web)
    bro.quit()
    restart_program()
def DownLoad():
  d=0
  global img_path,Path,chapter,hrefs1
  with open(img_path,'r') as f:
    img_srcs=f.read()
  img_srcs = [str(i)for i in img_srcs]
  img_srcs = ''.join(img_srcs)
  img_srcs1 = img_srcs.split("--#--")

  for j in range(len(img_srcs1)-1):
    img_srcs2=[str(i)for i in img_srcs1[j]]
    img_srcs2 = ''.join(img_srcs2).strip().lstrip().rstrip(',')
    img_srcs2 = img_srcs2.replace('\\','')
    img_srcs = img_srcs2.split("https")
    #print(img_srcs)
    print("正在下载 {}：".format(chapter[d]))
    for i in range(len(img_srcs)):
      img_srcs[i]="http"+str(img_srcs[i])
    img_srcs.pop(0)
    #print(img_srcs)
    #print(hrefs1[d])
    os.makedirs(Path+"\\已下载漫画\\"+str(chapter[d]))
    d+=1
    if(d%7==0):time.sleep(4)
    headersimg={
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-dest': 'document',
      'sec-fetch-user': '?1',
      #'Referer': hrefs1[d],
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
    for i in tqdm(range(len(img_srcs)),ascii=True):
      #print(img_srcs[i])
      if(i%10==0):time.sleep(2)
      #print(img_srcs[i])
      res4 = requests.session().get(url=img_srcs[i],headers=headersimg)
      create_filewb(Path+"\\已下载漫画\\"+chapter[d-1]+"\\"+str(i)+'.jpg',res4.content)
  print(" 已下载完成，可以离线看漫画啦！！\n")
  song("下载完成.wav")
def MultiStr_position(mu,zi):
  """查询子字符串在大字符串中的所有位置"""
  len1 = len(zi)
  # pl = []
  # for each in range(len(mu)-len1):  
  #     if mu[each:each+len1] == zi:   #找出与子字符串首字符相同的字符位置
  #         pl.append(each)
  pl = [each for each in range(len(mu)-len1) if mu[each:each+len1] == zi] #列表解析式
  return pl
def Multichapter_select(chap_index,res):#多章节选择
  # chap_index = 'chapter-list-'
  each = res2.find(chap_index)
  position = MultiStr_position(res,chap_index)
  count = len(position)
  id = []
  print('\n')
  for y in range(count):
    print('【{}】'.format(y+1),chapterName[y])
    id.append(res[position[y]:position[y]+16].strip('"! '))
  num = len(id)
  if num >= 1:
    id_select = int(input("有{}种目录，想选择哪一个：".format(count)))-1
  else:
    id_select = 0
  chap_id = [id_select,id]
  return chap_id

name_=input("请输入想看的漫画名称：")
data = {'keyword':name_}
data_dm = {'keywords':name_}
if(webchoice==1):
  r = requests.session()
  res1 = r.post(url=url_bn1,headers=headers_bn,data=data)
  res1 = res1.text
elif(webchoice==2):
  r = requests.session()
  res1 = r.get(url=url_mh1+name_,headers=headers_mh1)
  res1 = res1.text
elif(webchoice==4):
  r = requests.session()
  res1 = r.post(url=url_dm1,headers=headers_dm,data=data_dm)
  res1 = res1.text
else:
  r = requests.session()
  res1 = r.get(url=url_gf1+name_)
  res1 = res1.text
  # create_file(r"C:\Users\HASEE\Desktop\漫画爬虫\gf_res1.html",res1)
  # res1 = wbd1.a.get(url=url_gf1+name_)

names=[]
hrefs=[]
if(webchoice==1):
  soup=BeautifulSoup(res1,'lxml')
  list1=soup.select('#list_img>li')
  for str1 in list1:#获取漫画名字与链接
      names.append(str1.select('li>a>p')[0].get_text())
      hrefs.append(str1.select('li>a')[0]['href'])
elif(webchoice==2):
  soup=BeautifulSoup(res1,'lxml')
  list1 = soup.select('#w0>ul>li')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.select('li>a')[0]['title'])
    hrefs.append(str1.select('li>a')[0]['href'])
  #print(list1)
elif(webchoice==4):
  soup=BeautifulSoup(res1,'lxml')
  list1 = soup.select('div.tab-con>ul>li')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.select('li>a')[0]['title'])
    hrefs.append(str1.select('li>a')[0]['href'])
else:
  # res1 = wbd1.a.page_source
  soup=BeautifulSoup(res1,'lxml')
  list1 = soup.select('#w0>ul>li')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.select('li>a')[0]['title'])
    hrefs.append(str1.select('li>a')[0]['href'])
r.close()#关闭连接

if names:
  for i in range(len(names)):#打印搜索到的漫画列表
      print('【{}】-{}:  {}'.format(i+1,names[i],hrefs[i]))
  print('\n')
else:
  print("\n未搜索到该漫画！！，请换个网站再试试")
  song("报错.wav")
  Q = input("关闭窗口退出或按下回车键继续：")
  if Q=='':
    os.system("cls")
    restart_program()
  wbd1.a.quit()

# list2 = soup.select('#pagination')
# stats=[]
# for str2 in list2:
#     stats.append(str2.get_text())
# print(stats)#输出统计数据

i = int (input('请输入想看漫画的序号：'))
h = hrefs[i-1]
print('你选择的是 {}:{}\n'.format(names[i-1],h))
speed = input("请输入期望爬取速度（默认为0.5，最快为0,建议默认,太快会报错,不输入直接回车则为默认速度）：")
if speed == "":speed = 0.5
else:speed = float(speed)


if(webchoice==1):
  url_bn2 = url_bn+hrefs[i-1]
  res2 = r.get(url=url_bn2,headers=headers_bn1)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  list2=soup1.select('ul.jslist01>li')
elif(webchoice==2):
  h = hrefs[i-1]
  url_mh2 = h
  res2 = r.get(url=url_mh2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  list2=soup1.select('div.zj_list_con>ul>li')
elif(webchoice==4):
  h = 'https:'+hrefs[i-1]
  url_dm2 = h
  res2 = r.get(url=url_dm2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  list2=soup1.select('div.cartoon_online_border>ul>li')
else:
  chapterName=[]
  url_gf2 = h
  chap_index = 'chapter-list-'
  # print(url_gf2)
  res2 = r.get(url=url_gf2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')

  listchap = soup1.select('.caption')
  for strchap in listchap:
    chapterName.append(strchap.select('div>span')[0].get_text())#多章节选择章节名称获取
  # [s.extract() for s in soup1('i')]
  chap_id = Multichapter_select(chap_index,res2)
  id = chap_id[0]
  list2=soup1.select('#'+chap_id[1][id]+'>li')
# print(list2)
chapter=[]
hrefs1=[]
img_src=[]
img_srcs=[]
rm=[]
rm1=[]
j=0
d=0

fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
filepath1 = fpath[0].replace("/","/")
assets_path = filepath+"\\"+names[i-1]+web+"\\assets"#看板娘assets文件目的目录
# shutil.copytree(filepath+"\\assets",assets_path)
Path = filepath+"\\"+names[i-1]+web#漫画保存路径
os.mkdir(Path)#创建所选漫画为名的文件夹
name_path = Path+'\\章节名称.txt'#章节名称文件保存路径
hrefs1_path = Path+'\\章节链接.txt'#章节链接文件保存路径
img_path = Path+'\\漫画地址.txt'#图片地址文件路径
html_path = Path+'\\'+names[i-1]+'.html'#漫画html文件路径



html = """
<!DOCTYPE html>
<html lang="zh-CN">
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="never">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>"""+names[i-1]+"""</title>
    <link rel="icon" type="image/x-icon/" href="../assets/title.png"/>
	<!-- Bootstrap -->
	<link href="../dist/bootstrap-3.3.7-dist/css/bootstrap.min.css" rel="stylesheet">
	
	<!-- HTML5 shim 和 Respond.js 是为了让 IE8 支持 HTML5 元素和媒体查询（media queries）功能 -->
	<!-- 警告：通过 file:// 协议（就是直接将 html 页面拖拽到浏览器中）访问页面时 Respond.js 不起作用 -->
	<!--[if lt IE 9]-->
	  <!--<script src="https://cdn.jsdelivr.net/npm/html5shiv@3.7.3/dist/html5shiv.min.js"></script>-->
	  <!--<script src="https://cdn.jsdelivr.net/npm/respond.js@1.4.2/dest/respond.min.js"></script>-->
	<!--[endif]-->
	
  <style>
		*{
			padding: 0;
			margin: 0;
		}
		#control_1{
			user-select: none;
		}
		#control_2{
			user-select: none;
		}
		#div {
			user-select: none;
		}
		#full_screen{
			position: fixed;
			top: 0.625rem;
			right: 0.625rem;
		}
		#b4 {
		  position: relative;
		  top: 0px;
		  left: 0px;
		}
		.image {
			display: block;
			margin-left: auto;
			margin-right: auto;
		}
		/*菜单*/
/* 		#action{
			position: fixed;
			width: 50px;
			height: 50px;
			background: #fff;
			border-radius: 50%;
			box-shadow: 0 5px 5px rgba(255,255,255,1);
			user-select: none;
		}
		#action > span{
			position: relative;
			width: 100%;
			height: 100% ;
			display: flex;
			justify-content: center;
			align-items: center;
			color: #a13dea;
			font-size: 4em;
			transition: 0.3s ease-in-out ;
		}
		#action.active span{
			transform: rotate(135deg);
		}
		#action.active button{
			transform: rotate(-135deg);
		}
		#action ul{
			position: absolute;
			bottom: 3.4375rem;
			background-color: #fff;
			color: #000000;
			min-width: 15.625rem;
			padding: 1.25rem;
			border-radius: 1.25rem;
			opacity: 0;
			visibility: hidden;
			transform: 0.3s;
			box-shadow: 5px 5px 5px rgba(255,255,255,1);
		}
		#action.active ul{
			bottom: 3.4375rem;
			opacity: 1;
			visibility: visible;
			transform: 0.3s;
		}
		.active.active ul li{
			list-style: none;
			display: flex;
			justify-content: flex-start;
			align-items: center;
			padding: 0.625rem 0;
			transition: 0.3s;
			font-weight: 700;
		}
		#action.active ui li :not(:last-child){
			border-bottom: 0.0625rem solid rgba(0,0,0,1);
		}
		#action ul li button{
			margin-right: 1.875rem;
		}
		#action.active ul li{
			opacity: 0.3;
		}
		#action.active li:hover{
			opacity: 1;
		} */

		/*滑条*/
		#slidera{
			visibility: hidden;
		}
		#slidera.slider{
			position: fixed;
			top: 80px;
			right: 10px;
			visibility: visible;
			
		}
		
		/*阅读模式切换开关*/
		.toggle-button-wrapper{
			visibility: hidden;
		}
		.toggle-button-wrapper.switch{
			position: fixed;
			top: 110px;
			right: 10px;
			visibility: visible;
		}
		#toggle-button{
		            display: none;
		        }
		        .button-label{
		            position: relative;
		            display: inline-block;
		            width: 120px;
		            height: 30px;
		            background-color: #9CCD3F;
		            box-shadow: #ccc 0px 0px 0px 2px;
		            border-radius: 30px;
		            overflow: hidden;
		        }
		.circle{
		position: absolute;
		top: 0;
		 left: 0;
		 width: 30px;
		height: 30px;
		border-radius: 50%;
		background-color: #fff;
		}
		.button-label .text {
		line-height: 30px;
		font-size: 18px;
		text-shadow: 0 0 2px #ddd;
		}
		.on {
		color: #fff;
		display: none; 
		text-indent: 10px;
		user-select: none;
		}
		.off { 
		 color: #fff;
		display: inline-block;
		text-indent: 34px;
		user-select: none;
		}
		.button-label .circle{
		left: 0;
		transition: all 0.3s;
		}
		#toggle-button:checked + label.button-label .circle{
		left: 90px;
		}
		#toggle-button:checked + label.button-label .on{ display: inline-block; }
		#toggle-button:checked + label.button-label .off{ display: none; }
		#toggle-button:checked + label.button-label{
		background-color: #2CA2F9;
		}
  </style>

  </head>
  <body id="body" class="mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-auto mdui-appbar-with-toolbar" data-status="click" style="zoom: 1;">
    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
	<script src="../dist/bootstrap-3.3.7-dist/js/jquery.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="../dist/bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
	<script src="../dist/bootstrap-3.3.7-dist/js/bootstrap-slider.min.js"></script>
	<script type="text/javascript" src="../dist/bootstrap-3.3.7-dist/js/buttons.js"></script>
	<script src="../dist/mdui-v1.0.1/js/mdui.min.js"></script>
	<script id="l2d"></script>
	<!-- <link rel="stylesheet" type="text/css" href="dist/fontawesome-free-5.15.1-web/css/fontawesome.min.css"/> -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome/css/font-awesome.min.css">
	<link rel="stylesheet" type="text/css" href="../dist/bootstrap-3.3.7-dist/css/buttons.min.css"/>
	<link rel="stylesheet" type="text/css" href="../dist/mdui-v1.0.1/css/mdui.min.css"/>
	<link rel="stylesheet" type="text/css" href="../dist/bootstrap-3.3.7-dist/css/bootstrap-slider.min.css"/>
	
		<!-- 应用栏 -->
		<header class="mdui-appbar mdui-appbar-scroll-hide mdui-appbar-fixed">
		  <div class="mdui-toolbar mdui-color-theme">
			<span id="toggle" mdui-tooltip="{content: '目录'}" class="mdui-btn mdui-btn-icon mdui-ripple mdui-ripple-white" mdui-drawer="{target: '#main-drawer', swipe: true}"><i class="mdui-icon material-icons">menu</i></span>
			<span class="mdui-typo-title">"""+names[i-1]+"""</span>
			<div class="mdui-toolbar-spacer"></div>
			<!-- <a href="javascript:;" class="mdui-btn mdui-btn-icon"><i class="mdui-icon material-icons">search</i></a> -->
			<a href="javascript:;" class="mdui-btn mdui-btn-icon" mdui-tooltip="{content: '切换日间/夜间模式'}" id="tgns"><i class="mdui-icon material-icons">brightness_4</i></a>
			<span onclick="theme_auto()" class="mdui-btn mdui-btn-icon mdui-ripple mdui-ripple-white" mdui-dialog="{target: '#dialog-docs-theme'}" mdui-tooltip="{content: '设置主题跟随系统'}"><i class="mdui-icon material-icons">brightness_auto</i></span>
			<a href="javascript:;" mdui-tooltip="{content: '全屏'}" onclick="fullClick()" class="mdui-btn mdui-btn-icon mdui-ripple"><i class="mdui-icon material-icons">fullscreen</i></a>
		  </div>
		</header>
		<!-- 侧边目录 -->
		<div class="mdui-drawer mdui-drawer-close mdui-appbar-with-toolbar" id="drawer">
			<ul class="mdui-list" id="drawer_ul">
			</ul>
		</div>

	<!--文件读取-->
	<!-- <div id="files" style="display: block; float: left;"> -->
	<form id="files" class="form-inline" role="form">
		<div class="form-group">
			<label for="chapters_hreff">选择漫画地址文件:</label>
			<input type="file" id="chapters_hreff">
			<label for="chap_name">选择章节名称文件:</label>
			<input type="file" id="chap_name">
			<p class="help-block">选择好两个文件后点击右边按钮两下读取文件</p>
		</div>
		<button mdui-tooltip="{content: '读取全部文件'}" data-placement="auto" data-toggle="tooltip" type="button" class="button button-glow button-box button-caution button-giant" id="b4" /><span class="glyphicon glyphicon-play"></span></button>
	</form>

	<!-- 滑条 -->
	<div class="hidden-xs" id="slidera">
		<input id="slider1" type="text" data-slider-max="1077" data-slider-min="217" data-slider-step="1" data-slider-value="677"/>
	</div>
	<div class="visible-xs" id="slidera">
		<input id="slider1" type="text" data-slider-max="1077" data-slider-min="217" data-slider-step="1" data-slider-value="348"/>
	</div>

	<div class="col-md-offset-4 col-lg-offset-4col-xl-offset-4">
		<input type="text" style="visibility:hidden;" id="001" value="" >
		<input type="text" style="visibility:hidden;" id="002" value="" >
	</div>
	<h2 id="chap_names" align="center">章节名称：</h2>

	<form id="control_1">
		<div class="form-group col-md-offset-4 col-lg-offset-4col-xl-offset-4">
			<label for="sumchaps" class="form-inline"/>
				总共<input type="text" id="sumchaps" style="width: 60px;" class="form-control" placeholder="??">章
			</label>
			<label for="chaps" class="form-inline" />
				当前第<input data-toggle="tooltip" mdui-tooltip="{content: '在这输入要跳转的章节后点击跳转'}" type="text" id="chaps" style="width: 60px;" class="form-control" placeholder="1">章
			</label>
			<button data-toggle="tooltip" type="button" onclick=pre() mdui-tooltip="{content: '上一章'}" class='button button-3d button-pill button-action button-small'><span class="glyphicon glyphicon-chevron-left"></span></button>
			<button data-toggle="tooltip" type="button" onclick=Goto();show();topFunction() mdui-tooltip="{content: '跳转'}" id='bt' class="class='button button-raised button-circle button-action"><span class="glyphicon glyphicon-ok"></span></button>
			<button data-toggle="tooltip" type="button" onclick=next() mdui-tooltip="{content: '下一章'}" class='button button-3d button-pill button-action button-small'><span class="glyphicon glyphicon-chevron-right"></span></button>
		</div>
	</form>
	
	<!--漫画图片-->
	<div align="center" id="div"></div>
    <div align="center">
	  <i id='the_over' style='visibility:hidden'>漫画加载中......</i>
	</div>

	<!-- 菜单 -->
<!-- 	<div id="action" style="bottom: 2%;left: 2%;" onclick="actionToggle()"> 
		<span data-placement="right" data-toggle="tooltip" title="菜单">+</span> 
		<ul>
		<li><button data-toggle="tooltip" onclick="action_switch()" class="button button-3d button-box button-large button-inverse"><span class="glyphicon glyphicon-cloud-download"></span></button>(切换阅读方式)</li>
		<li><button data-toggle="tooltip" onclick="action_slider()" class="button button-3d button-box button-large button-primary"><span class="glyphicon glyphicon-wrench"></span></button>(调整漫画尺寸)</li>
		<li><button data-toggle="tooltip" class="button button-3d button-box button-large button-highlight" onclick=downloadFile('鬼灭之刃',"你看到了第"+document.getElementById('chaps').value+"章__"+Date()) id='history'><span class="glyphicon glyphicon-floppy-disk"></span></button>(保存历史记录)</li>
		</ul>
	</div> -->
	<div id="action"></div>
	<div class="mdui-fab-wrapper" id="fab1">
		<button class="mdui-fab mdui-ripple mdui-color-pink-accent">
		  <i class="mdui-icon material-icons">add</i>
		  <i class="mdui-icon mdui-fab-opened material-icons">mode_edit</i>
		</button>
		<div class="mdui-fab-dial">
		  <button mdui-tooltip="{content: '保存阅读记录'}" onclick=downloadFile('"""+names[i-1]+"""',"你看到了第"+document.getElementById('chaps').value+"章__"+Date()) id='history' class="mdui-fab mdui-fab-mini mdui-ripple mdui-color-pink"><i class="mdui-icon material-icons">save</i>
		  </button>
		  <button onclick="action_switch()" mdui-tooltip="{content: '切换阅读模式(本地/在线)'}" class="mdui-fab mdui-fab-mini mdui-ripple mdui-color-red"><i class="mdui-icon material-icons">cloud</i>
		  </button>
		  <button onclick="action_slider()" mdui-tooltip="{content: '调整漫画尺寸'}" class="mdui-fab mdui-fab-mini mdui-ripple mdui-color-orange"><i class="mdui-icon material-icons">build</i>
		  </button>
		  <button onclick="topFunction()" mdui-tooltip="{content: '到顶部'}" class="mdui-fab mdui-fab-mini mdui-ripple mdui-color-blue"><i class="mdui-icon material-icons">vertical_align_top</i>
		  </button>
		</div>
	</div>

	<!--切换开关-->
	<div class="toggle-button-wrapper">
	    <!-- 注意：label的for属性 要与其对应的input的id相对应 -->
	    <input type="checkbox" id="toggle-button" name="switch">
	    <label for="toggle-button" class="button-label">
	        <span class="circle" id="load"></span>
	        <span class="text on" onclick="switchto_online()">本地模式</span>
	        <span class="text off" onclick="switchto_local()">在线观看</span>
	    </label>
	</div>

	<form id="control_2">
		<div class="form-group col-md-offset-4 col-lg-offset-4col-xl-offset-4">
			<label for="sumchaps" class="form-inline"/>
				总共<input type="text" id="sumchaps" style="width: 60px;" class="form-control" placeholder="??">章
			</label>
			<label for="chaps" class="form-inline" />
				当前第<input type="text" id="chaps1" style="width: 60px;" class="form-control" placeholder="1">章
			</label>
			<button data-toggle="tooltip" type="button" onclick=pre() mdui-tooltip="{content: '上一章'}" class='button button-3d button-pill button-action button-small'><span class="glyphicon glyphicon-chevron-left"></span></button>
			<button data-toggle="tooltip" type="button" onclick=Goto();show();topFunction() mdui-tooltip="{content: '跳转'}" id='bt' class="class='button button-raised button-circle button-action"><span class="glyphicon glyphicon-ok"></span></button>
			<button data-toggle="tooltip" type="button" onclick=next() mdui-tooltip="{content: '下一章'}" class='button button-3d button-pill button-action button-small'><span class="glyphicon glyphicon-chevron-right"></span></button>
		</div>
	</form>
	<!-- 进度指示器 -->
	<div class="mdui-container mdui-p-b-0" style="position: fixed;bottom: 2px;">
	  <div class="mdui-progress">
	    <div id="steps" class="mdui-progress-determinate" style="width: 1%;"></div>
	  </div>
	</div>

  <script>
		var wait = false
		var wait1 = false
		var tem = ''
		var tem1 = ''
		var y = 1
		var count = 3
		var uclass = '"""+uclass+"""'
		var Uclass = uclass
		var wait_t = 1;

		if(navigator.userAgent.match(/(iPhone|iPod|Android|ios)/i)){//设定漫画默认尺寸和菜单位置
			var wid = wid1 = 348
		}else {
			live2d = document.getElementById("l2d")
			live2d.setAttribute("type", "text/javascript");
			live2d.setAttribute("src","../dist/live2d-widget-0.8.3/autoload.js")
			// more = document.getElementById("action")
			// more.setAttribute("style","bottom: 350px;left: 2%;")
			var wid = wid1 = 677
		}
		// 菜单悬浮球
		var inst_fab = new mdui.Fab('#fab1');
		// 应用栏
		var body = document.getElementById('body');
		document.getElementById('tgns').onclick = function(){
		    if (body.dataset.status == 'click'){
				body.dataset.status=''
		        body.className = 'mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-dark mdui-appbar-with-toolbar';
			    }
				else{
				console.log(body.dataset.status)
		        body.dataset.status='click';
				body.className = 'mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-white mdui-appbar-with-toolbar';
		    }
		}
		function theme_auto(){
			document.getElementById('body').setAttribute('class','mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-auto mdui-appbar-with-toolbar');
		}
		// 读文件
        document.getElementById('b4').addEventListener('click',function(){
            wait = true;
            if(wait){
				
				img_url = document.getElementById('001');
				s = img_url.value.toLocaleString();
				chap = s.split(",");
				pages = new Array();
				
				chap_name = document.getElementById('002')
				s1 = chap_name.value.toLocaleString();
				chap_name = s1.split(",");
				chaplen = chap.length;//获取到章节总数
				document.getElementById('sumchaps').value = chaplen-1;
				
				for(i=0;i<chaplen;i++){
				page = chap[i].toLocaleString();
				page = page.split('https');
				pagelen = page.length;
				pages[i]=pagelen//每章节页数
				}
				img_url=s.replace(/,/g,'');
				img_url=img_url.split('https');//获取到每页漫画图片地址
				img_url.push(img_url[0]);
				img_url.splice(0,1);
				URL = img_url

				
				img_url_loc = new Array();
				k=0;
				for(i=0;i<(chaplen-1);i++){
					//console.log(i);
					//console.log(pages[i]);
					for(j=0;j<pages[i]-1;j++){
						img_url_loc[k]="已下载漫画\\\\"+chap_name[i]+"\\\\"+j+".jpg";
						//console.log(img_url_loc[k]);
						k++;
					}
				}
				Uclass = uclass;
				URL = img_url;
				wait2 = true
		//懒加载
        document.getElementById('the_over').setAttribute('style','visible');

				//var unloaded = pages[y-1]-3; /*标记还有多少个图片没有加载*/
				window.onscroll = function() {
                //滚动条顶部到浏览器窗口顶部的距离，这里为什么要判断，是因为浏览器的兼容性问题
                scrollTop = (document.documentElement.scrollTop == 0 ? document.body.scrollTop : document.documentElement.scrollTop);
                //当滚动条滚动的距离 + 浏览器可视窗口大小 + wid/2 >= 图片元素的高度时加载
					if (scrollTop + document.documentElement.clientHeight + (wid1/2)*(wid1/wid) > image[count].offsetTop) {
					              console.log('此时count为:'+count);
								  // 进度指示器
								  document.getElementById('steps').setAttribute('style','width:'+ 100*(count/(pages[y-1]-2)) +'%;');
                        image[count].setAttribute('src', image[count].getAttribute('src-data'));
                        count++;
                        if(count+1==pages[y-1]){
                        document.getElementById('the_over').innerHTML='本章节已结束';
                      }
                        //console.log(count+' '+i);
					//if(pages[y-1]%2!=0) image[pages[y-1]-1].setAttribute('src', image[pages[y-1]-1].getAttribute('src-data'));
				}
				}
				

        	}
			
        })
		function hide(){
			document.getElementById("files").style.display = "none"
		}
		//菜单
		function actionToggle(){
			var action = document.querySelector('#action');
			action.classList.toggle('active')
		}
		//滑条调整漫画宽度
		function action_slider(){
			var action = document.querySelector('#slidera');
			action.classList.toggle('slider')
		}
		var slider = new Slider("#slider1", {
			reversed : true
		});
		slider.on("change", function(sliderValue) {
			console.log(sliderValue.newValue)
			wid = sliderValue.newValue
			for(var i=0;i<pages[y-1]-1;i++)
			image[i].setAttribute('style','width:'+wid+'px');
		});
		
		//切换开关
		function action_switch(){
			var action = document.querySelector('.toggle-button-wrapper');
			action.classList.toggle('switch')
		}
		btn = document.getElementById("load");
			t = true;
			btn.onclick = function dian() {
			if (t) {
				Uclass = '';
				URL = img_url_loc;
			}
			else {
				Uclass = uclass;
				URL = img_url;
			}
			t = !t;
		}
		function switchto_online(){
			Uclass = uclass;
			URL = img_url;
		}
		function switchto_local(){
			Uclass = '';
			URL = img_url_loc;
		}

		//拖拽效果
		// $('#action').mousedown(function(e) {
		//     // e.pageX
		//     var positionDiv = $(this).offset();
		//     var distenceX = e.pageX - positionDiv.left;
		//     var distenceY = e.pageY - positionDiv.top;
		//     //alert(distenceX)
		//     // alert(positionDiv.left);
		
		// $(document).mousemove(function(e) {
		// 	var x = e.pageX - distenceX;
		// 	var y = e.pageY - distenceY;
		// 		if (x < 0) {
		// 		x = 0;
		// 	} 
		// 	else if (x > $(document).width() - $('#action').outerWidth(true)) {
		// 		x = $(document).width() - $('#action').outerWidth(true);
		// 	}
		// 	if (y < 0) {
		// 		y = 0;
		// 	} 
		// 	else if (y > $(document).height() - $('#action').outerHeight(true)) {
		// 		y = $(document).height() - $('#action').outerHeight(true);
		// 	}
		// 	$('#action').css({
		// 		'left': x + 'px',
		// 		'top': y + 'px'
		// 		});
		// 	});
		// 	$(document).mouseup(function() {
		// 	$(document).off('mousemove');
		// 		});
		// 	});


		document.getElementById('b4').addEventListener('click',function(){
            wait = true
            if(wait){
				readAsText_img('chapters_href','chapters_hreff');
				readAsText_name('chapters_name','chap_name');
        	}
        })

		function firstone(){//每次初始先加载三张图片
			for(var i=0;i<3;i++){
				image = document.getElementsByClassName('image');
				image[i].setAttribute('src', image[i].getAttribute('src-data'));
				}
            }

    function readAsText_img(tem,id){
        var file = document.getElementById(id).files[0];
        var reader = new FileReader();//将文件以文本形式读入页面
        reader.readAsText(file)
        reader.onload = function(f){
        var jsArr = JSON.stringify(this.result);//对象转字符串
        var tem = jsArr.replace(/"/g,'');//删‘”’
        var tem = tem.split("--#--");//分割并且字符串转为数组
        inserts = document.getElementById('001').value = tem;
        if(wait1)
        for(num=0;num<pages[0]-1;num++){
          createimg(num);
		  hide();
        }
			wait1=true;
			image = document.getElementsByClassName('image');
			for(var i=0;i<3;i++){
				image[i].setAttribute('src', image[i].getAttribute('src-data'));
				}
            }
			return tem;
        }
		function readAsText_name(tem,id){
            var file = document.getElementById(id).files[0];
            var reader = new FileReader();//将文件以文本形式读入页面
            reader.readAsText(file)
            reader.onload = function(f){
            var jsArr = JSON.stringify(this.result);//对象转字符串
            var tem = jsArr.replace(/"/g,'');//删‘”’
			var tem = tem.split("--#--");//分割并且字符串转为数组
			document.getElementById('002').value = tem;
			
            }
			return tem;
        }

		function errornotice(){
			
			
		}
		
		var widths = document.getElementsByClassName('image');

    function image_error(image){
		  image.src="../assets/heart-broken.svg"
    }

		function createimg(n){
			var img = document.createElement('img');
			img.setAttribute('src-data',Uclass+URL[n]);
			img.setAttribute('src','bao cuo ba hahaha');
			img.setAttribute('class','image');
      img.setAttribute('onerror','image_error(this)');
			img.setAttribute('alt','图片错误');
			img.setAttribute('style','display: block;height: auto;width:'+wid+'px');
			img.id = n;
			var div = document.getElementById('div');
			div.appendChild(img);
		}
		var sum = 0
		function add_pre(n){
			if(n>=1){
				var n=n-1
				sum = sum - pages[n]+1}
			else sum = 0
			return sum
		}
		function add_next(n){
			if(n>=1){
				var n=n-1
				sum+=(pages[n-1]-1)}
			else sum = 0
			return sum
		}
		function add_go(n){
			if(n>=1){
				var n=n-1
				sum = 0
				for(i=0;i<n;i++){sum+=pages[i]-1;}
				}
			else sum = 0
			return sum
		}
		function listimg_pre(n){
			console.log(n);
			for(num=0;num<pages[n-1]-1;num++){
				createimg(sum+num);
			}
		}
		function listimg_next(n){
			console.log(n);
			for(num=0;num<pages[n-1]-1;num++){
				createimg(sum+num);
			}
		}
		
		function removeimg_pre(n){
			console.log(sum);
			if(sum>=0){
			var div1 = document.getElementById("div");
			for(i=sum+pages[n]-1;i<sum+pages[n]+pages[n+1]-2;i++){
				console.log(i)
				document.getElementById(i).remove();
				}
			}
		}
		function removeimg_next(n){
			console.log(sum);
			if(sum>0){
			var div1 = document.getElementById("div");
			for(i=sum-pages[n-1]+1;i<sum;i++){
				console.log(i)
				document.getElementById(i).remove();
				}
			}
		}
		function next(){if(y<chaplen-1){cnext();firstone();show();topFunction()}}
		function pre(){if(y>=2){cpre();firstone();show();topFunction()}}
		function cnext(){y++;add_next(y);listimg_next(y);removeimg_next(y-1);firstone();count=3;document.getElementById('the_over').innerHTML='漫画加载中......';}
		function cpre() {y--;add_pre(y);listimg_pre(y);removeimg_pre(y-1);firstone();count=3;document.getElementById('the_over').innerHTML='漫画加载中......';}
		function show(){y;document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];catalog = document.getElementById("catalog"+(y-1));catalog.setAttribute("class","mdui-color-grey mdui-shadow-6 mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2");}
		function Goto(){count=3;y = document.getElementById('chaps').value;add_go(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();}
		function Goto1(){count=3;y = document.getElementById('chaps1').value;add_go(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();}
		function topFunction() {
			document.body.scrollTop = 0;
			document.documentElement.scrollTop = 0;
		}
		
		// 目录
		var inst_drawer = new mdui.Drawer('#drawer');
		document.getElementById('toggle').addEventListener('click', function () {
			inst_drawer.toggle();
			if(wait_t == 1){
				for(c=0;c<chaplen-1;c++){
					catalogCreate(c);//生成目录
				}
			}
			wait_t=2;
		});
		function cashow(y){document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];catalog = document.getElementById("catalog"+(y-1));catalog.setAttribute("class","mdui-color-grey mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2");}
		function catalogCreate(n){
				var a = document.createElement('a')
				a.setAttribute("onclick","catalogGoto("+ (n+1) +")")
				a.setAttribute("class","mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2")
				a.id = "catalog"+n
				var drawer_ul = document.getElementById('drawer_ul')
				drawer_ul.appendChild(a)
				document.getElementById("catalog"+n).innerHTML=chap_name[n];
			}
		function catalogGoto(y){cashow(y);topFunction();Goto()}

		document.onkeydown = function(event){//键盘事件左右键控制翻章节
			var e=event || window.event;
			if(e&&e.keyCode == 37){if(y>=2){cpre();show();topFunction()}}
			else if(e&&e.keyCode == 39){if(y<chaplen-1){cnext();show();topFunction()}}
		}
		
function fullClick(){
   	//全屏
	var el = window.parent.document.documentElement;
    var rfs = el.requestFullScreen || el.webkitRequestFullScreen || el.mozRequestFullScreen || el.msRequestFullscreen;      
    if(typeof rfs != "undefined" && rfs) {
        rfs.call(el);
    };
    
    //退出全屏
    var el2 = window.parent.document;
    if (el2.exitFullscreen) {  
        el2.exitFullscreen();  
    }  
    else if (el2.mozCancelFullScreen) {  
        el2.mozCancelFullScreen();  
    }  
    else if (el2.webkitCancelFullScreen) {  
        el2.webkitCancelFullScreen();  
    }  
    else if (el2.msExitFullscreen) {  
        el2.msExitFullscreen();  
    } 
    if(typeof cfs != "undefined" && cfs) {
        cfs.call(el);
    }
    return false;
}

var path = window.location.href;
var path = decodeURI(path).replace(/com.html/g,"");

    function downloadFile(filename,text) {//保存阅读历史
        var pom = document.createElement("a");
        pom.setAttribute(
            "href",
            "data:text/plain;charset=utf-8," + encodeURIComponent(text)
          );
          pom.setAttribute("download", filename);
          if (document.createEvent) {
            var event = document.createEvent("MouseEvents");
            event.initEvent("click", true, true);
            pom.dispatchEvent(event);
          } else {
            pom.click();
          }
    }
  </script>
  </body>
</html>
"""

create_file(html_path,"{}".format(html))#漫画html写入txt文件

if(webchoice==1):
  for str2 in list2:#获取漫画章节链接
      chapter.append(str2.select('li>a')[0].get_text())
      hrefs1.append(str2.select('li>a')[0]['href'])
  for j in range(len(hrefs1)):
    hrefs1[j] = "https://www.bnmanhua.com"+str(hrefs1[j])
  chapter.reverse()
  first_chaperro()
elif(webchoice==2):
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>a')[0]['title'])
    hrefs1.append(str2.select('li>a')[0]['href'])
  first_chaperro()
  # for i in range(j):
  #   rm.append(i)
  # [ hrefs1.remove(cElement) for cElement in [hrefs1[i] for i in rm]]#按索引删除章节list
elif(webchoice==4):
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>a')[0]['title'])
    hrefs1.append(str2.select('li>a')[0]['href'])
else:
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>a>span')[0].get_text())
    hrefs1.append(str2.select('li>a')[0]['href'])
  first_chaperro()
# print(i,len(chapter),names)
print("\n {} 总共有 {} 话".format(names[i-1],len(chapter)))
upgrage = (input('爬取起始章节数 就是你想从第几话开始爬取\n输入爬取的起始章节数(直接回车从第一话开始爬取):'))
if upgrage=="":j=upgrage=0
else:
  upgrage = int(upgrage)-1
  j = upgrage
remove_list()

ifdownload = (input('是否将漫画下载到本地观看(输入1代表是，或直接回车否)：')) 
if ifdownload=="":ifdownload=0
else:ifdownload = int(ifdownload)

print("\n漫画相关文件保存在：")
print(html_path)
print(img_path)
print(name_path)
print('\n')

try:
    with tqdm(range(len(chapter)),ascii=True) as t:
        for k in t:
            create_file(name_path,"{}".format(chapter[k]+"--#--"))#章节目录名称写入txt文件
            #create_file(hrefs1_path,"{}".format('https://www.manhuadai.com'+hrefs1[k+j]+"--#--"))#章节链接写入txt文件
except KeyboardInterrupt:
    t.close()
    raise
t.close()

if(webchoice==1):
  i=0
  j=len(chapter)
  for x in tqdm(range(len(chapter)),ascii=True):
      url_bn3=hrefs1[j-1]
      if i==0:
          url_bn4 = h
      else:
          url_bn4 = hrefs1[j]
      headers2 = {
          'Host': 'www.bnmanhua.com',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate',
          'Referer': url_bn4,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}

      #print("第几话网址：",url_bn3)
      i+=1
      j-=1
      
      res3 = r.get(url_bn3,headers=headers2)
      res3 = res3.text
      
      soup2 = BeautifulSoup(res3,'lxml')
      img_begin = res3.find('z_img')
      img_end = res3.find('.jpg"]')
      
      img_src = res3[img_begin+9:img_end+4]
      img_src = img_src.split('","')
      for i in range(len(img_src)):
        img_src[i]="https://img.yaoyaoliao.com/"+img_src[i]
      
      img_src=[str(i) for i in img_src]
      img_src=''.join(img_src)
      create_file(img_path,img_src+'--#--')#保存漫画图片地址
      if j%13==0:time.sleep(12*speed)
      time.sleep(speed)
      if img_src:continue
      else:break
  r.close()#关闭连接

elif(webchoice==2):
  image_src=[]
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
    url_mh3 = 'https://www.manhuadai.com'+hrefs1[j]
    if j==0:
        url_mh4 = h
    else:
        url_mh4 = 'https://www.manhuadai.com'+hrefs1[j-1]
    headers2 = {
        'Referer': url_mh4,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}

    try:
        res3 = bro.get(url_mh3)
        bro.set_script_timeout(8)
        bro.set_page_load_timeout(8)
    except Exception:
        ActionChains(bro).send_keys(Keys.ESCAPE).perform()
    # res3 = bro.get(url_mh3)
    js3 = """
    var url = chapterImages;
    return url;
    """
    images = bro.execute_script(js3)
    while True:
      if images:
        ActionChains(bro).send_keys(Keys.ESCAPE).perform()
        # print('停了')
        break
      else:
        time.sleep(0.5)
        images = bro.execute_script(js3)
        continue
    res3 = bro.page_source
    soup2 = BeautifulSoup(res3,'lxml')
    list3 = soup2.select('div.comic_wraCon>div>img')
    # print(type(image_src))
    # print(hrefs1[j-1])
    for str3 in list3:
      image_src.append(str3['src'])
    # print(j)
    # print(type(image_src))
    # print(image_src)
    image_src=[str(i) for i in image_src]
    image_src=''.join(image_src)
    image_src=urllib.parse.unquote(image_src)
    #print(image_src)
    if images:
      # print('tiaoe!!!')
      position = image_src.find(images[0])
      #print(position)
      if position!=-1:
        image_src = image_src[0:position]
        i = 0
        for g in range(len(images)):
          img_src.append(image_src+images[i])
          i+=1
    else:
      img_src.append('https://img01.eshanyao.com/images/default/common.png')
      # print('tiao chu le!!!')
    
    for i in range(len(images)):
      images[i]="https://img01.eshanyao.com/showImage.php?url="+str(images[i])
    #print(images)
    images = []

    #print(img_src)
    img_src=[str(i) for i in img_src]
    img_src=''.join(img_src)
    #print(img_src)
    create_file(img_path,img_src+'--#--')#保存漫画图片地址
    if j%7==0:time.sleep(20*speed)
    j+=1
    if(j<len(chapter)+upgrage):
      img_src = []
      image_src = []
    #bro.execute_script('window.stop()')
  bro.quit()

elif(webchoice==4):
  bro = wbd1.a
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
      url_dm3 = ' https://manhua.dmzj.com'+hrefs1[j]
      if j==0:
          url_dm4 = h
      else:
          url_dm4 = ' https://manhua.dmzj.com'+hrefs1[j-1]
      headers2 = {
          'Referer': url_dm4,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45',
          'CooKie': 'display_mode=0'}      
      # print(url_dm3)
      # print(url_dm4)
      try:
        res3 = bro.get(url_dm3)
        bro.set_script_timeout(13)
        bro.set_page_load_timeout(13)
      except Exception:
        ActionChains(bro).send_keys(Keys.ESCAPE).perform()
      js='document.documentElement.scrollTop=26000'
      bro.execute_script(js)
      time.sleep(speed+0.2)
      res3 = bro.page_source
      soup2 = BeautifulSoup(res3,'lxml')
      list3 = soup2.select('div.btmBtnBox>select>option')
      for str3 in list3:
          img_src.append('https:'+str3['value'])
      img_src=[str(i) for i in img_src]
      img_src=''.join(img_src)
      # if(j==len(chapter)):
      #   check()
      create_file(img_path,img_src+'--#--')#保存漫画图片地址
      time.sleep(speed)
      j+=1
      if(j<len(chapter)):img_src = []
  bro.quit()
else:
  bro = wbd1.a
  image_src=[]
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
    url_gf3 = 'https://www.gufengmh8.com'+hrefs1[j]

    # try:
    #     res3 = bro.get(url_gf3)
    #     bro.set_script_timeout(4)
    #     bro.set_page_load_timeout(4)
    # except Exception:
    #     ActionChains(bro).send_keys(Keys.ESCAPE).perform()
    res3 = bro.get(url_gf3)
    js3 = """
    var url = chapterImages;
    return url;
    """
    images = bro.execute_script(js3)
    while True:
      if images:
        ActionChains(bro).send_keys(Keys.ESCAPE).perform()
        # print('停了')
        break
      else:
        time.sleep(0.5)
        images = bro.execute_script(js3)
        continue
    # images = str(images[0])
    # images = images.replace('\\','')
    res3 = bro.page_source
    soup2 = BeautifulSoup(res3,'lxml')
    list3 = soup2.select('#images>img')
    for str3 in list3:
      image_src.append(str3['src'])
    image_src=str(image_src[0])
    # print(image_src)
    # print(images)
    
    if images:
      # print('tiaoe!!!')
      position = image_src.find(images[0])
      # print(position)
      if position!=-1:
        image_src = image_src[0:position]
        i = 0
        for g in range(len(images)):
          img_src.append(image_src+images[i])
          i+=1
    else:
      img_src.append('https://img01.eshanyao.com/images/default/common.png')

    img_src = [str(i) for i in img_src]
    img_src=''.join(img_src)
    create_file(img_path,img_src+'--#--')#保存漫画图片地址
    # img_src = list(img_src)
    j+=1
    if j%7==0:time.sleep(12*speed)
    if(j<len(chapter)+upgrage):
      img_src = []
      image_src = []
  bro.quit()
if img_src:
  print(" 已成功爬取完毕！可以在线看漫画啦!\n")
  song("爬取完成.wav")
  if (ifdownload==1):
    DownLoad()
  Q = input("关闭窗口退出或按下回车键继续：")
  if Q=='':
    os.system("cls")
    restart_program()
else:
  print(Path)
  remove_file(Path)
  print("\n爬取失败！！\n该漫画无法观看，可到爬取的网站搜索该漫画查看原因，或换个网站再试试")
  song("报错.wav")
  Q = input("关闭窗口退出或按下回车键继续：")
  if Q=='': restart_program()
#os.system('pause')