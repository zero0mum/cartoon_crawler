import os,shutil,sys,zipfile,requests,time,urllib,json
import webbrowser
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QUrl, Slot, QObject
from PySide2.QtGui import  QIcon

fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
name_path = filepath+'\\dist\\章节名称.json'#章节名称文件保存路径
img_path = filepath+'\\dist\\漫画地址.json'#图片地址文件路径
pages_path = filepath+'\\dist\\pages.json'#漫画每章页数文件路径
coverjson_path = filepath+'\\dist\\cover.json'#漫画封面json路径
setting_path =  filepath+'\\dist\\setting.json'#设置json路径
html_path = filepath+'\\书架.html'#漫画html文件路径
data_path = filepath+'\\dist\\data.json'
ui_path = filepath+'\\assets\\GUI\\main.ui'

global_var_jsonlist={}
def read_asjson(jpath,name):
    with open(jpath, "r",encoding='utf-8') as jsonFile:
        global_var_jsonlist[name] = json.load(jsonFile)

'''漫画爬取部分'''

'''漫画删除部分'''
global_var_list={}
def read_jsoni(jpath,name):
    if os.path.exists(jpath):
        with open(jpath, "r",encoding='utf-8') as jsonFile:
            global_var_list[name] = str(json.load(jsonFile))
    else:
        global_var_list[name] = '""'
def read_json(jpath,name):
    with open(jpath, "r",encoding='utf-8') as jsonFile:
        global_var_list[name] = str(json.load(jsonFile))
def del_json(path,name):#删除字典指定键值对
    with open(path,"r",encoding='utf-8') as jsonFile:
        jsondata = json.load(jsonFile)
        del jsondata[name]
        create_file(path,json.dumps(jsondata,ensure_ascii=False),"w")
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)
def create_file(path,msg,way):#内容写成文本文件
    f=open(path,way,encoding="utf-8")
    f.write(msg)
    f.close
def comic_name_lenth():
    global keys_data, keys_lenth,keys_data_source
    if(os.path.exists(pages_path)):
        with open(pages_path,"r",encoding='utf-8') as jsonFile:
            keys_data_source = json.load(jsonFile)
            keys_data = list(keys_data_source.keys())
        keys_lenth = len(keys_data)
    else:
        keys_data = []
        keys_lenth = 0

