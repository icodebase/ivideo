# coding=utf-8
# python setup.py sdist build
# python setup.py sdist –formats = gztar,zip
# twine upload "dist/ivideo-1.6.10.tar.gz"
# 这是用于上传 pypi 前打包用的


from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ivideo',
    version='2.0.10',
    description=(
        '一款轻量、强大、好用的视频处理软件。'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://aiqianji.com/icodebase/ivideo',
    author='icodebase',
    author_email='icodebase@icodebase.com',
    maintainer='icodebase',
    maintainer_email='icodebase@icodebase.com',
    license='MPL-2.0 License',
    install_requires=[ # 需要额外安装的包
        'srt',
        'keyboard',
        'numpy',
        'scipy',
        'aliyun-python-sdk-core',
        'alibabacloud-nls-java-sdk',
        'PyQt5',
        'audiotsm',
        'cos-python-sdk-v5',
        'tencentcloud-sdk-python',
        'oss2',
        'pyaudio',
        'auditok',
        'pymediainfo',
        'you-get',
        'youtube-dl'
        ],
    packages=['ivideo', 'ivideo/languages', 'ivideo/misc'], # 需要打包的本地包（package）
    package_data={ # 每个本地包中需要包含的另外的文件
        'ivideo': ['*.md',
                '*.ico',
                '*.icns',
                'style.css',
                'sponsor.jpg'],
        'ivideo/languages':['*.*'],
        'ivideo/misc':['README*.html', 'assets/*.*']},

    entry_points={  # Optional
        'gui_scripts': [
            'ivideo=ivideo.ivideo:main',
            'ivideo=ivideo.ivideo:main',
            'ivideo=ivideo.ivideo:main',
            'ivideo=ivideo.ivideo:main'
        ]},


    platforms=["all"],

    classifiers=[
        # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video',

        # Pick your license as you wish
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        ],
    python_requires='>=3.5, <4',

)