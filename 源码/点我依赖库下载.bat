@Echo off
chcp 936
Title 安装依赖库库by zero0_mumu
echo 安装BeautifulSoup,tqdm,requests,lxml,selenium,pydub,ffmpeg,simpleaudio,pyside2
echo 返回信息：
python3 -m pip install --upgrade pip
pip3 install requests
pip3 install PyExecJS 
pip3 install beautifulsoup4
pip3 install lxml
pip3 install tqdm
pip3 install selenium==4.2.0
pip3 install pydub
pip3 install ffmpeg
pip3 install simpleaudio
pip3 install pyside2
echo.
echo.
echo 如果返回信息类似：Requirement already satisfied: beautifulsoup4 in d:\hk\python3.82\lib\site-packages (4.9.1)则说明你先前装过了这些个库了，装一次就够了。
echo.
Echo 按任意键关闭窗口 &pause>nul