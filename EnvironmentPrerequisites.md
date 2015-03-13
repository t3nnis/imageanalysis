# Linux Environment #

To run the scripts, you will need to install in a Linux environment:
  * python-numby-dev
  * python-scipy
  * python imaging library (PIL)
  * pylab (for visualization during development)
  * python-matplotlib


If you want to view the images, the Python Image Library in a Unix environment will want to use the xv image viewer, which can be installed as follows:

```
cd /tmp
wget ftp://ftp.cis.upenn.edu/pub/xv/xv-3.10a.tar.gz
wget http://prdownloads.sourceforge.net/png-mng/xv-3.10a-jumbo-patches-20050501.tar.gz
wget http://bok.fas.harvard.edu/debian/xv/xv-3.10a-jumbo20050501-1.diff.gz
tar xvzf xv-3.10a.tar.gz
tar xvzf xv-3.10a-jumbo-patches-20050501.tar.gz
gzip -d xv-3.10a-jumbo20050501-1.diff.gz
cd xv-3.10a
patch -p1 < ../xv-3.10a-jumbo-fix-patch-20050410.txt
patch -p1 < ../xv-3.10a-jumbo-enh-patch-20050501.txt
patch -p1 < ../xv-3.10a-jumbo20050501-1.diff
chmod 755 debian/rules 
apt-get install libc6-dev libxt-dev libjpeg62-dev libtiff4-dev libpng12-dev
make
sudo cp xv /usr/bin
```