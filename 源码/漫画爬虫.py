#!/usr/bin/env python
import requests,time,os,shutil,sys,shutil,urllib,json,execjs
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
title = """
███████╗███████╗██████╗  ██████╗         ███╗   ███╗██╗   ██╗███╗   ███╗██╗   ██╗
╚══███╔╝██╔════╝██╔══██╗██╔═══██╗        ████╗ ████║██║   ██║████╗ ████║██║   ██║
  ███╔╝ █████╗  ██████╔╝██║   ██║        ██╔████╔██║██║   ██║██╔████╔██║██║   ██║
 ███╔╝  ██╔══╝  ██╔══██╗██║   ██║        ██║╚██╔╝██║██║   ██║██║╚██╔╝██║██║   ██║
███████╗███████╗██║  ██║╚██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║╚██████╔╝
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝ 
                                                                                 
"""
print(title)
print('建议先在浏览器内打开这几个漫画网站进行漫画的搜索选择，再进行爬取')
webcho = ['【1】百年漫画网: https://www.bnmanhua.com/page/all.html','【2】优酷漫画: https://www.ykmh.com/','【3】古风漫画网: https://www.gufengmh8.com/','【4】Xmanhua(X漫画)：http://www.xmanhua.com/','【5】动漫之家','【6】MangaPanda：http://mangapanda.cc/']
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
  web="(优酷漫画)"
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
  web="(Xmanhua)"
  # wc1=1
  # wbd()
  # wbd1()
  # wbd1.a.minimize_window()

elif(webchoice==5):
  pclass="+'.jpg'"
  pclass1="https"
  uclass="https"
  web="(动漫之家)"
  wc1=1
  wbd()
  wbd1()
  wbd1.a.minimize_window()
elif(webchoice==6):
  pclass="+'.jpg'"
  pclass1="http"
  uclass="http"
  web="(MangaPanda)"
  wc1=1
  wbd()
  wbd1()
  wbd1.a.set_window_size(400,200)#窗口大小
  wbd1.a.set_window_position(470,0)#位置
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
url_yk = "https://www.ykmh.com"
url_yk1 = 'https://www.ykmh.com/search/?keywords='
url_xm = 'http://www.xmanhua.com'
url_xm1 = 'http://www.xmanhua.com/search?title='
url_dm1 = 'https://www.dmzj.com/dynamic/o_search/index'
url_mp1 = 'http://mangapanda.cc/search?s='
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
headers_yk1 = {
    'Referer': 'https://www.ykmh.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
headers_gf = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'referer': 'https://www.bnmanhua.com/comic/',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}
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
  # names = [ names[i] for i in range(len(names)) if (i not in rm)]#按索引删除章节list
  # [ names.remove(cElement) for cElement in [names[k] for k in rm]]#按索引删除章节名称list
def save_json(fpath,msg):
  if (os.path.exists(fpath)):
    with open(fpath, "r",encoding='utf-8') as jsonFile:
      data = json.load(jsonFile)
      data[names[i-1]] = msg
      print(msg)
  else:
    data = {}
    data[names[i-1]] = msg
    print(msg)

global_var_list={}
def read_json(jpath,name):
    with open(jpath, "r",encoding='utf-8') as jsonFile:
        global_var_list[name] = str(json.load(jsonFile))

