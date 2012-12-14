#!/usr/bin/env python3

import glob
import os
from xml.etree import ElementTree

TEMP = './tmp.svg'

def relativizeSize(fname):
  global svg
  
  #calculate relative sizes if used as xinclude
  root = svg.getroot()
  width = int(root.get('width'))
  height = int(root.get('height'))
  root.set('width','100%')
  root.set('height',str(round( height / width * 100, 2)) + "%")
  root.set('viewBox',"0 0 %s %s" % (width, height))

def rebrand(fname, brand):
  global svg
  
  for e in svg.iterfind(".//{http://www.w3.org/2000/svg}rect[@id='background']"):
    e.set('style', 'fill:url(#%s);' % (brand,))
  

for fname in glob.glob('*svg'):
  global svg
  
  print("processing %s" % (fname))
  os.system("inkscape --vacuum-defs -l %s %s" % (TEMP, fname))
  svg = ElementTree.parse(TEMP)
  rebrand(fname, "BLANK") #BLANK, GNOME, RHEL7
  #relativizeSize(fname)
  svg.write('../getting-started/C/figures/%s' % (fname))
  os.unlink(TEMP)
