iro-1.10.0.tar.bz2
cd py2cairo*
./waf configure --prefix=/home/PATH/TO/VIRT/
./waf build
./waf install

wget http://pypi.python.org/packages/source/P/PyGTK/pygtk-2.24.0.tar.bz2
cd pygtk*    
export PKG_CONFIG_PATH=/home/PATH/TO/VIRT/lib/pkgconfig
./configure --prefix=/home/PATH/TO/VIRT/
make 
make install
