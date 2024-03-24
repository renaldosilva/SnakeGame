from setuptools import setup, find_packages


with open("README.md", "r") as readme:
    long_description = readme.read()


setup(
    name='snakegame',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/renaldosilva/SnakeGame',
    license='MIT Licence',
    author='Renaldo Silva Santino',
    description='The classic snake game',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
