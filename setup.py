from setuptools import setup, find_packages

with open("ReadMe.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    my_license = f.read()

setup(
    name="learn_python",
    version="0.1.0",
    description="Python学习记录",
    author="XiaoTian",
    author_email="sunfeilong1993@gmail.com",
    url="https://github.com/longlongxiao/LearnPython",
    license=my_license,
    packages=find_packages(exclude="doc")
)
