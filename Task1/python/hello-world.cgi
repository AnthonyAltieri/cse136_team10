#!/usr/bin/python

import datetime
from random import randint

print 'Content-Type: text/html\n\n'
print '<html><head><title>Hello World Python</title>'
randNum = randint( 1, 16 )

def one():
    return 'aqua'
def two():
    return 'black'
def three():
    return 'fuchsia'
def four():
    return 'gray'
def five():
    return 'green'
def six():
    return 'lime'
def seven():
    return 'maroon'
def eight():
    return 'navy'
def nine():
    return 'olive'
def ten():
    return 'red'
def eleven():
    return 'silver'
def twelve():
    return 'teal'
def thirteen():
    return 'white'
def fourteen():
    return 'yellow'
def fifteen():
    return 'purple'
def sixteen():
    return 'blue'
colors = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
    10: ten,
    11: eleven,
    12: twelve,
    13: thirteen,
    14: fourteen,
    15: fifteen,
    16: sixteen,
}
daysArr [0] = 'Sun'
daysArr [1] = 'Mon'
daysArr [2] = 'Tue'
daysArr [3] = 'Wed'
daysArr [4] = 'Thu'
daysArr [5] = 'Fri'
daysArr [6] = 'Sat'

color = colors[ randNum ]()

hour = datetime.datetime.strftime( datetime.datetime.now(), '%H')
day = datetime.datetime.strftime( datetime.datetime.now(), '%a')
date = datetime.datetime.strftime( datetime.datetime.now(), '%d')
monthYear = datetime.datetime.strftime( datetime.datetime.now(), '%b %Y')

#ampm = ''

subtract = int(hour) - 7
if subtract < 0:
  hour = 24 + subtract

  dateNum = datetime.datetime.strftime( datetime.datetime.now(), '%w')
  if(dayNum-1 < 0):
    dayNum = 6
  day = daysArr[dayNum-1];

#if 0 <= int(hour) < 12:
#    hour = 12
#    ampm = 'am'
#else:
#    hour = ( int( hour ) % 12 ) + 1
#    ampm = 'pm'

minsec = datetime.datetime.strftime(datetime.datetime.now(), '%M:%S')
time =  str(day) + ', ' + str(date) + ' ' + monthYear + str( hour ) + ':' + minsec
print '<style>'
print 'body{ background-color: ' + color + ' }'
if randNum == 2 or randNum == 8 or randNum == 16:
    print 'h1{ color: white }'
print '</style><body><h1>Hello World from Python @ ' + time + '</h1>'
print '</body></html>'
