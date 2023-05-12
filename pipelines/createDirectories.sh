#!/bin/bash
 
directory="./data/row/video"
if [ ! -d "$directory" ]; then
    mkdir -p "$directory"
    echo "Directory '$directory' created."
else
    echo "Directory '$directory' already exists."
fi
directoryigm="./data/row/img"
if [ ! -d "$directoryigm" ]; then
    mkdir -p "$directoryigm"
    echo "Directory '$directoryigm' created."
else
    echo "Directory '$directoryigm' already exists."
fi