import json,os,shutil,sys

fpath = sys.argv[0]
fpath = os.path.split(fpath)#获取当前.py文件工作目录
filepath = fpath[0].replace("/","\\")
name_path = filepath+'\\dist\\章节名称.json'#章节名称文件保存路径
img_path = filepath+'\\dist\\漫画地址.json'#图片地址文件路径
pages_path = filepath+'\\dist\\pages.json'#漫画每章页数文件路径
coverjson_path = filepath+'\\dist\\cover.json'#漫画封面json路径
html_path = filepath+'\\书架.html'#漫画html文件路径
data_path = filepath+'\\dist\\data.json'

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

with open(pages_path,"r",encoding='utf-8') as jsonFile:
	keys_data = json.load(jsonFile)
	keys_data = list(keys_data.keys())
keys_lenth = len(keys_data)
# print(keys_data)
print("删除工具会删除对应所选漫画的封面,下载的内容,和数据(除了阅读记录保存在浏览器)")
print("在书架上的漫画有：")
for x in range(keys_lenth):
	print("【{}】 {}".format(x+1,keys_data[x]))
comic_name = keys_data[int(input("输入要删除的漫画序号："))-1]
cover_path = filepath+'\\assets\\封面\\'+comic_name+'cover.jpg'#漫画封面路径
comic_download = filepath+"\\Download\\"+comic_name+"\\"#下载漫画地址

total_path = [name_path,img_path,pages_path,coverjson_path,cover_path,data_path,comic_download]

choice = input("\n确定删除【{}】么？输入（y/n）:".format(comic_name))
if (choice=='y' and keys_lenth > 1):
	for y in range(4):
		del_json(total_path[y],comic_name)
	os.remove(cover_path)#删除封面
	if(os.path.exists(total_path[6])):
		shutil.rmtree(total_path[6])#删除下载得漫画
elif (keys_lenth==1):
	for y in range(6):
		os.remove(total_path[y])
	if(os.path.exists(total_path[6])):
		shutil.rmtree(total_path[6])
else:
    restart_program()



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
	create_file(data_path,name_img_pages,'w')#json合并写入name_img_pages.json
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

create_file(html_path,html,"w")#漫画html写文件
print("【{}】已删除".format(comic_name))
os.system('pause')