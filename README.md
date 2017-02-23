# Directory Search

This script allows you search all the .txt files in a directory (including all subdirectories) for two phrases a maximum of _n_ characters apart.

## Download
https://raw.githubusercontent.com/dmurawsky/python-directory-search/master/search.py

## Inline Usage
```shell
$ python search.py test-dir 'god' 'divine' 200
```
Or for current directory:
```shell
$ python search.py . 'god' 'divine' 200
```

## Input Usage
```shell
$ python search.py
__Directory to search:__ test-dir
__First search phrase:__ god
__Second search phrase:__ divine
__Max distance between phrases:__ 200
```

## Test
```shell
$ git clone https://github.com/dmurawsky/python-directory-search
$ cd python-directory-search
$ python tests.py
```
