#!/bin/bash

# note: -n = no preview
raspivid -fps 25 -vf -n -t 0 -o - | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264