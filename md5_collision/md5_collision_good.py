#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           �n���?r� ��p
��U�\a:��g&B�,8�������
^kf�1/yF06p%� T^�N��t��ƍI[�篌�0�wj�"�����!]�5+�p=�fՃ�/��O긋�Y��L+�fv�㑡
"""
from hashlib import sha256
if(sha256(blob).hexdigest()=="a61120f5bdf36488dc7933f7bfc53c798296a74948eb1463a94740318fb8b43b"):
        print "I come in peace."
elif(sha256(blob).hexdigest()=="83d3491a8576264c8097f2905592f43f994bfe80542b0a625781e5cadfb90668"):
        print "Prepare to be destroyed!"
else:
        print "Failed!"
