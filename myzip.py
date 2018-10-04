# coding: utf-8

path = './lenna.png'

def gethexdata():
  data = ''
  with open(path, mode='rb') as f:
    data = f.read().hex()
  return data

def main():
  hexdata = gethexdata()
  intdata = int(hexdata, 16)
  print('test')
  

if __name__ == '__main__':
  main()