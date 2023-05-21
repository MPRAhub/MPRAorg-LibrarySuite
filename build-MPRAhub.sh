
mkdir MPRAhub
cd MPRAhub

git clone git@github.com:MPRAhub/MPRAbase-Builder.git
git clone git@github.com:MPRAhub/iSEEindex.git
git clone git@github.com:MPRAhub/MPRAbase.git

cd ../env/
bash build-MPRAbase-image.sh