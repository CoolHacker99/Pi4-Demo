# Pi4-Demo

## Description
This is a simple python script for copying files between servers over the secure SSH protocol (SCP).

## Usage

First you need to change `config.ini` file and set your own parameters:
- `server` - server ip address
- `port` - port (the default value is 22)
- `user` - username
- `password` - password
- `remote_path` - remote path for uploading your files on the server

```shell
python piscp.py [path to local file/directory]
```

## Install

```shell
git clone https://github.com/CoolHacker99/Pi4-Demo.git && cd ./Pi4-Demo
```
