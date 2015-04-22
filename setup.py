#!/usr/bin/env python
from setuptools import setup
import os

os.system("msgfmt po/zh.po -o po/zh.mo")

setup(name='screenkey', version='0.4',
      description='A screencast tool to display keys',

      author='Pablo Seminario',
      author_email='pabluk@gmail.com',
      maintainer='Yuri D\'Elia',
      maintainer_email='wavexx@thregr.org',
      license='GPLv3+',
      keywords='screencast keyboard keys',
      url='https://github.com/wavexx/screenkey',
      download_url='https://github.com/wavexx/screenkey/releases',

      classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: X11 Applications :: GTK',
                   'Intended Audience :: Education',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Topic :: Education',
                   'Topic :: Multimedia :: Graphics :: Presentation',
                   'Topic :: Multimedia :: Video :: Capture'],

      long_description="""
      Screenkey is a useful tool for presentations or screencasts.
      Inspired by ScreenFlick and initially based on the key-mon project code.
      """,

      scripts=['screenkey'],
      packages=['Screenkey'],
      data_files=[('share/applications', ['data/screenkey.desktop']),
                  ('share/doc/screenkey', ['README.rst', 'NEWS.rst']),
                  ('share/locale/zh_CN/LC_MESSAGES/screenkey.mo', ['po/zh.mo'])],
)
