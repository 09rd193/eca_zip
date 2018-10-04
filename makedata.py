# coding: utf-8
import csv

n = 16
size = 2 ** n 

def getbintoint(integer, size):
  binnum = format(integer, 'b')
  binnum = binnum.zfill(size)
  return binnum

def onestep(line):
  newline = ''
  for i in range(len(line)):
    x, z = '0', '0'
    if i == 0:
        x, z = '0', line[i + 1]
    elif i == len(line) - 1:
        x, z = line[i - 1], '0'
    else:
        x, z = line[i - 1], line[i + 1]
    newline += '0' if x == z else '1'
  return newline

def main():
  with open('data.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    binnum = getbintoint(1, size)
    for i in range((2 ** (n + 1)) - 2):
      writer.writerow((i+1, int(binnum, 2)))
      binnum = onestep(binnum)

if __name__ == '__main__':
  main()