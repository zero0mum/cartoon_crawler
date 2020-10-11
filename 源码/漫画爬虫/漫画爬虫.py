import requests,time,os,shutil,sys,shutil,urllib
from pydub import AudioSegment
from pydub.playback import play
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.options import Options
# from selenium.webdriver.chrome.options import Options
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
  #print(filepath+"\\"+"assets\\"+path)
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
webcho = ['【1】百年漫画网: https://www.bnmanhua.com/','【2】漫画呗: https://www.manhuabei.com/','【3】古风漫画网: https://www.gufengmh8.com/','【4】动漫之家']
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
url_mh1 = 'https://www.manhuabei.com/search/?keywords='
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
    'Referer': 'https://www.manhuabei.com/',
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
  if (j<len(chapter)):
    for i in range(j):
      rm.append(i)
    [ chapter.remove(cElement) for cElement in [chapter[i] for i in rm]]#按索引删除章节list
  else:
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
  url_gf2 = h
  # print(url_gf2)
  res2 = r.get(url=url_gf2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  # [s.extract() for s in soup1('i')]
  list2=soup1.select('#chapter-list-1>li')
# print(list2)
chapter=[]
hrefs1=[]
img_src=[]
img_srcs=[]
rm=[]
rm1=[]
j=0
d=0
upgrage = (input('爬取起始章节数 就是你想从第几话开始爬取\n输入爬取的起始章节数(直接回车从第一话开始爬取):'))
if upgrage=="":j=upgrage=0
else:
  upgrage = int(upgrage)-1
  j = upgrage = upgrage-1

ifdownload = (input('是否将漫画下载到本地观看(输入1代表是，或直接回车否)：')) 
if ifdownload=="":ifdownload=0
else:ifdownload = int(ifdownload)

fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
filepath1 = fpath[0].replace("/","/")
assets_path = filepath+"\\"+names[i-1]+web+"\\assets"#看板娘assets文件目的目录
shutil.copytree(filepath+"\\assets",assets_path)
#os.mkdir(fpath[0]+r"/"+names[i-1])#创建所选漫画为名的文件夹
Path = filepath+"\\"+names[i-1]+web#漫画保存路径
name_path = Path+'\\章节名称.txt'#章节名称文件保存路径
hrefs1_path = Path+'\\章节链接.txt'#章节链接文件保存路径
img_path = Path+'\\漫画地址.txt'#图片地址文件路径
html_path = Path+'\\'+names[i-1]+'.html'#漫画html文件路径



html = """
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="referrer" content="never">
    <title>"""+names[i-1]+"""</title>
	<link rel="stylesheet" type="text/css" href="assets/waifu.min.css?v=1.4.2"/>
	<style>
#load {
  position: fixed;
  left: 18px;
  width: 140px;
  height: 30px;
  top: 140px;
  background-color: #555;
  color: white;
  font-weight: bold;
  cursor: pointer;
  display: block;
  border: none;
  outline: none;
  border-radius: 15px;
  box-shadow: 5px 5px 3px #F8F8F8;
}
#load:hover {
  background-color: red;
}

#myBtn {
  display: none;
  position: fixed;
  bottom: 20px;
  right: 30px;
  z-index: 99;
  border: none;
  outline: none;
  background-color: red;
  color: white;
  font-weight: bold;
  cursor: pointer;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 5px 5px 3px #F8F8F8;
}

#myBtn:hover {
  background-color: #555;
}

.nav .nav-icon {
  position: fixed;
	top: -60px;
	right: 25px;
	width: 32px;
    min-width: 32px;
    height: 32px;
	cursor: pointer;
    background-repeat: no-repeat;
    background-position: center center;
	transition: 1s;
	-moz-transition: 1s; /* Firefox 4 */
	-webkit-transition: 1s; /* Safari and Chrome */
	-o-transition: 1s; /* Opera */
	box-shadow: 5px 5px 3px #F8F8F8;
}

.nav .nav-text {
  position: fixed;
	top: 53px;
	right: 21px;
	width: 40px;
  text-align: center;
  color: white;
}

#userinfo .nav-icon {
    background-image: url(assets/fullscreen.jpg);
}

#full_screen .nav-icon {
    background-image: url(assets/fullscreen.jpg);
}
.nav .nav-icon:hover{
	width:90px;
	height:70px;
}

#width1 {
  position: fixed;
  top: 180px;
  left: 65px;
  width: 40px;
  display: block;
  border: none;
  outline: none;
  background-color: red;
  color: white;
  font-weight: bold;
  cursor: pointer;
  padding: 15px;
  border-radius: 100px;
  box-shadow: 6px 6px 1px #F8F8F8;
  transition:width 1s;
  -moz-transition:width 1s; /* Firefox 4 */
  -webkit-transition:width 1s; /* Safari and Chrome */
  -o-transition:width 1s; /* Opera */
}
#width0 {
  position: fixed;
  top: 260px;
  left: 65px;
  width: 40px;
  display: block;
  border: none;
  outline: none;
  background-color: red;
  color: white;
  font-weight: bold;
  cursor: pointer;
  padding: 15px;
  border-radius: 100px;
  box-shadow: 6px 6px 1px #F8F8F8;
  transition:width 1s;
  -moz-transition:width 1s; /* Firefox 4 */
  -webkit-transition:width 1s; /* Safari and Chrome */
  -o-transition:width 1s; /* Opera */
}
#width{
  position: fixed;
  top: 180px;
  left: 15px;
  z-index: 99;
  border: none;
  outline: none;
  background-color: #3366FF;
  color: white;
  font-weight: bold;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 5px 5px 3px #F8F8F8;
  width: 40px;
  hight: 80px;
}
#history {
  position: fixed;
  top: 180px;
  left: 120px;
  width: 40px;
  display: block;
  border: none;
  outline: none;
  background-color: #FF6633;
  color: black;
  font-weight: bold;
  cursor: pointer;
  padding: 15px;
  border-radius: 100px;
  box-shadow: 6px 6px 3px #F8F8F8;
  transition:width 1s;
  -moz-transition:width 1s; /* Firefox 4 */
  -webkit-transition:width 1s; /* Safari and Chrome */
  -o-transition:width 1s; /* Opera */
}
#width1:hover {
  background-color: #555;
  width:52px;
  high:62px;
}
#width0:hover {
  background-color: #555;
  width:52px;
  high:62px;
}
#history:hover {
  background-color: #555;
  width:52px;
  high:62px;
}



#b4 {
  position: absolute;
  top: 10px;
  left: 350px;
  display: block;
  border: none;
  outline: none;
  background-color: red;
  color: white;
  font-weight: bold;
  cursor: pointer;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 6px 6px 3px #F8F8F8;
}

#b4:hover {
  background-color: #555;
}

#div2{
	position: fixed;
	bottom: 100;
	right: 12;
}

.bt{
	box-shadow: 10px 10px 5px #F8F8F8;
}

body{
background: #282828;
color: #FFFFFF;
}

#div{width: 800px;height: auto;margin: 0 auto;}

</style>
  </head>
  <body>
  <button onclick="topFunction()" id="myBtn" title="回顶部">返回顶部</button>
  <label>选择漫画地址文件：</label>
      <input type="file" id="chapters_hreff" /><br>
   <label>选择章节名称文件：</label>
	  <input type="file" id="chap_name" />
<div id="user-panel" class="ui-helper-clearfix">
	<a id="full_screen" class="nav" onclick="fullClick()" title="全屏浏览">
		<div class="nav-icon" style="margin-top: 6%; margin-bottom: -6%;"></div>
		<div class="nav-text">全屏</div>					
	</a>
</div>	
	<button onclick=width_plus() class='width' id='width1'>+</button>
	<button onclick=width_minus() class='width' id='width0'>-</button>
	<button  class='width' id='width'>调整漫画宽度</button>
	<div id="div2">
	<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=240 height=450 src="https://music.163.com/outchain/player?type=0&id=952033167&auto=1&height=430"></iframe>
    </div>
	  <input type="button" id="b4" value="读取全部文件" />
	  <input type="button" value="切换为本地阅读模式" id="load">
	  
	  <div align="center">
	  <input type="text" style="visibility:hidden;" id="001" value="" >
	  <input type="text" style="visibility:hidden;" id="002" value="" >
	  <h2 id="chap_names">章节名称：</h2>
	  总共<input type="text" id="sumchaps" style="width:35px" value="??" >章
	  <button onclick=pre() class='bt'>上一章</button>
	  当前第<input type="text" id="chaps" style="width:35px" value="1" >章
	  <button onclick=Goto();c();topFunction() class='bt'>跳转</button>
	  <button onclick=next() class='bt'>下一章</button>
	  <button onclick=downloadFile('"""+names[i-1]+"""',"你看到了第"+document.getElementById('chaps').value+"章__"+Date()) id='history'>保存阅读记录</button>
	  </div>
	  <div align="center" id="div"></div>
    <div align="center">
	  <i id='the_over' style='visibility:hidden'>漫画加载中......</i>
	  </div>
    <script>		
		var wait = false
		var wait1 = false
		var tem = ''
		var tem1 = ''
		var y = 1
		var count = 3
		var wid = 677
		var uclass = '"""+uclass+"""'
		var Uclass = uclass
				
        document.getElementById('b4').addEventListener('click',function(){
            wait = true
            if(wait){
				
				img_url = document.getElementById('001')
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
				
				btn = document.getElementById("load");
				t = true;
				btn.onclick = function dian() {
				if (t) {
					btn.value = "切换为在线阅读模式";
					Uclass = '';
					URL = img_url_loc;
				}
				else {
					btn.value = "切换为本地阅读模式";
					Uclass = uclass;
					URL = img_url;
				}
				t = !t;
			}
	
				wait2 = true

        document.getElementById('the_over').setAttribute('style','visible');

				//var unloaded = pages[y-1]-3; /*标记还有多少个图片没有加载*/
				window.onscroll = function() {
                //滚动条顶部到浏览器窗口顶部的距离，这里为什么要判断呢，是因为浏览器的兼容性问题
                scrollTop = (document.documentElement.scrollTop == 0 ? document.body.scrollTop : document.documentElement.scrollTop);
                //当滚动条滚动的距离 + 浏览器可视窗口大小 >= 图片元素的高度时加载
					if (scrollTop + document.body.clientHeight > image[count].offsetTop) {
					              console.log('此时count为:'+count);
                        image[count].setAttribute('src', image[count].getAttribute('src-data'));
                        count++;
                        if(count+1==pages[y-1]){
                        document.getElementById('the_over').innerHTML='本章节已结束';
                      }
                        //console.log(count+' '+i);
					//if(pages[y-1]%2!=0) image[pages[y-1]-1].setAttribute('src', image[pages[y-1]-1].getAttribute('src-data'));
				}
				//当网页向下滑动 200px 出现"返回顶部" 按钮
                if (scrollTop > 200) {
                    document.getElementById("myBtn").style.display = "block";
                } else {
                    document.getElementById("myBtn").style.display = "none";
                }
				}
				

        	}
			
        })
		
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
		function width_plus(){
			wid += 20;
			for(var i=0;i<pages[y-1]-1;i++)
			image[i].setAttribute('style','width:'+wid+'px');
		}
		function width_minus(){
			wid -= 20;
			for(var i=0;i<pages[y-1]-1;i++)
			image[i].setAttribute('style','width:'+wid+'px');
		}

		function createimg(n){
			var img = document.createElement('img');
			img.setAttribute('src-data',Uclass+URL[n]);
			img.setAttribute('class','image');
			img.setAttribute('style','width:'+wid+'px;vertical-align:middle;height:auto');
			img.id = n;
			var div = document.getElementById('div');
			div.appendChild(img);
		}
		
		function add_pre(n){
			sum = 0
			if(n>1){
				var n=n-1;
				for(i=0;i<n;i++){sum+=pages[i]-1;}
				}
			else sum = 0
			return sum
		}
		function add_next(n){
			sum = 0
			if(n>=1){
				var n=n-1;
				for(i=0;i<n;i++){sum+=pages[i]-1;}
				}
			else sum = 0
			return sum
		}
		function listimg_pre(n){
			console.log(n);
			for(num=0;num<pages[n-1]-1;num++){
				createimg(sum-pages[n-1]+1+num);
			}
		}
		function listimg_next(n){
			console.log(n);
			for(num=0;num<pages[n-1]-1;num++){
				createimg(sum+num);
			}
		}
		
		function removeimg_pre(n){
			if(sum>0){
			var div1 = document.getElementById("div");
			for(i=sum;i<sum+pages[n+1]-1;i++){
				document.getElementById(i).remove();
				}	
			}
		}
		function removeimg_next(n){
			console.log(sum);
			if(sum>0){
			var div1 = document.getElementById("div");
			for(i=sum-pages[n]+1;i<sum;i++){
				console.log(i)
				document.getElementById(i).remove();
				}	
			}
		}
		
		function next(){if(y<chaplen-1){cnext();firstone();c();topFunction()}}
		function pre(){if(y>=2){cpre();firstone();c();topFunction()}}
		function cnext(){y++;add_next(y);listimg_next(y);removeimg_next(y-2);firstone();count=3;document.getElementById('the_over').innerHTML='漫画加载中......';}
		function cpre() {y--;add_pre(y+1);listimg_pre(y);removeimg_pre(y-1);firstone();count=3;document.getElementById('the_over').innerHTML='漫画加载中......';}
		function c(){y;document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];}
		function Goto(){y = document.getElementById('chaps').value;add_next(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();}
		function Goto1(){y = document.getElementById('chaps1').value;add_next(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();}
		function topFunction() {
			document.body.scrollTop = 0;
			document.documentElement.scrollTop = 0;
		}
		
		
		document.onkeydown = function(event){//键盘事件左右键控制翻章节
			var e=event || window.event;
			if(e&&e.keyCode == 37){if(y>=2){cpre();c();topFunction()}}
			else if(e&&e.keyCode == 39){if(y<chaplen-1){cnext();c();topFunction()}}
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
	
	
	<!-- 看板娘 -->
	<!-- waifu-tips.js 依赖 JQuery 库 -->
    <script src="assets/jquery.min.js?v=3.3.1"></script>
    <!-- 实现拖动效果，需引入 JQuery UI -->
    <script src="assets/jquery-ui.min.js?v=1.12.1"></script>
    
    <div class="waifu">
        <div class="waifu-tips"></div>
        <canvas id="live2d" class="live2d"></canvas>
        <div class="waifu-tool">
            <span class="fui-home"></span>
            <span class="fui-chat"></span>
            <span class="fui-eye"></span>
            <span class="fui-user"></span>
            <span class="fui-photo"></span>
            <span class="fui-info-circle"></span>
            <span class="fui-cross"></span>
        </div>
    </div>
        
    <script src="assets/waifu-tips.min.js?v=1.4.2"></script>
    <!-- <script src="assets/waifu-tips.js"></script> -->

    <script src="assets/live2d.min.js?v=1.0.5"></script>
    <script type="text/javascript">
        /* 可直接修改部分参数 */
        live2d_settings['modelId'] = 3;                  // 默认模型 ID
        live2d_settings['modelTexturesId'] = 4;         // 默认材质 ID
        live2d_settings['modelStorage'] = false;         // 不储存模型 ID
        live2d_settings['canCloseLive2d'] = true;       // 隐藏 关闭看板娘 按钮
        live2d_settings['canTurnToHomePage'] = false;    // 隐藏 返回首页 按钮
        live2d_settings['waifuSize'] = '336x300';        // 看板娘大小
        live2d_settings['waifuTipsSize'] = '570x150';    // 提示框大小
        live2d_settings['waifuFontSize'] = '30px';       // 提示框字体
        live2d_settings['waifuToolFont'] = '36px';       // 工具栏字体
        live2d_settings['waifuToolLine'] = '50px';       // 工具栏行高
        live2d_settings['waifuToolTop'] = '-60px';       // 工具栏顶部边距
        live2d_settings['waifuDraggable'] = 'axis-x';    // 拖拽样式
        /* 在 initModel 前添加 */
        initModel("assets/waifu-tips.json?v=1.4.2")
    </script>
    <script type="text/javascript">initModel()</script>
	
	<div align="center">
	<button onclick=pre() class='bt'>上一章</button>
	  当前第<input type="text" id="chaps1" style="width:35px" value="1" >章
	  <button onclick=Goto1();c();topFunction() class='bt'>跳转</button>
	  <button onclick=next() class='bt'>下一章</button>
	</div>
  </body>
</html>
"""

create_file(html_path,"{}".format(html))#漫画html写入txt文件
print("\n漫画相关文件保存在：")
print(html_path)
print(img_path)
print(name_path)
print('\n')

if(webchoice==1):
  for str2 in list2:#获取漫画章节链接
      chapter.append(str2.select('li>a')[0].get_text())
      hrefs1.append(str2.select('li>a')[0]['href'])
  for i in range(len(hrefs1)):
    hrefs1[i] = "https://www.bnmanhua.com"+str(hrefs1[i])
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

try:
    with tqdm(range(len(chapter)),ascii=True) as t:
        for k in t:
            create_file(name_path,"{}".format(chapter[k]+"--#--"))#章节目录名称写入txt文件
            #create_file(hrefs1_path,"{}".format('https://www.manhuabei.com'+hrefs1[k+j]+"--#--"))#章节链接写入txt文件
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
  # check()

      # html_url=soup2.head.select('[name="mobile-agent"]')
      
      # html_url=[str(i) for i in html_url]#使用列表推导式把列表中的单个元素全部转化为str类型
      # html_url="".join(html_url)#把列表中的元素放在空串中，元素间用空格隔开
      # begin=html_url.find('comic')
      # end=html_url.find('.html')
      # html_url=html_url[begin:end+5]#获取当前页面url

      # page_sum = soup2.p#.select('[id="k_tota"]')
      
      # page_sum=[str(i) for i in page_sum]#使用列表推导式把列表中的单个元素全部转化为str类型
      # page_sum="".join(page_sum)#把列表中的元素放在空串中，元素间用空格隔开
      # begin=page_sum.find('k_total')
      # end=page_sum.find('</span>',45)
      # #print("总页数",page_sum[79:80])
elif(webchoice==2):
  image_src=[]
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
    url_mh3 = 'https://www.manhuabei.com'+hrefs1[j]
    if j==0:
        url_mh4 = h
    else:
        url_mh4 = 'https://www.manhuabei.com'+hrefs1[j-1]
    headers2 = {
        'Referer': url_mh4,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}

    try:
        res3 = bro.get(url_mh3)
        bro.set_script_timeout(4)
        bro.set_page_load_timeout(4)
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
      # print('tiao chu le!!!')
      # print(img_src)
    # s = soup2.select('p.img_info')#获取每章总页数
    # sum_page = s[0].get_text()
    # bounder = sum_page.find('/')
    # sum_page = str(sum_page[bounder+1:].strip().lstrip().rstrip(')'))
    # print(sum_page)
    # print(type(sum_page))
    # torf = True
    # while torf:#判断是否加载完成
    #     if torf:
    #         if 'data-index="'+sum_page in res3:
    #             ActionChains(bro).send_keys(Keys.ESCAPE).perform()
    #             print('停了')
    #             break
    #         else:
    #             res3 = bro.page_source
    #             time.sleep(2)
    #             print('顿一下')
    #             continue

    # res3 = bro.page_source
    # soup2 = BeautifulSoup(res3,'lxml')
    # for p in soup2.find_all('p'):
    #     p.decompose()
    # list3 = soup2.select('#images>img')#['src']
    # #print(len(list3))
    # for str3 in list3:#获取漫画名字与链接
    #     img_src.append(str3.get('src'))
    
    # img_src=[str(i) for i in img_src]#列表推导列表变字符串
    # img_src=''.join(img_src)
    #print(img_src)
    # if(j==len(chapter)):
    #   check()
    # img_src = img_src[0]
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