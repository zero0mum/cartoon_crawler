	//功能键隐藏
	function hide_button(){
		var action = document.querySelectorAll('.function_button');
		// for(var i=0;i<action.length;i++){action[i].classList.toggle('hide')}
		if(hide_boole){
			$(".function_button").fadeOut()
			mdui.snackbar({
			  message: '已隐藏所有功能键'
			})
			hide_boole = false
		}else{
			$(".function_button").fadeIn()
			mdui.snackbar({
			  message: '已显示所有功能键'
			})
			hide_boole = true
		}
	}
	function show_button(){
		var action = document.querySelector('#wymusic');
		action.classList.toggle('show')
	}
	//加载网易音乐插件
	function randomNum(minNum,maxNum){//生成随机数
		switch(arguments.length){ 
			case 1: 
				return parseInt(Math.random()*minNum+1,10); 
			break; 
			case 2: 
				return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
			break; 
				default: 
					return 0; 
				break; 
		} 
	}
	function wymusic(){
		var tem = Object.keys(musics)
		document.getElementById('music').innerHTML += musics[randomNum(0,tem.length-1)]
	}
	function action_inout(){
		var action = document.querySelector('#wymusic');
		action.classList.toggle('out')
		var icon = document.getElementById('wymusic_icon')
		var icon_dad = document.getElementById('wy_inout')
		if(music_boole){
			icon_dad.innerHTML = '<i id="wymusic_icon" class="function_button mdui-icon material-icons">keyboard_arrow_right</i>'
			music_boole = false
		}else{
			icon_dad.innerHTML = '<i id="wymusic_icon" class="function_button mdui-icon material-icons">keyboard_arrow_left</i>'
			music_boole = true
		}
	}
	function switch_music(){
		var tem = document.getElementById('music')
		tem.getElementsByTagName('iframe')[0].remove()
		wymusic()
	}
	function folder(){
		var e = document.createEvent("MouseEvents");
		e.initEvent("click", true, true);
		document.querySelector("iframe").querySelector(".bg open").dispatchEvent(e);
		// document.getElementsByClassName("bg open")[0].dispatchEvent(e);
	}
	//初始化加载漫画
	if(localStorage.getItem(comic_name+"chapter")){
		setTimeout(function(){history_goto()},100)
	}
	else{
		hishow(1)
		for(num=0;num<pages[0];num++){
		  createimg(num);
		}
		firstone()
		localStorage.setItem(comic_name+"chapter",0)
	}
	for(c=0;c<chaplen;c++){
		catalogCreate(c);//生成目录
	}
	$("#topage_box").fadeOut()
	$("#nextpre_fixed").fadeOut()
	var timer = setInterval(function(){myTimer()},1000);//时间
	lazyload();
	wymusic()//加载网易音乐
	
	//时间：
	function myTimer(){
		var d=new Date();
		var t=d.toLocaleTimeString();
		document.getElementById("time").innerHTML=t;
		if(auto_boole){var tem = sum_temn}else{var tem = 0}
		if(count==parseInt(pages[y-1]-1 + tem)){
		document.getElementById('the_over').innerHTML='本章节已结束';
		}else{document.getElementById('the_over').innerHTML='漫画加载中......'}
	}
	function Get_comicname(){
		var url = document.URL;
		var url = url.split("/")
		comic_name = decodeURI(url[url.length-1].replace(".html",""))
		return comic_name
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
	function show_textfield(){
		$("#topage").fadeIn()
		// document.getElementById("topage").style.display = "block";
	}
	function close_textfield(){
		$("#topage").fadeOut()
		// document.getElementById("topage").style.display = "none";
	}
	function pageto(){
	document.getElementById(localStorage.getItem(comic_name+"page")).scrollIntoView();console.log('执行了哟')}
	function topage(){
		var input_page = parseInt(document.getElementById("topage_input").value)
		//alert(sum_temn+input_page-1)
		document.getElementById(sum_temn+input_page-1).scrollIntoView()
	}
	// 阅读历史跳转
	function pageto(){document.getElementById(localStorage.getItem(comic_name+"page")).scrollIntoView();console.log('执行了哟')}
	function hishow(y){document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];}
	function hiGoto(){y = document.getElementById('chaps').value;add_go(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();}
	function history_goto(){
		if(y==1&&localStorage.getItem(comic_name+"chapter")==0){
			console.log('1特殊？！！！')
			hishow(1)
			for(num=0;num<pages[0];num++){
			  createimg(num);
			}
			firstone()
			setTimeout(function(){pageto()},100)
		}else{
			console.log('2普通？！！！')
			hishow(parseInt(localStorage.getItem(comic_name+"chapter"))+1)
			hiGoto()
			console.log(localStorage.getItem(comic_name+"page"),sum)
			setTimeout(function(){pageto()},300)
		}
	}
	//平滑滚动
	function elementPosition(obj) {
	  var curleft = 0, curtop = 0;
	  if (obj.offsetParent) {
	   curleft = obj.offsetLeft;
	   curtop = obj.offsetTop;
	   while (obj = obj.offsetParent) {
		curleft += obj.offsetLeft;
		curtop += obj.offsetTop;
	   }
	  }
	  return { x: curleft, y: curtop };
	}
	function ScrollToControl(id)
	{
	 var elem = document.getElementById(id);
	 var scrollPos = elementPosition(elem).y;
	 scrollPos = scrollPos - document.documentElement.scrollTop;
	 var remainder = scrollPos % 50;
	 var repeatTimes = (scrollPos - remainder) / 50;
	 ScrollSmoothly(scrollPos,repeatTimes);
	 window.scrollBy(0,remainder);
	}
	var repeatCount = 0;
	var cTimeout;
	var timeoutIntervals = new Array();
	var timeoutIntervalSpeed;
	function ScrollSmoothly(scrollPos,repeatTimes)
	{
	 if(repeatCount < repeatTimes)
	 {
	 window.scrollBy(0,50);
	 }
	 else
	 {
	 repeatCount = 0;
	 clearTimeout(cTimeout);
	 return;
	 }
	repeatCount++;
	cTimeout = setTimeout("ScrollSmoothly('"+scrollPos+"','"+repeatTimes+"')",10);
	}
	//判断元素是否可见区域内
	function elementInView(id,sle){
			if(document.getElementById(id)){
				rect = document.getElementById(id).getBoundingClientRect()
				if(sle==1){
					if(rect.top - window.innerHeight < (wid1/2)*(wid1/localStorage.getItem("wid"))){yInView = true}else{yInView = false}
				}else{
					yInView = rect.top < window.innerHeight && rect.bottom > 0
				}
				return yInView
			}
	}
	//记录阅读进度
	function localstorage(){
		// 判断浏览器是否支持
		if (typeof(Storage) !== "undefined") {
			// 存储
			localStorage.setItem(comic_name+"chapter", y-1);
			localStorage.setItem(comic_name+"page", sum_temn);
		} else {
			alert("对不起，您的浏览器不支持Web Storage，无法记录阅读进度。")
		}
	}
	// function lightness(){
	// 	// document.getElementById('body').setAttribute('class','mdui-theme-primary-indigo mdui-theme-accent-pink mdui-theme-layout-auto mdui-appbar-with-toolbar');
	// 	if(Switch){cover(brightness);Switch = false}
	// 	else if(Switch == false){cover(brightness0);Switch = true}
	// }
	function reloada (){
<!-- 		<a href="javascript:;" id="nav" style="border-radius:60px;" class="mdui-m-a-1 mdui-color-black mdui-ripple mdui-bottom-nav-active mdui-bottom-nav-scroll-hide"></a> -->
		var nava =document.getElementById('fa_div')
		nava.innerHTML=''
		var frameDiv = document.createElement('a')
		var bodyFa = document.getElementById("fa_div");//通过id号获取frameDiv 的父类（也就是上一级的节点）
		bodyFa .appendChild(frameDiv);//把创建的节点frameDiv 添加到父类body 中；
		frameDiv.setAttribute('href',"javascript:;")
		frameDiv.setAttribute('id',"nav")
		frameDiv.setAttribute('style',"border-radius:60px;")
		frameDiv.setAttribute('class',"mdui-m-a-1 mdui-color-black mdui-ripple mdui-bottom-nav-active mdui-bottom-nav-scroll-hide")
	}
	function lazyload(){
		window.onscroll = function(){
			var oScrollTop = $(window).scrollTop();
			if(oScrollTop > sign) {
				sign = oScrollTop;//更新scrollTop
				button_group()
				direction = 'down'
				//console.log('向下');
			}
			if(oScrollTop < sign) {
				sign = oScrollTop//更新scrollTop
				button_group1()
				direction = 'up'
				//console.log('向上');
			}
			for (k=sum_temn;k < sum_temn+pages[y-1]; k++) {
				if (elementInView(k,1)) {
					var tem = sum_temn
					if(auto_boole){var tem = 0}
					count = k - tem//记录已加载页
					var Image = document.getElementById(k)
					//console.log("k：",k)
					Image.setAttribute('src', Image.getAttribute('src-data'))

					y = parseInt(Image.getAttribute('data-chapter'))
					/* console.log(Image.getAttribute('first') != false)
					Image.setAttribute('first', true)
					if(Image.getAttribute('first') == true){
						$("#"+k).fadeOut()
						$("#"+k).fadeIn()
						Image.setAttribute('first', false)
					} */
					//image[count].setAttribute('src', image[count].getAttribute('src-data'));
					// console.log(count)
				}
				if (elementInView(k,0)) {
					step = k//记录可见页
					localStorage.setItem(comic_name+"page", k)
					// snackbar()
					document.getElementById('nav').innerHTML = '第'+y+'章,'+(step-sum_temn+1)+'/'+pages[y-1]+'页'
				}
				document.getElementById('steps').setAttribute('style','width:'+ 100*((step-sum_temn)/(pages[y-1]-1)) +'%;');//进度指示器
				Loading = document.getElementById(step)
				// if(Loading.readyState == 'loading'){console.log('skjguasfgaufvgavfv hjfc bzgjh???!!');Loading.setAttribute('scr','assets/zip.png')}
			}
				// console.log(elementInView(k),typeof(elementInView(k)))
		}
	}
	//菜单
	function actionToggle(){
		var action = document.querySelector('#action');
		action.classList.toggle('active')
	}
	//设置菜单
	function action_setting(sel){
		var action = document.querySelector('#action_all');
		if(sel){
			action.classList.toggle('allout')
		}else{action.classList.toggle('hide')}
	}
	function action_all(){
		action_setting(true)
		action_sliderlight()
		action_slider()
		// action_autonext()
		action_switch()
		// bookshelf()
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
		//console.log(sliderValue.newValue)
		wid = sliderValue.newValue
		localStorage.setItem("wid", sliderValue.newValue);
		for(i=step;i<step+pages[y-1];i++){
			var Image = document.getElementById(i)
			Image.setAttribute('style','width:'+localStorage.getItem("wid")+'px');
		}
	});
	function action_sliderlight(){
		var action = document.querySelector('#sliderb');
		action.classList.toggle('slider')
	}
	var slider = new Slider("#sliderlight", {
		reversed : true
	});
	slider.on("change", function(sliderValue) {
		//console.log(sliderValue.newValue)
		brightness = sliderValue.newValue
		document.getElementsByClassName('cover')[0].style.outlineColor = 'rgba(0,0,0,' + brightness + ')';
		// localStorage.setItem("wid", sliderValue.newValue);
		// for(var i=0;i<pages[y-1]-1;i++)
	});

	// 页数跳转功能
	function pageto_actionin(){
		pagein = $("#topage_slider")
		pagein.empty()
		pagein.append("<input id='chip_slider' type='text' data-slider-min='1' data-slider-max='"+ pages[y-1] +"' data-slider-step='1' data-slider-value='"+ (step-sum_temn+1) +"'/>")
		$("#chip_slider").slider();
		$("#chip_slider").on("slide", function(slideEvt) {
			document.getElementById(sum_temn + slideEvt.value-1).scrollIntoView()
			$("#pageto_current_page").text(slideEvt.value)
			// $("#ex6SliderVal").text(slideEvt.value);
		});
		$("#pageto_current_page").text(step-sum_temn+1)
		$("#pageto_sum_page").text(pages[y-1])
		pagein.fadeIn()
		$("#topage_box").fadeIn()
		$("#nextpre_fixed").fadeIn()
	}
	function pageto_actionout(){
		pageout = $("#topage_slider")
		pageout.fadeOut()
		$("#topage_box").fadeOut()
		$("#nextpre_fixed").fadeOut()
	}
	$("#chip_dad").hover(function(){pageto_actionin()}, function(){pageto_actionout()})

	//自动下一章开关
	function autonext_switch(){
		var tem = document.getElementsByClassName('slider round')
		if(switch_boole){
			//alert('开了')
			mdui.snackbar({
			  message: '自动下一章已开启'
			});
			auto_on()
			switch_boole = false
		}else{
			auto_off()
			//alert('关了')
			mdui.snackbar({
			  message: '自动下一章已关闭'
			});
			switch_boole = true}
	}
	function button_group(){
		document.getElementById('fabs').style = 'position: fixed;display: block;width: 5%;height: 5%;bottom: 1%;right: 1%;transform:translateY(300%);transition: transform 0.7s;transition-timing-function:ease;'
	}
	function button_group1(){
		document.getElementById('fabs').style = 'position: fixed;display: block;width: 5%;height: 5%;bottom: 1%;right: 1%;transform:translateY(0%);transition: transform 0.7s;transition-timing-function:ease;'
	}
	//书架和帮助
	function help(){
		window.open("https://blog.csdn.net/zero_mumu/article/details/107852060",target="_blank");
	}
	function bookshelf(){
		// var action = document.querySelector('#home');
		// action.classList.toggle('out')
		window.open("书架.html",target="_self");
	}
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
		Uclass = uclass
		URL = img_url
		console.log(URL)
		removeimg_now(y)
		listimg_next(y)
		firstone()
	}
	function switchto_local(){
		Uclass = ''
		URL = img_url_loc
		console.log(URL)
		removeimg_now(y)
		listimg_next(y)
		firstone()
	}
	//放大镜
	var zoom_list = []
	$('#zoom_close').fadeOut();
	function zoom(self){
		$(self).lightzoom({
				zoomPower   : 2,    //Default
				glassSize   : 180,  //Default
			});
		zoom_list.push($(self).attr('id'))
		$('#zoom_close').fadeIn();
	}
	function del_zoom(){
		$('#glass').unbind('mousemove');
		for(i=0;i<zoom_list.length;i++){
			$('#'+String(zoom_list[i])).unbind('mousemove');
		}
		zoom_list = []
		$('#glass').remove();
		$("body").css("cursor","default");
		$('#zoom_close').fadeOut()
	}

