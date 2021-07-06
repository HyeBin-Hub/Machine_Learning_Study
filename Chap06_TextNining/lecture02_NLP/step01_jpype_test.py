# -*- coding: utf-8 -*-
"""
준비물 : jdk 설치 
java 가상머신 사용을 위한 준비 & 테스트 
"""

import jpype

path = jpype.getDefaultJVMPath()
print(path)
# C:\Program Files\Java\jdk1.8.0_231\jre\bin\server\jvm.dll