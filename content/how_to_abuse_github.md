Title: 手把手教你如何滥用Github, Travis-ci, Coding等资源来建立一个博客
Date: 2016-03-18 17:42:23
Category: UselessSkill

## 这个和一般的博客有什么区别

- 可以在任何地方在Github上写下Markdown语法的内容，然后就会自动编译成html并发布
- 可以绑定自己的域名
- 可以比较自由地改样式
- 和别人家的不太一样，可以装逼
- 静态页面打开比较快
- 可以分国内外进入不同服务器，打开比较快，~~异地多活~~
- 不要钱，不要钱，不要钱

## demo地址

当然就是我的博客啦。。

Github上的地址是：[戳我](https://github.com/faith0811/oreki.moe)

## 准备工作

- 建一个Github账号，如果没有的话
- 建一个Travis-ci账号，并与Github绑定，如果没有的话
- 安装travis的cli命令行工具（``sudo gem install travis``）
- 建一个Coding账号，如果没有的话（可选）
- 保证自己有Python, pip等工具（可选）
- 准备一个域名（可选）

## 让我们开始吧

因为我的博客用了``pelican``，所以我就用他作为教程的一部分了。。如果你喜欢``hexo``之类的，只要替换掉这个部分的内容就行了。

### 第一步，本地安装pelican并且完成配置

一般来说，只要``pip install pelican markdown``就能搞定了。。

如果不行的话，就[戳我](http://docs.getpelican.com/en/3.6.3/install.html)来看官方的安装文档吧。。

然后就依次执行

    :::bash
    mkdir -p ~/projects/yoursite
    cd ~/projects/yoursite
    pelican-quickstart
    
注意把对应的目录名字改掉。。。

然后就会有一个亲切的人机互动界面，你可以按照他的提示，把必要的信息填进去，填错也没关系，之后可以改

然后你的目录大概看上去长这样

```
.
├── Makefile
├── content
├── develop_server.sh
├── fabfile.py
├── output
├── pelicanconf.py
└── publishconf.py
```

然后，你可以在content文件夹内，加入你的第一篇博客，你可以这么写

    :::text
    Title: 呵呵
    Date: 2016-03-18 18:28:12
    Category: HEHE
    
    大家好我是博客主体内容。:)
    
然后保存为``hello_world.md``就行了。。

再之后，你只要做``pelican content``就可以build出html页面并输出到``./output``下。

你可以通过进入output目录，再使用pelican自带的服务器启动预览
```
python -m pelican.server
```

来看看成果吧。进入``http://localhost:8000``来访问。

## 第二步

下次再写。。
