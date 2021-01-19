import os, zipfile, sys, shutil,json
from tqdm import tqdm

# 请将本工具放在 漫画地址.txt 和章节名称.txt 两文件同一目录下后再运行
# 将 \已下载漫画 目录下的漫画按章节打包为zip压缩包，再用布卡漫画app本地看
global_var_list = {}
def read_json(jpath,name):
    with open(jpath, "r",encoding='utf-8') as jsonFile:
        global_var_list[name] = str(json.load(jsonFile))

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

files = []
fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
#漫画保存路径
chap_path = filepath+'\\dist\\章节名称.json'#章节名称文件保存路径
pages_path = filepath+'\\dist\\pages.json'#漫画每章页数文件路径

with open(pages_path,"r",encoding='utf-8') as jsonFile:
	keys_data = json.load(jsonFile)
	keys_data1 = list(keys_data.keys())
keys_lenth = len(keys_data1)

print("在书架上的漫画有：")
for x in range(keys_lenth):
	print("【{}】 {}".format(x+1,keys_data1[x]))
comic_name = keys_data1[int(input("输入要打包的漫画序号："))-1]
img_lenth = keys_data[comic_name]
chapter_lenth = len(img_lenth)
read_json(chap_path,"name")
chap_name = eval(global_var_list["name"])
chap_name = chap_name[comic_name]

dow_path = filepath+"\\Download\\"+comic_name

os.mkdir(dow_path+"\\打包好啦！")
print("\n压缩打包后是否删除源文件？")
rm_select = input("输入1为是，直接回车否:")

for i in tqdm(range(chapter_lenth),ascii=True):
    i = str(i)
    zip_name = dow_path + "\\打包好啦！\\" + chap_name[i]+'.zip'
    for j in range(img_lenth[i]):
        img = dow_path +"\\"+ chap_name[i] + '\\' + str(j) + '.jpg'
        files.append(img)
    file2zip(zip_name,files)
    if rm_select != "":
        remove_file(dow_path +"\\"+ chap_name[i])
    files = []
print("\n打包好的压缩包在：\n",dow_path+"\\打包好啦！\\")
os.system('pause')