/* 		拖拽效果
	$('#action').mousedown(function(e) {
		// e.pageX
		var positionDiv = $(this).offset();
		var distenceX = e.pageX - positionDiv.left;
		var distenceY = e.pageY - positionDiv.top;
		//alert(distenceX)
		// alert(positionDiv.left);
	
	$(document).mousemove(function(e) {
		var x = e.pageX - distenceX;
		var y = e.pageY - distenceY;
			if (x < 0) {
			x = 0;
		} 
		else if (x > $(document).width() - $('#action').outerWidth(true)) {
			x = $(document).width() - $('#action').outerWidth(true);
		}
		if (y < 0) {
			y = 0;
		} 
		else if (y > $(document).height() - $('#action').outerHeight(true)) {
			y = $(document).height() - $('#action').outerHeight(true);
		}
		$('#action').css({
			'left': x + 'px',
			'top': y + 'px'
			});
		});
		$(document).mouseup(function() {
		$(document).off('mousemove');
			});
		}); */


	function firstone(){//每次初始先加载2张图片
		if(pages[y-1]<2){
			var firstone = pages[y-1]
		}
		else{var firstone = 2}
		for(var i=0;i<firstone;i++){
			image = document.getElementsByClassName('image');
			image[i].setAttribute('src', image[i].getAttribute('src-data'));
			}
		}
	
	var widths = document.getElementsByClassName('image');

