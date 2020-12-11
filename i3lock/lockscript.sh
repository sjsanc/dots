#!/bin/bash

# get rid of old bgs
rm ~/.config/i3lock/bg*

IMG=~/.config/i3lock/img.png
BG=~/.config/i3lock/bg.png
scrot $BG
convert $BG -blur 0x5 $BG
convert $BG $IMG -gravity center -composite -matte $BG
i3lock -i $BG
