from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'friendly-reminder',
    version = '0.0.1',
    author = 'Robert Lützner',
    author_email = 'robert.luetzner@pm.me',
    license = 'GPL-3.0',
    description = 'A CLI tool to stay on touch with your friends',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/rluetzner/friendly-reminder',
    py_modules = ['main', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3.10.2",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        friendly-reminder=main:cli
    '''
)