function image_error(image){
	var img=event.srcElement;
	image.setAttribute('src-error-data',image.getAttribute('src-data'))
	image.setAttribute('onclick','reload_image(this)')
	image.setAttribute('src', image.getAttribute('src-data'))
	setTimeout(function(){
		image.setAttribute('src-data','assets/heart-broken.svg')
		image.src="assets/heart-broken.svg"
	},1000)
	img.οnerrοr=null;// 控制不要一直跳动
}
function reload_image(image){
	image.setAttribute('src-data',image.getAttribute('src-error-data'))
	image.setAttribute('src', image.getAttribute('src-error-data'))
	$(image).fadeOut()
	$(image).fadeIn()
	console.log('reload!!!!')
}
function image_loading(image){
	image.src="assets/zip.png"
}
	function createimg(n){
		/*var img = document.createElement('img');
		img.setAttribute('src-data',Uclass+URL[n]);
		img.setAttribute('src','assets/loading.gif');
		img.setAttribute('class','image');
		img.setAttribute('loading','lazy');
		img.setAttribute('onerror','image_error(this)');
		// img.setAttribute('onloadstartNew','image_loading(this)');
		// img.setAttribute('alt','图片错误');
		img.setAttribute('style','display: block;height: auto;width:'+wid+'px');
		img.id = n;*/
		var div = document.getElementById('div');
		img = '<img src-data="'+ Uclass+URL[n] +'"src="assets/loading.gif" class="image" onclick="zoom(this)" loading="lazy" draggable="false" onerror="image_error(this)" style="display: block;height: auto;width:'+ wid +'px" data-chapter='+y+' id="'+ n +'">'
		//div.appendChild(img);
		div.innerHTML += img;
		//div.appendChild(img);
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
		sum_temn = parseInt(sum) + parseInt(y)-1
		for(num=0;num<pages[n-1];num++){
			createimg(sum_temn+num);
		}
	}
	
	function remove_oldimg(){
		selector = "[data-chapter='"+(y-3)+"']"
		console.log(selector)
		if($(selector).length != 0){
			setTimeout("$(selector).remove()", 2000)
		}
	}
	function listimg_next(n){
		console.log(n);
		sum_temn = parseInt(sum) + parseInt(y)-1
		if(chap_name[y-1]&&auto_boole){//阅读完毕提示
			document.getElementById('div').innerHTML += '<p style="font-weight: 1000" class="abstruct" data-sum='+sum+' data-chapter='+(y-1)+' id=abstruct-'+(y-1)+'>已读完：'+chap_name[y-2]+'<br/><br/><br/></p>';
			document.getElementById('div').innerHTML += '<p style="font-weight: 1000" class="abstruct" data-sum='+sum+' data-chapter='+y+' id=abstruct-'+(y-1)+'>下一章：'+chap_name[y-1]+'</p>';
			$('#the_over').css('display','none')
			remove_oldimg();
			if(pages[y-1]>30){
				WaitTime = pages[y-1]/30
			}else{WaitTime = 1}
			setTimeout(function(){$('#the_over').css('display','block')},WaitTime*1000)
		}
		for(num=0;num<pages[n-1];num++){
			createimg(sum_temn+num);
		}
	}
	
	function removeimg_pre(n){
		// console.log(sum);
		if(sum>=0){
		var div1 = document.getElementById("div");
		for(i=sum_temn+pages[n-1];i<sum_temn+pages[n-1]+pages[n];i++){
			console.log(i)
			document.getElementById(i).remove();
			}
		}
	}
	function removeimg_now(n){
		for(i=sum_temn;i<sum_temn+pages[n-1];i++){
			// console.log(i)
			document.getElementById(i).remove();
			}
	}
	function removeimg_next(n,sel){
		if(sel){
			// console.log(sum);
			// console.log(sel)
			if(sum>0){
			var div1 = document.getElementById("div");
			for(i=sum_temn-pages[n-2];i<sum_temn;i++){
				// console.log(i)
				document.getElementById(i).remove();
				}
			}
		}
	}
	function topFunction(sel_top) {
		// console.log(sel_top)
		if(sel_top){
			fade_img(fadeimg_boole)
			document.body.scrollTop = 0;
			document.documentElement.scrollTop = 0;
			fade_img()
		}
	}
	function fade_img(sel){
		if(sel){
			$("#div").fadeOut()
		}else{
			$("#div").fadeIn()
		}
	}
	function next(sel){if(y<chaplen){cnext(sel);topFunction(sel);firstone();show()}}
	function pre(){if(y>=2){cpre();topFunction(true);firstone();show()}}
	function cnext(sel){y++;fade_img(fadeimg_boole);add_next(y);listimg_next(y);removeimg_next(y,sel);firstone();fade_img();document.getElementById('the_over').innerHTML='漫画加载中......';}
	function cpre(){y--;fade_img(fadeimg_boole);add_pre(y);listimg_pre(y);removeimg_pre(y);firstone();fade_img();document.getElementById('the_over').innerHTML='漫画加载中......';}
	function show(){document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];localstorage();document.getElementById("catalog"+(y-1)).setAttribute("class","mdui-color-grey mdui-shadow-6 mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2");}
	function Goto(){y = document.getElementById('chaps').value;fade_img(fadeimg_boole);add_go(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();fade_img();localstorage();}
	function Goto1(){y = document.getElementById('chaps1').value;fade_img(fadeimg_boole);add_go(y);document.getElementById('div').innerHTML="";listimg_next(y);firstone();fade_img();localstorage()}

	function hide_control(){
		var action = document.querySelectorAll('.nextpre');
		for(var i=0;i<action.length;i++){action[i].classList.toggle('hide')}
		$("#nextpre_fixed").fadeOut()
	}
	function auto_off(){//关闭自动下一章及参数更新
		auto_boole = false
		hide_control()
		clearInterval(auto_next)
		document.getElementById('div').innerHTML = ''
		lazyload()
		history_goto()
		document.onkeydown = function(event){//键盘事件左右键控制翻章节
			var e=event || window.event;
			if(e&&e.keyCode == 37){pre()}
			if(e&&e.keyCode == 39){next(true)}
		}
	}
	auto_on()
	function auto_on(){//开启自动下一章及参数更新
		auto_boole = true
		hide_control()
		document.onkeydown = undefined
		auto_next = setInterval(function(){
			if(elementInView('the_over',0)&&document.getElementById('the_over').innerText =='本章节已结束'&&y<pages.length){
				document.getElementById('the_over').innerHTML = '漫画加载中......'
				next(false)
				//alert('abstruct-'+(y-1))
				document.getElementById('abstruct-'+(y-1)).scrollIntoView(false)
			}
			for(i=0;i<pages.length;i++){
				abstruct_id = 'abstruct-'+String(i+1)
				if(elementInView(abstruct_id,0)){
					var abst = document.getElementById(abstruct_id)
					var tem = abstruct_id.split('-')
					if(direction=='up'){
						y = parseInt(tem[1])
						localStorage.setItem(comic_name+"chapter", y-1);
						sum = parseInt(abst.getAttribute('data-sum'))+1-pages[y-1]
						// console.log('add pre')
					}else{
						y = parseInt(tem[1])+1
						localStorage.setItem(comic_name+"chapter", y-1);
						sum = parseInt(abst.getAttribute('data-sum'))
						// console.log('add next')
					}
					sum_temn = parseInt(sum) + parseInt(y)-1
				}
			}
		},200)
	}
	// 目录
	var inst_drawer = new mdui.Drawer('#drawer');
	document.getElementById('toggle').addEventListener('click', function () {
		inst_drawer.toggle();
		turn_grey();
		document.getElementById("catalog" + (y-1)).scrollIntoView()
		if(machine=='other'){
			if(music_hide_boole){
				$("#wymusic").fadeOut()
				music_hide_boole = false
			}else{
				$("#wymusic").fadeIn()
				music_hide_boole = true
			}
		}
	});
	function turn_grey(){
		document.getElementById("catalog"+(y-1)).setAttribute("class","mdui-color-grey mdui-shadow-6 mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2");
	}
	function cashow(y){document.getElementById('chaps').value=y;document.getElementById('chaps1').value=y;document.getElementById('chap_names').innerHTML = chap_name[y-1];document.getElementById("catalog"+(y-1)).setAttribute("class","mdui-color-grey mdui-shadow-6 mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2");}
	function catalogCreate(n){
			var a = document.createElement('a')
			a.setAttribute("onclick","catalogGoto("+ (n+1) +")")
			a.setAttribute("class","mdui-hoverable mdui-list-item mdui-ripple mdx-toc-item mdx-toc-item-h2")
			a.id = "catalog"+n
			var drawer_ul = document.getElementById('drawer_ul')
			drawer_ul.appendChild(a)
			document.getElementById("catalog"+n).innerHTML=chap_name[n];
		}
	function catalogGoto(y){cashow(y);topFunction(true);Goto()}

	//显示遮罩
	function cover(brightness) {
		// if (typeof(ndiv) == 'undefined') {
		// 	ndiv = document.createElement('div');
		// 	ndiv.setAttribute('style', 'position:fixed;top:0;left:0;outline:5000px solid;z-index:99999;');
		ncover = document.getElementsByClassName('cover')
		// 	ncover[0].appendChild(ndiv)
		// } else {
		// 	ndiv.style.display = '';
		// }
		ncover[0].style.outlineColor = 'rgba(0,0,0,' + brightness + ')';
	}
	if(auto_boole == false){
		document.onkeydown = function(event){//键盘事件左右键控制翻章节
			var e=event || window.event;
			if(e&&e.keyCode == 37){pre()}
			if(e&&e.keyCode == 39){next(true)}
		}
	}
	// function OpenNight(){cover(brightness = 0.3);}
	window.addEventListener('keydown', function(e) {
		if (e.altKey && e.keyCode == 38) { //Alt+↑:增加亮度
			if (brightness - 0.01 >= 0) cover(brightness -= 0.01);
		}
		if (e.altKey && e.keyCode == 40) { //Alt+↓:降低亮度
			if (brightness + 0.01 < 0.95) cover(brightness += 0.01);
		}
	}, false);
		
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
function snackbar () {
  mdui.snackbar({
	timeout: 0,
    message: '第'+y+'章,'+step+'/'+pages[y-1]+'页',
    position: 'bottom'
  })
}