# Pyflicka

Randomly moves the mouse.
Install it on someone else’s computer, just because it’s fun.

Quick install:
```sh
# Creater Folder
test -d ~/.flicka || mkdir ~/.flicka
cd ~/.flicka
# Download build
curl -s https://api.github.com/repos/CeloAugusto/pyflicka/releases/latest \
| grep "browser_download_url.*pyflicka.tar.gz" \
| cut -d : -f 2,3 \
| tr -d \" \
| wget -qi -
# Rename build
mv *pyflicka*tar.gz pyflicka.tar.gz
# Download Makefile
wget -qi https://raw.githubusercontent.com/CeloAugusto/pyflicka/master/Makefile
# Setup & Install
make update
```