'''漫画打包部分'''
def file2zip(zip_file_name: str, file_names: list):
    """ 将多个文件夹中文件压缩存储为zip
    
    :param zip_file_name:   /root/Document/test.zip
    :param file_names:      ['/root/user/doc/test.txt', ...]
    :return: 
    """
    # 读取写入方式 ZipFile requires mode 'r', 'w', 'x', or 'a'
    # 压缩方式  ZIP_STORED： 存储； ZIP_DEFLATED： 压缩存储
    with zipfile.ZipFile(zip_file_name, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for fn in file_names:
            parent_path, name = os.path.split(fn)
            
            # zipfile 内置提供的将文件压缩存储在.zip文件中， arcname即zip文件中存入文件的名称
            # 给予的归档名为 arcname (默认情况下将与 filename 一致，但是不带驱动器盘符并会移除开头的路径分隔符)
            zf.write(fn, arcname=name)
            
            # 等价于以下两行代码
            # 切换目录， 直接将文件写入。不切换目录，则会在压缩文件中创建文件的整个路径
            # os.chdir(parent_path)
            # zf.write(name)

def remove_file(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    else:print('文件不存在！')

'''漫画导入部分'''
def json_write(path,names,msg):#文件目录：0（未导入）或1（已经导入过）
    if (os.path.exists(path)):
        msg = str(msg)
        with open(path,"r",encoding='utf-8') as jsonFile:
            data = json.load(jsonFile)
            tem1 = str(data)
            if tem1.find(names) != -1:
                data = "{" + str(data)[1:-1] + ","+"'"+names+"'"+ ":'1'}"
            else:
                data = "{" + str(data)[1:-1] + ","+"'"+names+"'"+ ":'"+msg+"'}"
    print(data)
    data = eval(data)
    create_file(path,json.dumps(data,ensure_ascii=False),"w")#写入json文件
    
def pagesjson_write(n):
  global pages,list_t,pages_path,names
  pagestem = dict(zip(list_t,pages))
  if (os.path.exists(pages_path)):
    with open(pages_path,"r",encoding='utf-8') as jsonFile:
      jdata = json.load(jsonFile)
      jdata = "{" + str(jdata)[1:-1] + ","+"'"+names[n]+"'"+ ':""}'
      jdata = eval(jdata)
      jdata[names[n]] = pagestem.copy()

def imgjson_write(n):
  global img_path,names,img_src
  if (os.path.exists(img_path)):
    with open(img_path,"r",encoding='utf-8') as jsonFile:
      data = json.load(jsonFile)
      if(x==0):
        data = "{" + str(data)[1:-1] + ","+"'"+names[n]+"'"+ ':""}'
        data = eval(data)
        data[names[n]] = img_src
        # print(data[names[n]])
        # print(type(data[names[n]]))
      else:
        # print(n)
        # print(type(data))
         data[names[n]] = img_src
  else:
    data = {}
    # print(n)
    data[names[n]] = img_src
  return data
def combine():
  #json合并
  read_json(name_path,"name")
  read_json(img_path,"img")
  read_json(pages_path,"pages")
  read_json(setting_path,"setting")
  read_json(coverjson_path,"cover")

  name_img_pages = "var chap_name ="+global_var_list["name"]+";"+"var img_url = "+global_var_list["img"]+";"+"var pages = "+global_var_list["pages"]+";"+"var setting = "+global_var_list["setting"]+";"+"var covers = "+global_var_list["cover"]
  create_file(data_path,name_img_pages,'w')#json合并写入name_img_pages.json
def combinei():
  #json合并
  read_jsoni(name_path,"name")
  read_jsoni(img_path,"img")
  read_jsoni(pages_path,"pages")
  read_jsoni(setting_path,"setting")
  read_jsoni(coverjson_path,"cover")

  name_img_pages = "var chap_name ="+global_var_list["name"]+";"+"var img_url = "+global_var_list["img"]+";"+"var pages = "+global_var_list["pages"]+";"+"var setting = "+global_var_list["setting"]+";"+"var covers = "+global_var_list["cover"]
  create_file(data_path,name_img_pages,'w')#json合并写入name_img_pages.json

'''漫画爬取部分'''

List = []
cover_path = ''
comic_download = ''
comic_name = ''
keys_data = []
keys_lenth = 0

read_json(setting_path,"setting")
global_var_list['setting'] = eval(global_var_list['setting'])
global_var_list['setting']['default_import_src'] = filepath.replace('\\','/') + '/漫画导入'
if global_var_list['setting']['firsttime'] == 'true':
    global_var_list['setting']['current_import_src'] = filepath.replace('\\','/') + '/漫画导入'
    global_var_list['setting']['firsttime'] = 'false'
data = eval(str(global_var_list['setting']))
create_file(setting_path,json.dumps(global_var_list['setting'],ensure_ascii=False),"w")#默认路径写入json文件
combinei()


comic_name_lenth()
class Comic:

    def __init__(self):
        self.ui = QUiLoader().load(ui_path)
        # self.ui.setStyleSheet ("border:2px groove gray;border-radius:10px;padding:2px 4px;")
        self.ui.openbookrack.clicked.connect(self.openbookrack)
        self.ui.comics_import.clicked.connect(self.comics_import)#导入按钮
        self.ui.edit_folder.clicked.connect(self.edit_folder)#改导入文件夹
        self.ui.open_import_folder.clicked.connect(self.open_import_folder)#打开导入文件夹
        self.ui.reset_folder.clicked.connect(self.reset_folder)
        self.ui.help.clicked.connect(self.help)#帮助
        #self.ui.progressBar_2.setValue(0)#进度条归零
        self.ui.progressBar_2.reset()#进度条初始化
        self.del_start()
        self.zip_start()
        read_json(setting_path,"setting")
        global_var_list['setting'] = eval(global_var_list['setting'])
        self.ui.tab4_label_currentsrc.setText('当前本地漫画导入文件夹路径为：' + global_var_list['setting']['current_import_src'])
        self.ui.tab4_label_defaultsrc.setText('默认本地漫画导入文件夹路径为：' + global_var_list['setting']['default_import_src'])
    def help(self):
        webbrowser.open('https://blog.csdn.net/zero_mumu/article/details/107852060')
    def about(self):
        webbrowser.open('https://blog.csdn.net/zero_mumu/article/details/107852060')
    def Clear(self):
        self.ui.listWidget.clear()
    def Clear2(self):
        self.ui.listWidget_2.clear()
    def Clear3(self):
        self.ui.listWidget_3.clear()
    '''漫画爬取'''
    def openbookrack(self):
        webbrowser.open(html_path)
        # url = QUrl.fromLocalFile("C:\\Users\\HASEE\\Desktop\\漫画爬虫\\书架.html")
        # web = QWebEngineView()
        # web.load(url)
    '''漫画删除'''
    def del_start(self):
        # self.ui.listWidget_2.addItems(["删除工具会删除对应所选漫画的封面,下载的内容,和数据(除了阅读记录保存在浏览器)","在书架上的漫画有：\n"])
        self.ui.listWidget_2.addItems(keys_data)
        self.ui.listWidget_2.itemClicked.connect(self.ClearShow)
    def ClearShow(self):
        global List, cover_path, comic_download, global_var_list, comic_name
        list_item = self.ui.listWidget_2.currentItem()
        comic_name = list_item.text()
        list_index = self.ui.listWidget_2.indexFromItem(list_item)
        self.Clear2()
        self.ui.listWidget_2.addItem(comic_name)
        List = [comic_name,list_index]
        cover_path = filepath+'\\assets\\封面\\'+comic_name+'cover.jpg'#漫画封面路径
        comic_download = filepath+"\\Download\\"+comic_name+"\\"#下载漫画地址
        read_asjson(setting_path,'setting')
        if str(global_var_jsonlist['setting']).find(comic_name) != -1:
            setting_boole = True
            comic_imported = global_var_jsonlist['setting']['current_import_src'] +'/'+ comic_name
        else:
            setting_boole = False
            comic_imported = ''
        choice = QMessageBox.question(
            self.ui,
            '确认',
            '确定要删除【{}】吗？'.format(comic_name))

        total_path = [name_path,img_path,pages_path,coverjson_path,cover_path,data_path,comic_download,comic_imported]


        # choice = input("\n确定删除【{}】么？输入（y/n）:".format(comic_name))
        if (choice == QMessageBox.Yes and keys_lenth > 1):
            for y in range(4):
                del_json(total_path[y],comic_name)
            if comic_imported != '':
                del_json(setting_path,comic_imported)#删除setting.jso中对应avoid_reimport的值
            if os.path.exists(cover_path):
                os.remove(cover_path)#删除封面
            if(os.path.exists(total_path[6])):
                shutil.rmtree(total_path[6])#删除下载得漫画

            if(os.path.exists(total_path[7]) & setting_boole):
                shutil.rmtree(total_path[7])#删除导入的得漫画
            self.rewrite_web()
        elif (choice == QMessageBox.Yes and keys_lenth==1):
            for y in range(6):
                os.remove(total_path[y])
            if(os.path.exists(total_path[6])):
                shutil.rmtree(total_path[6])
            if comic_imported != '':
                del_json(setting_path,comic_imported)#删除setting.jso中对应avoid_reimport的值
            if(os.path.exists(total_path[7]) & setting_boole):
                shutil.rmtree(total_path[7])#删除导入的得漫画
            self.rewrite_web()
        else:
            # restart_program()
            self.Clear2()
            self.ui.listWidget_2.addItems(keys_data)
        combine()
    def rewrite_web(self):
        global keys_data, keys_lenth, global_var_list, comic_name
        if(keys_lenth>1):
            comicbook1 = []
            with open(coverjson_path,"r",encoding='utf-8') as jsonFile:
                coverjson = json.load(jsonFile)
            for value in coverjson.values():
                comicbook1.append(value)
            comicbook = ''.join(comicbook1)
            #json合并
            global_var_list={}
            read_json(name_path,"name")
            read_json(img_path,"img")
            read_json(pages_path,"pages")
            name_img_pages = "var chap_name ="+global_var_list["name"]+";"+"var img_url = "+global_var_list["img"]+";"+"var pages = "+global_var_list["pages"]
            create_file(data_path,name_img_pages,'w')#json合并写入data.json
        else:
            comicbook = ''
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

        # create_file(html_path,html,"w")#漫画html写文件
        comic_name_lenth()
        self.Clear2()
        self.ui.listWidget_2.addItems(keys_data)
        self.Clear3()
        self.ui.listWidget_3.addItems(keys_data)
        QMessageBox.information(
        self.ui,
        '删除成功',
        "【{}】已删除".format(comic_name))

    '''漫画打包部分'''
    def zip_start(self):
        self.ui.listWidget_3.addItems(keys_data)
        self.ui.listWidget_3.itemClicked.connect(self.zip_handler)
        self.ui.progressBar_3.reset()
    def zip_handler(self):
        global keys_data_source, global_var_list, comic_name
        list_item3 = self.ui.listWidget_3.currentItem()
        comic_name = list_item3.text()
        self.dow_path = filepath+"\\Download\\"+comic_name
        if(os.path.exists(self.dow_path+"\\打包好啦！")):
            QMessageBox.warning(
                self.ui,
                '打包过啦！',
                f'【{comic_name}】已经打包过啦！')
        elif(os.path.exists(self.dow_path)):
            self.Clear3()
            self.ui.listWidget_3.addItem(comic_name)
            zip_confirm = QMessageBox.question(
                self.ui,
                '确认',
                '确定要打包【{}】吗？'.format(comic_name))
            if zip_confirm == QMessageBox.Yes:
                self.zip()
            else:
                self.Clear3()
                self.ui.listWidget_3.addItems(keys_data)
        else:
            QMessageBox.warning(
                self.ui,
                '这漫画你还没下载呢！',
                f'【{comic_name}】尚未下载无法打包！')
            # self.ui.listWidget_3.itemClicked.connect(self.zip_handler)
        # img_lenth = keys_data_source[comic_name]
        # chapter_lenth = len(img_lenth)
        # read_json(name_path,"name")
        # chap_name = eval(global_var_list["name"])
        # chap_name = chap_name[comic_name]
        # dow_path = filepath+"\\Download\\"+comic_name
        # os.mkdir(dow_path+"\\打包好啦！")

        # zipdel_confirm = QMessageBox.question(
        #     self.ui,
        #     '确认',
        #     '确定要删除源文件吗？')
        # self.ui.progressBar_3.setRange(0,chapter_lenth)
        # for i in range(chapter_lenth):
        #     self.ui.progressBar_3.setValue(int(i))
        #     i = str(i)
        #     zip_name = dow_path + "\\打包好啦！\\" + chap_name[i]+'.zip'
        #     for j in range(img_lenth[i]):
        #         img = dow_path +"\\"+ chap_name[i] + '\\' + str(j) + '.jpg'
        #         files.append(img)
        #     file2zip(zip_name,files)
        #     if zipdel_confirm == QMessageBox.Yes:
        #         remove_file(dow_path +"\\"+ chap_name[i])
        #     files = []
    def zip(self):
        global comic_name, keys_data_source
        self.files = []
        img_lenth = keys_data_source[comic_name]
        chapter_lenth = len(img_lenth)
        read_json(name_path,"name")
        chap_name = eval(global_var_list["name"])
        chap_name = chap_name[comic_name]
        # dow_path = filepath+"\\Download\\"+comic_name
        os.mkdir(self.dow_path+"\\打包好啦！")

        zipdel_confirm = QMessageBox.question(
            self.ui,
            '确认',
            '是否要删除源文件？')
        self.ui.progressBar_3.setRange(0,chapter_lenth-1)
        for i in range(chapter_lenth):
            self.ui.progressBar_3.setValue(int(i))
            i = str(i)
            zip_name = self.dow_path + "\\打包好啦！\\" + chap_name[i]+'.zip'
            for j in range(img_lenth[i]):
                img = self.dow_path +"\\"+ chap_name[i] + '\\' + str(j) + '.jpg'
                self.files.append(img)
                QApplication.processEvents()#防假死
            file2zip(zip_name,self.files)
            if zipdel_confirm == QMessageBox.Yes:
                remove_file(self.dow_path +"\\"+ chap_name[i])
            self.files = []
        QMessageBox.information(
            self.ui,
            '打包完成',
            f'【{comic_name}】已打包完成')
        self.ui.progressBar_3.reset()
        self.Clear3()
        self.ui.listWidget_3.addItems(keys_data)

    '''漫画导入部分'''
    def reset_folder(self):
        read_json(setting_path,"setting")
        global_var_list['setting'] = eval(global_var_list['setting'])
        global_var_list['setting']['current_import_src'] = global_var_list['setting']['default_import_src']
        create_file(setting_path,json.dumps(global_var_list['setting'],ensure_ascii=False),"w")#目录写入json文件
        self.ui.tab4_label_currentsrc.setText('当前本地漫画导入文件夹路径为：' + global_var_list['setting']['default_import_src'])
    def open_import_folder(self):
        read_asjson(setting_path,'setting')
        current_import_src = global_var_jsonlist['setting']['current_import_src']#读取当前漫画导入文件夹路径
        print(current_import_src)
        os.startfile(current_import_src)
        # os.system('start explorer '+ current_import_src)
    def edit_folder(self):
        filePath = QFileDialog.getExistingDirectory(self.ui, "选择漫画导入文件夹路径")
        print(filePath)
        read_json(setting_path,"setting")
        global_var_list['setting'] = eval(global_var_list['setting'])
        # print(global_var_list['setting'])
        # print(global_var_list['setting']['current_import_src'])
        if filePath != '':
            global_var_list['setting']['current_import_src'] = filePath
            create_file(setting_path,json.dumps(global_var_list['setting'],ensure_ascii=False),"w")#目录写入json文件
        self.ui.tab4_label_currentsrc.setText('当前本地漫画导入文件夹路径为：' + global_var_list['setting']['current_import_src'])

    def show_bardetials(self,content):#更新进度条下面的文本
        self.ui.label_progressBar_2.setText(str(content))
        #time.sleep(0.2)

    def comics_import(self):
        read_asjson(setting_path,'setting')
        current_import_src = global_var_jsonlist['setting']['current_import_src']#读取当前漫画导入文件夹路径
        print('1-----------------------------------------------------------------------\n')
        files, dirs, files2, dirs2, chapter, pages, names, img_src=[],[],[],[],[],[],[],[]
        print(global_var_jsonlist['setting']['current_import_src'])
        for item in os.listdir(current_import_src):
            item = current_import_src +'/'+ item
            print(item)
            if os.path.isfile(item):
                files.append(item)
            elif os.path.isdir(item):
                dirs.append(item)
        print(f"files：{files};  dirs：{dirs}")

        print('2-----------------------------------------------------------------------\n')
        dirs_dict = {}
        # for x in range(len(dirs)):

        comics_len = len(dirs)
        self.ui.progressBar_4.setRange(0,comics_len)#进度条范围
        for i in range(comics_len):
            self.ui.label_progressBar_3.setText('(当前任务：'+str(dirs[i]+')总进度：').replace(current_import_src+'/',''))#总进度条的文本
            json_write(setting_path,dirs[i],0)
            read_asjson(setting_path,'setting')
            # print()
            if global_var_jsonlist['setting'][dirs[i]]=='0':#判断是否导入过；文件目录：0（未导入）或1（已经导入过）
                file_len = len(os.listdir(dirs[i]))
                self.ui.progressBar_2.setRange(0,file_len-1)#进度条范围
                y=0
                for item in os.listdir(dirs[i]):
                    print(f'item2: {item}')
                    item =  dirs[i] +'/'+ item
                    print(item)
                    if os.path.isfile(item):
                        print(f'file: {item}')
                        files2.append(item)
                        y+=1
                        self.ui.progressBar_2.setValue(y)#设进度条当前值
                        QApplication.processEvents()#防假死
                        self.show_bardetials(item)#进度条下面的文本
                    elif os.path.isdir(item):
                        dirs2.append(item)
                        print(f'dir: {item}')
                        QApplication.processEvents()#防假死
                dirs_dict[dirs[i]+'_files'] = files2
                dirs_dict[dirs[i]+'_dir'] = dirs2
                self.temp = dirs2
                files2, dirs2 = [],[]
                # print(dirs[i])
                print('\n')
            if(self.temp == []):
                self.ui.progressBar_4.setValue(i+1)#设进度条当前值
                QApplication.processEvents()#防假死
                #self.barupdated_flag = False
                #self.barupdated_count = i+1
        print(f"files2：{files2};  dirs2：{dirs2}")
        print('\n\n\n')
        print(dirs_dict)
        #self.ui.progressBar_2.reset()
        #time.sleep(3)
        #self.ui.progressBar_2.setValue(0)#进度条归零

        print('3-----------------------------------------------------------------------\n')

        for i in range(len(dirs)):
            if global_var_jsonlist['setting'][dirs[i]]=='0':
                dirs_dict_dir = dirs_dict[dirs[i]+'_dir']
                if dirs_dict_dir:
                    # tem_dict = {}
                    files3, dirs3 = [],[]
                    for j in range(len(dirs_dict_dir)):
                        file_len = len(os.listdir(dirs_dict_dir[j]))
                        self.ui.progressBar_2.setRange(0,file_len-1)#进度条范围
                        y=0
                        for item in os.listdir(dirs_dict_dir[j]):
                            y+=1
                            item =  dirs_dict_dir[j] +'/'+ item
                            print(item)
                            if os.path.isfile(item):
                                print(f'file: {item}')
                                files3.append(item)
                                self.ui.progressBar_2.setValue(y)#设进度条当前值
                                QApplication.processEvents()#防假死
                                self.show_bardetials(item)#进度条下面的文本
                            elif os.path.isdir(item):
                                dirs3.append(item)
                                print(f'dir: {item}')
                        print(f'dirs_dict: {dirs_dict}')
                        dirs_dict[dirs_dict_dir[j]+'_files'] = files3
                        dirs_dict[dirs_dict_dir[j]+'_dir'] = dirs3
                        files3, dirs3 = [],[]

                    self.ui.progressBar_4.setValue(i+1)#设进度条当前值
                    QApplication.processEvents()#防假死

        print(dirs_dict)
        self.ui.progressBar_2.reset()#进度条重置
        #time.sleep(3)
        #self.ui.progressBar_2.setValue(0)#进度条归零

        #json写入

        # 章节名称写入
        for tem in dirs:
            tem = tem.replace(global_var_jsonlist['setting']['current_import_src']+'/','')
            names.append(tem)
        for x in range(len(dirs)):
            if global_var_jsonlist['setting'][dirs[x]]=='0':
                if dirs_dict[dirs[x]+'_dir']:
                    chapter_tem = []
                    chapter_tem = dirs_dict[dirs[x]+'_dir']
                    for tem in chapter_tem:
                        tem = tem.replace(dirs[x]+'/','')
                        chapter.append(tem)
                if chapter == []:
                    chapter = ['第一话']

                list_t = []
                len_tem = len(chapter)
                for c in range(len_tem):
                    list_t.append(c)
                chapter_t = dict(zip(list_t,chapter))
                if (os.path.exists(name_path)):
                    with open(name_path, "r",encoding='utf-8') as jsonFile:
                        data = json.load(jsonFile)
                        data = "{" + str(data)[1:-1] + ",'"+names[x]+"': " + "{}}"
                        data = eval(data)
                        data[names[x]] = chapter_t.copy()
                else:
                    data = {}
                    data[names[x]] = chapter_t
                print(chapter_t)
                create_file(name_path,json.dumps(data,ensure_ascii=False),"w")#章节目录名称写入json文件
                chapter_t = []
                chapter = []
        print('\n\n\n')
        print('4-----------------------------------------------------------------------\n')
        # print(dirs_dict[dirs_dict_dir[0]+'_files'])
        print('\n\n\n')
        # print(dirs_dict[dirs[0]+'_files'])
        print('4-----------------------------------------------------------------------\n')
        print('\n\n\n')

        # 每章页数pages写入
        for x in range(len(dirs)):
            read_asjson(setting_path,'setting')
            print(global_var_jsonlist['setting'])
            if global_var_jsonlist['setting'][dirs[x]]=='0':
                print(f'x: {x}')
                dirs_dict_dir = dirs_dict[dirs[x]+'_dir']#第一层目录的子目录们
                chapter_len = len(dirs_dict_dir)
                if chapter_len == 0:
                    chapter_len += 1
                list_t = []
                for k in range(chapter_len):
                    list_t.append(k)
                for y in range(chapter_len):
                    if dirs_dict[dirs[x]+'_dir']:
                        cover_html = dirs_dict[dirs_dict[dirs[x]+'_dir'][0]+'_files'][0]#第2层第一张图做封面
                        tem_index = cover_html.find(filepath.replace('\\','/'))
                        if tem_index != -1:
                            cover_html = cover_html.replace(filepath.replace('\\','/'),'')[1:]

                        for src_tem in dirs_dict[dirs_dict[dirs[x]+'_dir'][y]+'_files']:
                            src_tem = src_tem.replace(current_import_src,'')
                            img_src.append(src_tem)# 漫画图片地址写入

                        pages.append(len(dirs_dict[dirs_dict_dir[y]+'_files']))
                        print(1)
                        print(dirs_dict[dirs_dict_dir[y]+'_files'])
                        #create_file(pages_path,json.dumps(pagesjson_write(x),ensure_ascii=False),"w")#保存漫画页数
                    print(f'len: {len(dirs_dict_dir)}')
                    if dirs_dict[dirs[x]+'_files']:
                        cover_html = dirs_dict[dirs[x]+'_files'][0]#第1层第一张图做封面
                        tem_index = cover_html.find(filepath.replace('\\','/'))
                        if tem_index != -1:
                            cover_html = cover_html.replace(filepath.replace('\\','/'),'')[1:]

                        for src_tem in dirs_dict[dirs[x]+'_files']:
                            src_tem = src_tem.replace(current_import_src,'')
                            img_src.append(src_tem)# 漫画图片地址写入

                        pages.append(len(dirs_dict[dirs[x]+'_files']))
                        print(2)
                        print(dirs_dict[dirs[x]+'_files'])
                        #create_file(pages_path,json.dumps(pagesjson_write(x),ensure_ascii=False),"w")#保存漫画页数
                    print(pages)
                print(f'{x}---------------------------')
                print(f'pages: {pages}; list_t: {list_t}')

                pagestem = dict(zip(list_t,pages))
                if (os.path.exists(pages_path)):#如果dist目录下的pages.json存在
                    jdata = []
                    with open(pages_path,"r",encoding='utf-8') as jsonFile:
                        jdata = json.load(jsonFile)
                        jdata = "{" + str(jdata)[1:-1] + ","+"'"+names[x]+"'"+ ':""}'
                        jdata = eval(jdata)
                        jdata[names[x]] = pagestem.copy()
                else:
                    jdata = {}
                    jdata[names[x]] = pagestem.copy()
                create_file(pages_path,json.dumps(jdata,ensure_ascii=False),"w")#保存漫画页数
                pages = []

                # 封面写入
                cover = """<div onmouseover='bounceon(this)' onmouseout='bounceoff(this)' class='mdui-ripple mdui-hoverable mdui-card mdui-col-md-2 mdui-col-xs-6'><div class='mdui-ripple mdui-hoverable mdui-card-media'><a href='阅读.html?"""+names[x]+"""?locimport'><img src='"""+cover_html+"""'/></a><div class='mdui-card-media-covered'><div class='mdui-card-primary'><div comic_type='locimport'; style='font-weight:900;font-size: large;' onclick='openweb(this)';>"""+names[x]+"""</div></div></div></div></div>"""
                if (os.path.exists(coverjson_path)):
                    with open(coverjson_path,"r",encoding='utf-8') as jsonFile:
                        jcover = json.load(jsonFile)
                        jcover = "{" + str(jcover)[1:-1] + ","+"'"+names[x]+"'"+ ':""}'
                        jcover = eval(jcover)
                        jcover[names[x]] = cover
                else:
                    jcover = {}
                    # print(i-1)1
                    jcover[names[x]] = cover
                create_file(coverjson_path,json.dumps(jcover,ensure_ascii=False),"w")#保存漫画封面地址
                cover,jcover = [],[]

                # 漫画图片地址
                print(x)
                if (os.path.exists(img_path)):
                    with open(img_path,"r",encoding='utf-8') as jsonFile:
                        img_data = json.load(jsonFile)
                        if(x==0):
                            img_data = "{" + str(img_data)[1:-1] + ","+"'"+names[x]+"'"+ ':""}'
                            img_data = eval(img_data)
                            img_data[names[x]] = img_src
                            # print(img_data[names[n]])
                            # print(type(img_data[names[n]]))
                        else:
                            # print(n)
                            # print(type(img_data))
                            img_data[names[x]] = img_src
                else:
                    img_data = {}
                    # print(n)
                    img_data[names[x]] = img_src
                create_file(img_path,json.dumps(img_data,ensure_ascii=False),"w")#保存漫画图片地址
                img_src = []
                json_write(setting_path,dirs[x],1)
                read_asjson(setting_path,'setting')
                combinei()
                #self.ui.progressBar_2.reset()

        #self.ui.progressBar_2.reset()
        comic_name_lenth()
        self.Clear2()
        self.ui.listWidget_2.addItems(keys_data)#更新漫画列表
        QMessageBox.information(
            self.ui,
            '导入成功',
            "【{}】已成功导入".format(names)
        )

app = QApplication([])
app.setWindowIcon(QIcon('assets/title.png'))
Comics = Comic()
Comics.ui.show()
app.exec_()