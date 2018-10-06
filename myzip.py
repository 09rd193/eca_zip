# coding: utf-8
import sqlite3

datapath = './lenna.png'
dbpath = 'eca.sqlite'

def selectx10(intdata):
  connection = sqlite3.connect(dbpath)
  cursor = connection.cursor()
  query = '''
    select id, x10
    from eca_n16
    where cast(x10 as singed) <= %s
    order by cast(x10 as signed) desc
    limit 1;
  ''' % intdata
  cursor.execute(query)

  id, x10 = 0, 0
  for i, x in cursor:
    id, x10 = i, x

  connection.close()
  return id, int(x10)

def gethexdata(datapath):
  data = ''
  with open(datapath, mode='rb') as f:
    data = f.read().hex()
  return data

def main():
  hexdata = gethexdata(datapath)
  intdata = int(hexdata, 16)
  _id, _x10 = -1, -1
  count = 0
  while 0 < intdata:
    print(count)
    count = count + 1
    print(len(str(intdata)))
    if _x10 < 0:
      _id, _x10 = selectx10(intdata)
      intdata = intdata - _x10
    elif _x10 <= intdata:
      intdata = intdata - _x10
    else:
      _id, _x10 = selectx10(intdata)
      intdata = intdata - _x10
  

if __name__ == '__main__':
  main()