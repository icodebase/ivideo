**ivideo** 是一款轻量、强大、好用的视频处理软件。它是一个轻量的工具，而不是像 Davinci Resolve、Adobe Premiere 那样专业的、复杂的庞然大物。ivideo可以满足普通人一般的视频处理需求：压缩视频、转码视频、倒放视频、合并片段、根据字幕裁切片段、自动配字幕、自动剪辑……

ivideo是开源的，你可以免费使用它，但正因为开源，因此插入恶意代码是很容易的事，所以请认准仓库发行页面的下载地址：

- 仓库地址：[AI千集](https://aiqianji.com/icodebase/ivideo) 和 [GitHub](https://github.com/icodebase/ivideo)
- 发行版发布地址：[AI千集 releases](https://aiqianji.com/icodebase/ivideo/releases) 和 [Github releases](https://github.com/icodebase/ivideo/releases)

## 🔨 开发

### 搭建环境

你需要 pip 安装这些包：

```
srt
keyboard
numpy
setuptools
aliyun-python-sdk-core
PyQt5
audiotsm
scipy
cos-python-sdk-v5
tencentcloud-sdk-python
oss2
pyaudio
auditok @ git+https://github.com/amsehili/auditok@v0.1.8
requests
```

其中，pyaudio 很难安装！编译成功有很多要求。所以 Windows 用户可以直接到 [这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) 下载已经被志愿者编译好的 whl 包，用 pip 安装，注意下载对应你 python 版本的包。

Linux 的用户，经 @**[shniubobo](https://github.com/shniubobo)** 的测试，Ubuntu 用户在安装 pyaudio 前只要装这个就行了：

```
sudo apt install portaudio19-dev
```

其他包可以通过[requirements.txt](requirements.txt)安装：

```
pip3 install -r requirements.txt
```

#### 阿里云语音识别 sdk

然后还需要安装阿里云语音识别引擎的sdk， [这篇阿里云官方文档](https://help.aliyun.com/document_detail/120693.html?spm=a2c4g.11186623.6.569.27675df0FENQ6O) 只说了用下面的方法安装：

[下载Python SDK](http://download.taobaocdn.com/freedom/33762/compress/alibabacloud-nls-python-sdk.zip)。

```
 # 打包 python setup.py bdist_egg # 安装 python setup.py install
```

不过有用户反馈可以用下面这个命令直接安装，不过我还没试验：

```
pip3 install aliyun-python-sdk-nls-cloud-meta
```

### 运行问题：

安装完依赖之后开始运行脚本，你可能会遇到这些问题：

- 安装完依赖后，你运行脚本，却发现 `import oss2` 时提示出错：`No module named 'winrandom'`，这时，你需要修改 `Python38\Lib\site-packages\Crypto\Random\OSRNG` 下的 `nt.py` 文件，将 `import winrandom` 修改为：`from Crypto.Random.OSRNG import winrandom`

- `import oss2` 时提示出错：from Crypto.Cipher import AES ImportError: cannot import name 'AES', 处理办法：pip3 uninstall pycrypto && pip3 install pycryptodome
这些问题的原因是一些模块用了其它依赖，而这些其它依赖已经好久没更新了。只能遇到一个问题就搜一下，解决掉。上面这些问题都是我遇到后，在网上找了解法，根据自己的情况做了改动，使得问题得以解决。

**Mac 和 Linux 用户请注意：**

为了在 Windows 上运行时候不弹黑窗口，我在用 subprocess 的时候用了一个  `subprocess.STARTUPINFO()` 类，但是在 Linux 或 Mac 上好像不能用它，所以你们在使用前，要删除几段代码：

首先是末尾的这三行：

```
subprocessStartUpInfo = subprocess.STARTUPINFO()
subprocessStartUpInfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
subprocessStartUpInfo.wShowWindow = subprocess.SW_HIDE
```

然后再全局搜索 `, startupinfo=subprocessStartUpInfo` 将其删掉。理论上就好了。

搭建好环境可以运行之后，如果修改了源代码然，后要进行发布，就应当打包成可以独立运行的exe文件，下面提供两种方法进行编译打包：

### pyinstaller 编译：

先安装上 pyinstaller ：

```
pip3 install pyinstaller
```

直接使用这个命令进行编译：

```python
pip3 install pyinstaller
pip3 install setuptools --upgrade
pyinstaller -wy -i icon.ico ivideo.py  # Windows 用户用这个
pyinstaller -wy -i icon.icns ivideo.py # 为了图标格式兼容，Mac 用户请用这个
```

### 编译后打包后要做的事

编译完成后，还有几个事要做，首先，下载对应系统的 [ffmpeg](http://ffmpeg.org/download.html) 放到编译根目录，再把本 `README.md` 导出成 `README.html` ，同 `icon.ico`、`sponsor.jpg`、`languages` 一起放入编译根目录（Mac 用户放 `icon.icns`），再下载对应系统的 [lux](https://github.com/iawia002/lux/releases) 放入编译根目录。

如果是 Mac 、Linux 打包的，那一定要给编译目录下的可执行文件用 `chmod +x` 授予可执行权限！

然后就可以打包了，Windows 下可以打包成 `7z` 格式，Mac、Linux 用户不要打包` zip`、`7z` 格式！因为这会让可执行文件的权限消失！Mac、Linux 用户可以用 `tar.gz` 或者 `dmg` 格式打包。

建议打包后的命名成类似 `ivideo_Mac_v1.2.0_pyinstaller.dmg` 这样的。如果你是志愿者，为这个项目打包，你也可以在命名后面加上你的 id 等信息。

在发包的时候，建议上传到蓝奏云、天翼云，新建一个文件夹，将包放到这个文件夹里，再把这个文件夹的分享链接发出来，这样，以后要更新的话，只要把新版本放到那个文件夹，分享链接就不用变了。

你可以将打包好的云盘文件夹链接发给作者，作者会把这个链接放到 release 页面。
