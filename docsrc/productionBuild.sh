#!/bin/bash
#
#===============================================================================
# productionBuild.sh - Shell script to build the Fusion Documentation Suite
#===============================================================================
#
# This script is used to automated the process of making the Fusion 
# documentation suite/website.
#
# Revision History:
#	08-May-2020 <jwa> - Since the build system currently has the correct versions of 
#		the tools needed to generate the documentation site, let's disable the
#		apt-get update(s) and installs here for now.
#	06-May-2020 <jwa> - Since we've added the build instruction source files to
#		the repo, we will copy the .pdf build instruction files from their
#		working locations to the ext_docs folder prior to build.
#   01-Apr-2020 <jwa> - It seems that we now need to specify the version of
#		mkdocs that we install.  We will continue to use v0.17.5 for now.
#
#===============================================================================
#

#sudo apt-get update -y 
#sudo apt-get install libyaml-dev -y
#sudo pip install mkdocs==0.17.5

# 06-May-20 <jwa>
# Copy the final .pdf image files to the ext_docs folder & remove the place holder .txt file
cp Robot_Build_Instruction_Sources/__PDF_Files_for_DocSubSystem/*.pdf  docs/ext_docs -fv
rm docs/ext_docs/Build_Instructions.txt

sudo mkdocs build -v
sudo rm -r ../FusionServer/Src/public/assets/docs/fusion
sudo mkdir ../FusionServer/Src/public/assets/docs/fusion
mv ./site/* ../FusionServer/Src/public/assets/docs/fusion
