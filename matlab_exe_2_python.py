# exe 파일 만들기 위한 matlab 명령창
# mcc -m 파일이름.m

import subprocess


def execute_exefile():
    subprocess.call(["point.exe"])
