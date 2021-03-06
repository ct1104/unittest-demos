# -*- coding:utf-8 -*-
import unittest

class TestFileIter(unittest.TestCase):

    def test_bigfile_iter(self):
      '使用迭代器处理大文本文件，每次读取一行数据'
      fp = open("./static/bigtextfile.txt")
      for line in fp:
        temp = line.split(":")
        print (temp,)
      fp.close()
    
    def test_bigfile(self):
      '一次读取所有行，遍历每一行数据'
      fp = open("./static/bigtextfile.txt")
      lines = fp.readlines()
      for line in lines:
        temp = line.split(":")
        print (temp,)
      fp.close()

if __name__ == '__main__':
  unittest.main()