def create_file(path,msg,way):#内容写成文本文件
    f=open(path,way,encoding="utf-8")
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
  global img_path,Path,chapter,hrefs1,comic_download,Serial_number,names
  img_srcs2=[]
  read_json(pages_path,"pages_download")
  read_json(img_path,"img_download")
  pages_download = eval(global_var_list['pages_download'])[names[Serial_number-1]]
  img_srcs1 = eval(global_var_list['img_download'])[names[Serial_number-1]]
  pages_download = list(pages_download.values())

  img_srcs1 = img_srcs1.replace('\\','')
  img_srcs = img_srcs1.split("https")
  img_srcs.pop(0)
  for i in range(len(img_srcs)):
    img_srcs[i]="http"+str(img_srcs[i])

  d=0
  count=0
  for j in range(len(pages_download)):
    os.makedirs(comic_download+str(chapter[d]))
    img_srcs2 = []
    print("正在下载 {}：".format(chapter[d]))
    if(j==0):
      for i in range(pages_download[j]):
        img_srcs2.append(str(img_srcs[i]))
    else:
      for i in range(pages_download[j]):
        i = i + count
        img_srcs2.append(str(img_srcs[i]))

    if(d%7==0):time.sleep(4)
    headersimg={
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-dest': 'document',
      'sec-fetch-user': '?1',
      #'Referer': hrefs1[d],
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.45'}
    for i in tqdm(range(len(img_srcs2)),ascii=True):
      if(i%10==0):time.sleep(2)
      res4 = requests.session().get(url=img_srcs2[i],headers=headersimg)
      create_filewb(comic_download+str(chapter[d])+"\\"+str(i)+'.jpg',res4.content)
    count += int(pages_download[j])
    d+=1
  print("\n  下载的漫画保存在【{}】目录下".format(comic_download))
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
  if num > 1:
    id_select = int(input("有{}种目录，想选择哪一个：".format(count)))-1
  else:
    id_select = 0
  chap_id = [id_select,id]
  return chap_id

def imgjson_write():
  global img_path,Serial_number,names,img_src
  if (os.path.exists(img_path)):
    with open(img_path,"r",encoding='utf-8') as jsonFile:
      data = json.load(jsonFile)
      if(x==0):
        data = "{" + str(data)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
        data = eval(data)
        data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src
        # print(data[names[Serial_number-1]])
        # print(type(data[names[Serial_number-1]]))
      else:
        # print(Serial_number-1)
        # print(type(data))
         data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src
  else:
    data = {}
    # print(Serial_number-1)
    data[names[Serial_number-1]] = img_src
  return data

def pagesjson_write():
  global pages,list_t,pages_path,Serial_number,names
  pagestem = dict(zip(list_t,pages))
  if (os.path.exists(pages_path)):
    with open(pages_path,"r",encoding='utf-8') as jsonFile:
      jdata = json.load(jsonFile)
      jdata = "{" + str(jdata)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
      jdata = eval(jdata)
      jdata[names[Serial_number-1]] = pagestem.copy()

      # print(jdata[names[Serial_number-1]])
      # print(type(jdata[names[Serial_number-1]]))
  else:
    jdata = {}
    # print(Serial_number-1)
    jdata[names[Serial_number-1]] = pages
  return jdata

def combine():
  #json合并
  read_json(name_path,"name")
  read_json(img_path,"img")
  read_json(pages_path,"pages")

  name_img_pages = "var chap_name ="+global_var_list["name"]+";"+"var img_url = "+global_var_list["img"]+";"+"var pages = "+global_var_list["pages"]
  create_file(data_path,name_img_pages,'w')#json合并写入name_img_pages.json


name_=input("请输入想看的漫画名称：")
data = {'keyword':name_}
data_dm = {'keywords':name_}
if(webchoice==1):
  r = requests.session()
  res1 = r.post(url=url_bn1,headers=headers_bn,data=data)
  res1 = res1.text
elif(webchoice==2):
  r = requests.session()
  res1 = r.get(url=url_yk1+name_,headers=headers_yk1)
  res1 = res1.text
elif(webchoice==4):
  r = requests.session()
  res1 = r.get(url=url_xm1+name_)
  res1 = res1.text
elif(webchoice==5):
  r = requests.session()
  res1 = r.post(url=url_dm1,headers=headers_dm,data=data_dm)
  res1 = res1.text
elif(webchoice==5):
  r = requests.session()
  res1 = r.get(url=url_mp1 + name_ + '&post_type=manga')
  res1 = res1.text
else:
  r = requests.session()
  res1 = r.get(url=url_gf1+name_, headers = headers_gf)
  res1 = res1.text
  # create_file(r"C:\Users\HASEE\Desktop\漫画爬虫\gf_res1.html",res1,"w")
  # res1 = wbd1.a.get(url=url_gf1+name_)

names=[]
hrefs=[]
pages=[]
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
  soup = BeautifulSoup(res1,'lxml')
  list1 = soup.select('.title>a')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.get_text())
    hrefs.append(str1['href'])

