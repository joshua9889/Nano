# - pip install cython
# - Update files in library
# - Update MANIFEST.in and setup.py with files to be included
# - Change version number in setup.py
# - run ./compile.sh

sudo rm -r temp
mkdir temp
sudo cp -R src/* temp

cd temp

sudo python setup.py sdist
sudo pip uninstall Fusion -y
sudo pip install dist/*.tar.gz 
cd ..
# sudo cp temp/dist/*.tar.gz ./
sudo rm -r temp
