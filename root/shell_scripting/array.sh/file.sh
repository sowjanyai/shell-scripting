#! /bin/bash

os=('ubuntu' 'windows' 'kali')
echo "${os[@]}"
echo "{os[1]}"
echo "{!os[a]}"
echo "${#os[@]}"
