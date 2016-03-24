Title: 手把手教你如何滥用Github, Travis-ci, Coding等资源来建立一个博客
Date: 2016-03-18 17:42:23
Category: UselessSkill

#### 这个和一般的博客有什么区别

- 可以在任何地方在Github上写下Markdown语法的内容，然后就会自动编译成html并发布
- 可以绑定自己的域名
- 可以比较自由地改样式
- 和别人家的不太一样，可以装逼
- 静态页面打开比较快
- 可以分国内外进入不同服务器，打开比较快，~~异地多活~~
- 不要钱，不要钱，不要钱

#### demo地址

当然就是我的博客啦。。

Github上的地址是：[戳我](https://github.com/faith0811/oreki.moe)

#### 准备工作

- 建一个Github账号，如果没有的话
- 建一个Travis-ci账号，并与Github绑定，如果没有的话
- 安装travis的cli命令行工具（``sudo gem install travis``）
- 建一个Coding账号，如果没有的话（可选）
- 保证自己有Python, pip等工具（可选）
- 准备一个域名（可选）

#### 让我们开始吧

因为我的博客用了``pelican``，所以我就用他作为教程的一部分了。。如果你喜欢``hexo``之类的，只要替换掉这个部分的内容就行了。

#### 第一步，本地安装pelican并且完成配置

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

接下来你可以对你的博客进行各个角度的调整，例如增加插件啊，更换模板啊，更改名字啊等等。。

#### 第二步 将源码push至Github

看到这里的时候，你需要保证你的博客已经能够顺利地build了

现在，我们需要在Github上增加一个public的repo来储存你的博客的源码。

创建repo的话，[戳这里](https://github.com/new)

之后就将你刚才创建的源码加入git版本控制中

```
cd /path/to/your/blog/directory
git init
git remote add origin git@github.com:your_name/your_repo.git
git push origin master
```

如果一切顺利，你的代码就被push到github上托管了。

顺带一提的是，你的``output``文件夹内的内容其实是build生成的，应该被排除在版本控制之外。

所以可以在``.gitignore``这个文件中添加``output/``来将整个文件夹去除。

#### 第三步 开启github pages

Github Pages是Github的一个静态页面托管的服务。你可以将静态的html放在git的``gh-pages``分支。

在push至github之后，他就会自动地将该分支内的内容发布至互联网上。

这一步其实非常简单，我们使用一个插件来帮助我们完成这个动作。

这个插件的名字叫``ghp-import``

可以通过pip来安装

```
pip install ghp-import
```

使用的话也很简单，只需要一行命令

```
ghp-import -n output/
```

这行命令会创建gh-pages分支，并填充指定的文件夹下的内容。

再之后我们只需要push该分支至github就行

```
git checkout gh-pages
git push origin gh-pages
```

然后，你就可以通过``http://your_name.github.io/your_repo``来访问你的博客了。

关于怎么使用自己的域名，可以[戳这里](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)

#### 第四步 使用travis-ci来构建博客

其实做到第三步，理论上你已经可以完整地使用你的博客了。

但是，每次都要在cli下执行一坨命令来build博客再上传是不是很麻烦呢，而且也不支持在线编辑。

所以我们需要一个第三方的平台来帮我们构建自己的博客。

在这种情况下，提供开源免费服务的travis-ci就是首选了。

核心的思路就是，每当任何代码被push至blog的master分支后，travis-ci帮我去做build以及push至对应repo的动作。

那问题就来了，怎么让travis-ci拥有权限push代码到我的repo中呢？

在这里，我们需要使用github的一个功能叫做person_access_token

可以通过[戳这里](https://github.com/settings/tokens)来添加token。

只需要勾选public_repo的权限就可以了。。

之后在Makefile中添加了github的方法以及在项目根目录中添加``.travis.yml``文件，来让travis-ci能够识别并正确执行build流程

```
Makefile添加：

github: publish
ifeq ($(TRAVIS_PULL_REQUEST), false)
        ghp-import -n $(OUTPUTDIR)
        @git push -fq https://${GH_TOKEN}@github.com/$(TRAVIS_REPO_SLUG).git gh-pages > /dev/null
endif

.travis.yml文件添加：

language: python
branches:
  only:
  - master
install:
- pip install pelican
- pip install markdown
- pip install ghp-import
script:
- 'make github 2> /dev/null'
env:
  global:
  - GH_TOKEN: 9c898c9b98a877663e4a556989b
```

但是，如果这样做的话，你的person_access_token就会被放进代码库中，会被任何人获取到，存在安全隐患。

所以我们需要对它进行加密。。

还好travis-ci预料到了这样的需求发生，它允许你拥有一些不能被别人知道的变量。

你可以通过命令来创建它

```
cd /path/to/your/repo
travis encrypt GH_TOKEN=9c898c9b98a877663e4a556989b
```

之后travis会给你一长串字符串，这个字符串是通过RSA加密过的，private key是保存在travis服务器上，普通人只能拿到public key，所以相对还是比较安全的。

然后，我们把这个key加入``.travis.yml``中

```
env:
  global:
  - secure: xUPoc+miOMcmsgKu2kpQM5Sl5pRxN1HaNoXK20Iog4ynVo0DRA9gBkvS8Q/H15+ddDqu+fNMblCw2jIbXtUQmaciS1e+Gx1+vtBnD8f2i9JFwwo8P8sdTRX6ucvQuZBRssmrId6qY6qsz+iTri+kG1P5wzNasvMWpvPWgexK7enhDeoaGPeDwLT6KLZmXdsIuGCM1X7kGnVhMYi8pom0dDN4HFYrtzp/PidYFA3xsAOjyjqfgeMdZ1Oxot3281ilvAvY8DDhJ3ZNhkiNFBFAYN2MmQxOLQj4d15puJ8tAr4bKLmxOJkHBP0CE621bDZcLkTkk82TtgJyq3KZWv503ni6LFQ0qmJGEICSYfP/5lWKF/6BQzTBjOoeKCunZKqP1KVgUkXDgAqwo8yv+f3ZTOxD0xoysOnnE+q8QBWlxojWRFx01Ihg/G1kYpIgm+HXzY4huqIXST3Vu1Me4UISeGX/lSXeJ3/kjbCqNRMdeybag7nLSrKudnr/A+6R4gbQFOks6FjEl7HWCX/jSGcNSupIJCd+dhYlsz0KxhYxIuWDmRphGS0mM4z58T71GdL0YNZ40q8NG7fSGGF2j++u8KqtvLIXSj6RpIE6I3qum7iJkZhYEBAFpzQjlT6lfHZg13PTZljk+juW/zm2kDYat5U/10djOUru1jQ/B256xaI=
```

记得删除之前的GH_TOKEN。。。

然后``git push origin master``，并在travis中完成设置，你的博客就可以由travis来build啦。。

#### 第五步 使用Coding为国内分流

因为Coding在国内也提供相类似的服务，并且在国内拥有比较好的访问速度。

所以我们在push build完的html的时候，可以同时push至两个地方（github以及coding）。

再通过dnspod来区分国内外的流量来做分流。

push至coding的方法与github比较相似，在这里就不展开了。如果有问题可以看我blog的repo来参考。。

#### 总结

我已经写的很详细了。。好累啊
