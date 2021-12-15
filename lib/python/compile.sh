# - pip install cython
# - Update files in library
# - Update MANIFEST.in and setup.py with files to be included
# - Change version number in setup.py
# - run ./compile.sh

sudo apt-get install python-dev --fix-missing -y
sudo apt-get install cython 
#sudo pip install cython

sudo rm -r temp
mkdir temp
sudo cp -R src/* temp

cd temp
mkdir build
mkdir Fusion_obj
mkdir CoreControl_obj

sudo cp -R Fusion/* build
cd build
sudo python setup.py build_ext --inplace
cd ..
sudo cp build/build/*.so Fusion_obj
sudo cp build/__init__.py Fusion_obj
sudo rm -r build

mkdir build
sudo cp -R CoreControl/* build
cd build
sudo python setup.py build_ext --inplace
cd ..
sudo cp build/build/*.so CoreControl_obj
sudo cp build/__init__.py CoreControl_obj
sudo rm -r build

sudo mv Fusion/examples .
sudo rm -r Fusion
mkdir Fusion
sudo cp Fusion_obj/* Fusion
sudo mv examples Fusion/.

sudo mv CoreControl/examples .
sudo rm -r CoreControl
mkdir CoreControl
sudo cp CoreControl_obj/* CoreControl
sudo mv examples CoreControl/.

sudo python setup.py sdist
cd ..
sudo cp temp/dist/*.tar.gz ../
sudo rm -r temp