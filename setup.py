from setuptools import setup

setup(name="SysInfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Daragh O'Farrell",
      licence="GPL3",
      packages=['SysInfo'],
      entry_points={'console_scripts':['comp30670_SysInfo=SysInfo.main:main']}
      )