elif(webchoice==5):
  soup=BeautifulSoup(res1,'lxml')
  list1 = soup.select('div.tab-con>ul>li')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.select('li>a')[0]['title'])
    hrefs.append(str1.select('li>a')[0]['href'])
elif(webchoice==5):
  soup=BeautifulSoup(res1,'lxml')
  list1 = soup.select('div.left')
  for str1 in list1:#获取漫画名字与链接
    names.append(str1.select('div>a>h3')[0].get_text())
    hrefs.append(str1.select('div>a')[0]['href'])
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

Serial_number = i = int (input('请输入想看漫画的序号：'))
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
  cover_src = soup1.select('div.bpic>img')[0]['src']
  img_domain_index = cover_src.find('.com')
  img_domain = cover_src[0:img_domain_index]+'.com'
  list2=soup1.select('ul.jslist01>li')
elif(webchoice==2):
  chapterName=[]
  h = hrefs[i-1]
  url_yk2 = h
  chap_index = 'chapter-list-'
  res2 = r.get(url=url_yk2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  cover_src = soup1.select('.comic_i_img>img')[0]['src']

  listchap = soup1.select('.zj_list_head')
  for strchap in listchap:
    chapterName.append(strchap.select('div>h2')[0].get_text())#多章节选择章节名称获取
  chap_id = Multichapter_select(chap_index,res2)
  id = chap_id[0]
  # list2=soup1.select('#'+chap_id[1][id]+'>li')
  list2 = soup1.select('div.zj_list_con')[id]
  list2 = list2.select('div>ul>li')
elif(webchoice==4):
  url_xm2 = url_xm+hrefs[i-1]
  mid = str(hrefs[i-1][1:-3])
  res2 = r.get(url=url_xm2)
  res2 = res2.text
  soup1 = BeautifulSoup(res2,'lxml')
  cover_src = soup1.select('.detail-info-cover')[0]['src']
  list2 = soup1.select('#chapterlistload>a')
  listpage = soup.select('.title>a')
elif(webchoice==5):
  h = 'https:'+hrefs[i-1]
  url_dm2 = h
  res2 = r.get(url=url_dm2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  list2=soup1.select('div.cartoon_online_border>ul>li')
elif(webchoice==5):
  h = hrefs[i-1]
  url_mp2 = h
  res2 = r.get(url=url_mp2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  list2=soup1.select('div.cl>ul>li')
else:
  chapterName=[]
  url_gf2 = h
  chap_index = 'chapter-list-'
  # print(url_gf2)
  res2 = r.get(url=url_gf2)
  res2 = res2.text
  soup1=BeautifulSoup(res2,'lxml')
  cover_src = soup1.select('.pic')[0]['src']
  print(cover_src)

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
img_srcx=[]
pages=[]
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
Path = filepath+"\\Download\\"+names[i-1]+web#漫画保存路径
name_path = filepath+'\\dist\\章节名称.json'#章节名称文件保存路径
# hrefs1_path = Path+'\\章节链接.txt'#章节链接文件保存路径
img_path = filepath+'\\dist\\漫画地址.json'#图片地址文件路径
pages_path = filepath+'\\dist\\pages.json'#漫画每章页数文件路径
data_path = filepath+'\\dist\\data.json'
cover_path = filepath+'\\assets\\封面\\'+names[i-1]+'cover.jpg'#漫画封面路径
coverjson_path = filepath+'\\dist\\cover.json'#漫画封面json路径
html_path = filepath+'\\index.html'#漫画html文件路径
comic_download = filepath+"\\Download\\"+names[Serial_number-1]+"\\"#下载漫画地址

res_cover = requests.session().get(url=cover_src)
create_filewb(cover_path,res_cover.content)#封面下载

cover = """<div onmouseover='bounceon(this)' onmouseout='bounceoff(this)' class='mdui-ripple mdui-hoverable mdui-card mdui-col-md-2 mdui-col-xs-6'><div class='mdui-ripple mdui-hoverable mdui-card-media'><a href='阅读.html?"""+names[i-1]+"""' target="_blank"><img src='assets\\封面\\"""+names[i-1]+"""cover.jpg'/></a><div class='mdui-card-media-covered'><div class='mdui-card-primary'><div style='font-weight:900;font-size: large;'>"""+names[i-1]+"""</div></div></div></div></div>"""
if (os.path.exists(coverjson_path)):
  with open(coverjson_path,"r",encoding='utf-8') as jsonFile:
    jcover = json.load(jsonFile)
    jcover = "{" + str(jcover)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
    jcover = eval(jcover)
    jcover[names[Serial_number-1]] = cover
else:
    jcover = {}
    # print(i-1)1
    jcover[names[Serial_number-1]] = cover
create_file(coverjson_path,json.dumps(jcover,ensure_ascii=False),"w")#保存漫画封面地址

comicbook1 = []
with open(coverjson_path,"r",encoding='utf-8') as jsonFile:
  coverjson = json.load(jsonFile)
for value in coverjson.values():
    comicbook1.append(value)
comicbook = ''.join(comicbook1)

html = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<meta name="referrer" content="never">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>书架</title>
		<link rel="icon" type="image/x-icon/" href="assets/书架.png"/>
		<link href="dist/bootstrap-3.3.7-dist/css/bootstrap.min.css" rel="stylesheet">
		<link
		    rel="stylesheet"
		    href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"
		  />
	</head>
	<body id="body" class="mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-auto mdui-appbar-with-toolbar" data-status="click" style="zoom: 1;">
		<!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
		<script src="dist/bootstrap-3.3.7-dist/js/jquery.min.js"></script>
		<!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
		<script src="dist/bootstrap-3.3.7-dist/js/bootstrap.min.js"></script>
		<script src="dist/bootstrap-3.3.7-dist/js/bootstrap-slider.min.js"></script>
		<script type="text/javascript" src="dist/bootstrap-3.3.7-dist/js/buttons.js"></script>
		<script src="dist/mdui-v1.0.1/js/mdui.min.js"></script>
		<!-- <link rel="stylesheet" type="text/css" href="dist/fontawesome-free-5.15.1-web/css/fontawesome.min.css"/> -->
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome/css/font-awesome.min.css">
		<link rel="stylesheet" type="text/css" href="dist/bootstrap-3.3.7-dist/css/buttons.min.css"/>
		<link rel="stylesheet" type="text/css" href="dist/mdui-v1.0.1/css/mdui.min.css"/>
		<link rel="stylesheet" type="text/css" href="dist/bootstrap-3.3.7-dist/css/bootstrap-slider.min.css"/>
		
		<div class="mdui-container">
		  <div class="mdui-row">
			  <div>
            """+comicbook+"""
			  </div>
		  </div>
		</div>
		<script>
			function bounceon(bounce1){
				bounce1.setAttribute('class',"mdui-ripple mdui-hoverable mdui-card mdui-col-md-2 mdui-col-xs-6 animate__animated animate__bounce")
			}
			function bounceoff(bounce2){
				bounce2.setAttribute('class',"mdui-ripple mdui-hoverable mdui-card mdui-col-md-2 mdui-col-xs-6")
			}
		</script>
	</body>
</html>
"""

create_file(html_path,html,"w")#漫画html写文件

if(webchoice==1):
  for str2 in list2:#获取漫画章节链接
      chapter.append(str2.select('li>a')[0].get_text())
      hrefs1.append(str2.select('li>a')[0]['href'])
  for j in range(len(hrefs1)):
    hrefs1[j] = img_domain +str(hrefs1[j])
  chapter.reverse()
  first_chaperro()

elif(webchoice==2):
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('.list_con_zj')[0].get_text().replace(' ',''))
    hrefs1.append(str2.select('li>a')[0]['href'])
  
  first_chaperro()
elif(webchoice==4):
  for str2 in list2:#获取漫画章节链接
      t = 0
      print(str2.get_text())
      temt = str2.get_text()
      tem = str2.get_text().split(' ')
      print(tem)
      tem = [tem[0],tem[-2]]
      chapter.append(tem[0])
      hrefs1.append(str2['href'])
      pages.append(tem[1][1:-2])
      tem = []
      t += 1
  for j in range(len(hrefs1)):
    hrefs1[j] = url_xm +str(hrefs1[j])
  pages.reverse()
  chapter.reverse()
  first_chaperro()

elif(webchoice==5):
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>a')[0]['title'])
    hrefs1.append(str2.select('li>a')[0]['href'])

elif(webchoice==5):
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>span>a')[0]['title'])
    hrefs1.append(str2.select('li>span>a')[0]['href'])

else:
  for str2 in list2:#获取漫画章节链接
    chapter.append(str2.select('li>a>span')[0].get_text())
    hrefs1.append(str2.select('li>a')[0]['href'])
    # print('666666')

  first_chaperro()
# print(i,len(chapter),names)

print("\n {} 总共有 {} 话".format(names[i-1],len(chapter)))
upgrage = (input('爬取起始章节数 就是你想从第几话开始爬取\n输入爬取的起始章节数(直接回车从第一话开始爬取):'))
if upgrage=="":j=upgrage=0
else:
  upgrage = int(upgrage)-1
  j = upgrage
remove_list()

print("\n")
ifdownload = (input('是否将漫画下载到本地观看(输入1代表是，或直接回车否)：')) 
if ifdownload=="":ifdownload=0
else:ifdownload = int(ifdownload)

print("\n漫画相关文件保存在：")
print(html_path)
print(img_path)
print(name_path)
print('\n')

# try:
#     with tqdm(range(len(chapter)),ascii=True) as t:
#         for k in t:
list_t = []
for x in range(len(chapter)):
    list_t.append(x)
chapter_t = dict(zip(list_t,chapter))
if(webchoice==4):
  create_file(pages_path,json.dumps(pagesjson_write(),ensure_ascii=False),"w")#保存漫画页数

if (os.path.exists(name_path)):
  with open(name_path, "r",encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)
    data = "{" + str(data)[1:-1] + ",'"+names[i-1]+"': " + "{}}"
    data = eval(data)
    data[names[i-1]] = chapter_t.copy()
else:
  data = {}
  data[names[i-1]] = chapter_t

# save_json(name_path,chapter)
create_file(name_path,json.dumps(data,ensure_ascii=False),"w")#章节目录名称写入txt文件
        #create_file(hrefs1_path,"{}".format('https://www.manhuadai.com'+hrefs1[k+j]+"--#--"))#章节链接写入txt文件
# except KeyboardInterrupt:
#     t.close()
#     raise
# t.close()

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
        img_src[i]= img_domain +'/'+img_src[i]
      pages.append(len(img_src))
      create_file(pages_path,json.dumps(pagesjson_write(),ensure_ascii=False),"w")#保存漫画页数

      img_src=[str(i).replace('\\','') for i in img_src]
      img_src=''.join(img_src)
      if (os.path.exists(img_path)):
        with open(img_path,"r",encoding='utf-8') as jsonFile:
          data = json.load(jsonFile)
          if(x==0):
            data = "{" + str(data)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
            data = eval(data)
            data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src

            # print(data[names[Serial_number-1]])
            # print(type(data[names[Serial_number-1]]))
          else:
            # print(Serial_number-1)
            # print(type(data))
            data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src
      else:
        data = {}
        # print(Serial_number-1)
        data[names[Serial_number-1]] = img_src

      create_file(img_path,json.dumps(data,ensure_ascii=False),"w")#保存漫画图片
      combine()
      if j%13==0:time.sleep(12*speed)
      time.sleep(speed)
      if img_src:continue
      else:break
# def paegs_write():
#   pages = dict(zip(list_t,pages))
#   if (os.path.exists(pages_path)):
#     with open(pages_path,"r",encoding='utf-8') as jsonFile:
#       jdata = json.load(jsonFile)
#       jdata = "{" + str(jdata)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
#       jdata = eval(jdata)
#       jdata[names[Serial_number-1]] = pages.copy()
#       create_file(pages_path,json.dumps(jdata,ensure_ascii=False),"w")#保存漫画图片页数

#       # print(jdata[names[Serial_number-1]])
#       # print(type(jdata[names[Serial_number-1]]))
#   else:
#     jdata = {}
#     # print(Serial_number-1)
#     jdata[names[Serial_number-1]] = pages
#     create_file(pages_path,json.dumps(jdata,ensure_ascii=False),"w")#保存漫画图片页数
  r.close()#关闭连接

elif(webchoice==2):
  image_src=[]
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
    url_mh3 = url_yk + hrefs1[j]
    if j==0:
        url_yk4 = h
    else:
        url_yk4 = url_yk + hrefs1[j-1]
    headers2 = {
        'Referer': url_yk4,
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
    # pages[x] = len(images)
    # print(pages)
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
      img_src.append('http://bujianle/bujianle.png')
      # print('tiao chu le!!!')
    
    pages.append(len(img_src))
    create_file(pages_path,json.dumps(pagesjson_write(),ensure_ascii=False),"w")#保存漫画页数
    img_src = [str(i) for i in img_src]
    img_src=''.join(img_src)
    create_file(img_path,json.dumps(imgjson_write(),ensure_ascii=False),"w")#保存漫画图片地址
    combine()

    # for i in range(len(images)):
    #   images[i]="https://img01.eshanyao.com/showImage.php?url="+str(images[i])
    # #print(images)
    # images = []

    # pages.append(len(img_src))
    # create_file(pages_path,json.dumps(pagesjson_write(),ensure_ascii=False),"w")#保存漫画页数
    # img_src=[str(i) for i in img_src]
    # img_src=''.join(img_src)
    # #print(img_src)
    # create_file(img_path,json.dumps(imgjson_write(),ensure_ascii=False),"w")#保存漫画图片地址
    # combine()
    # # create_file(img_path,names[i-1]+":"+json.dumps(img_src))#保存漫画图片地址

    if j%7==0:time.sleep(20*speed)
    j+=1
    if(j<len(chapter)+upgrage):
      img_src = []
      image_src = []
    #bro.execute_script('window.stop()')
  bro.quit()

elif(webchoice==4):
  i=0
  j=len(chapter)
  for x in tqdm(range(len(chapter)),ascii=True):
      url_xm3=hrefs1[j-1]
      req_count1 = int(pages[j-1])-2
      req_count2 = 3
      if(req_count1>15):
        req_count = int(req_count1/15)
      else:
        req_count = 1
      cid = str(hrefs1[j-1][23:-1])
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
      headers_xm = {
          'Host': 'www.xmanhua.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
          'Accept': '*/*',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate',
          'X-Requested-With': 'XMLHttpRequest',
          'Connection': 'close',
          'Referer': hrefs1[j-1],#http://www.xmanhua.com/m91735/
          'Content-Length': '2'
      }
      #print("第几话网址：",url_bn3)
      i+=1
      j-=1
      res3 = r.get(url_xm3+"chapterimage.ashx?cid="+cid+"&page=1&key=&_cid="+cid+"&_mid="+mid, headers = headers_xm)
      img_src.append(execjs.eval(res3.text))
      for y in range(req_count):
        res3 = r.get(url_xm3+"chapterimage.ashx?cid="+cid+"&page="+str(req_count2)+"&key=&_cid="+cid+"&_mid="+mid, headers = headers_xm)
        req_count2 = int(req_count2)
        req_count2 += 15

      if (os.path.exists(img_path)):
        with open(img_path,"r",encoding='utf-8') as jsonFile:
          data = json.load(jsonFile)
          if(x==0):
            data = "{" + str(data)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
            data = eval(data)
            data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src

            # print(data[names[Serial_number-1]])
            # print(type(data[names[Serial_number-1]]))
          else:
            # print(Serial_number-1)
            # print(type(data))
            data[names[Serial_number-1]] = data[names[Serial_number-1]] + img_src
      else:
        data = {}
        # print(Serial_number-1)
        data[names[Serial_number-1]] = img_src

      create_file(img_path,json.dumps(data,ensure_ascii=False),"w")#保存漫画图片
      combine()
      if j%13==0:time.sleep(12*speed)
      time.sleep(speed)
      if img_src:continue
      else:break
# def paegs_write():
#   pages = dict(zip(list_t,pages))
#   if (os.path.exists(pages_path)):
#     with open(pages_path,"r",encoding='utf-8') as jsonFile:
#       jdata = json.load(jsonFile)
#       jdata = "{" + str(jdata)[1:-1] + ","+"'"+names[Serial_number-1]+"'"+ ':""}'
#       jdata = eval(jdata)
#       jdata[names[Serial_number-1]] = pages.copy()
#       create_file(pages_path,json.dumps(jdata,ensure_ascii=False),"w")#保存漫画图片页数

#       # print(jdata[names[Serial_number-1]])
#       # print(type(jdata[names[Serial_number-1]]))
#   else:
#     jdata = {}
#     # print(Serial_number-1)
#     jdata[names[Serial_number-1]] = pages
#     create_file(pages_path,json.dumps(jdata,ensure_ascii=False),"w")#保存漫画图片页数
  r.close()#关闭连接

elif(webchoice==5):
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
      create_file(img_path,names[i-1]+":"+json.dumps(img_src))#保存漫画图片地址
      time.sleep(speed)
      j+=1
      if(j<len(chapter)):img_src = []
  bro.quit()

elif(webchoice==5):
  bro = wbd1.a
  image_src=[]
  img_src=[]
  for x in tqdm(range(len(chapter)),ascii=True):
    url_mp3 = hrefs1[j]

    # try:
    #     res3 = bro.get(url_gf3)
    #     bro.set_script_timeout(4)
    #     bro.set_page_load_timeout(4)
    # except Exception:
    #     ActionChains(bro).send_keys(Keys.ESCAPE).perform()
    res3 = bro.get(url_mp3)
    js3 = """
    var url = picArry;
    return url;
    """
    images = bro.execute_script(js3)
    while True:
      if images:
        ActionChains(bro).send_keys(Keys.ESCAPE).perform()
        break
      else:
        time.sleep(0.5)
        images = bro.execute_script(js3)
        continue
    # images = str(images[0])
    # images = images.replace('\\','')
    i = 0
    for g in range(len(images)):
      img_src.append(images[i])
      i+=1

    img_src = [str(i) for i in img_src]
    img_src=''.join(img_src)
    create_file(img_path,names[i-1]+":"+json.dumps(img_src))#保存漫画图片地址
    # img_src = list(img_src)
    j+=1
    if j%7==0:time.sleep(12*speed)
    if(j<len(chapter)+upgrage):
      img_src = []
      image_src = []
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
      img_src.append('http://bujianle.com/bujianle.png')

    pages.append(len(img_src))
    create_file(pages_path,json.dumps(pagesjson_write(),ensure_ascii=False),"w")#保存漫画页数
    img_src = [str(i) for i in img_src]
    img_src=''.join(img_src)
    create_file(img_path,json.dumps(imgjson_write(),ensure_ascii=False),"w")#保存漫画图片地址
    combine()
    # create_file(img_path,names[i-1]+":"+json.dumps(img_src))#保存漫画图片地址

    # img_src = list(img_src)
    j+=1
    if j%7==0:time.sleep(12*speed)
    if(j<len(chapter)+upgrage):
      img_src = []
      image_src = []
  bro.quit()


if (global_var_list["img"]):
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