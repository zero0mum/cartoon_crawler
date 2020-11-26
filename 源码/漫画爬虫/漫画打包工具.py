import os, zipfile, sys, shutil
from tqdm import tqdm

# 请将本工具放在 漫画地址.txt 和章节名称.txt 两文件同一目录下后再运行
# 将 \已下载漫画 目录下的漫画按章节打包为zip压缩包，再用布卡漫画app本地看

def read_imgfile(path):
    with open(path,'r') as f:
        img_srcs=f.read()
    img_srcs = [str(i)for i in img_srcs]
    img_srcs = ''.join(img_srcs)
    img_srcs1 = img_srcs.split("--#--")

    img_lenth = []
    for j in range(len(img_srcs1)-1):
        img_srcs2=[str(i)for i in img_srcs1[j]]
        img_srcs2 = ''.join(img_srcs2).strip().lstrip().rstrip(',')
        img_srcs2 = img_srcs2.replace('\\','')
        img_srcs = img_srcs2.split("https")
        img_lenth.append(len(img_srcs)-2)
    return img_lenth

def read_chapname(path):
    with open(path,'r',encoding='utf-8') as f:
        chap_name=f.read()
    chap_name = [str(i)for i in chap_name]
    chap_name = ''.join(chap_name)
    chap_name1 = chap_name.split("--#--")
    chap_name1 = chap_name1[0:-1]
    return chap_name1

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
    else:print('文件已不存在！')

files = []
fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
#漫画保存路径
img_path = filepath+'\\漫画地址.txt'#图片地址文件路径
chap_path = filepath+'\\章节名称.txt'#章节名称文件路径
# print(fpath,filepath)
chap_name = read_chapname(chap_path)
dow_path = filepath+"\\已下载漫画\\"
img_lenth = read_imgfile(img_path)
chapter_lenth = len(img_lenth)
# print(chapter_lenth,img_lenth)

os.mkdir(dow_path+"打包好啦！")
print("\n压缩打包后是否删除源文件？")
rm_select = input("输入1为是，直接回车否:")

for i in tqdm(range(chapter_lenth),ascii=True):
    zip_name = str(dow_path+chap_name[i]+".zip")
    zip_name = zip_name.replace("\\","/")
    zip_name = dow_path + "打包好啦！\\" + chap_name[i]+'.zip'
    # print(zip_name)
    for j in range(img_lenth[i]+1):
        img = dow_path + chap_name[i] + '\\' + str(j) + '.jpg'
        files.append(img)
    # print(files)
    file2zip(zip_name,files)
    if rm_select != "":
        remove_file(dow_path + chap_name[i])
    files = []
print("\n打包好的压缩包在：\n",dow_path+"打包好啦！\\")
os.system('pause')