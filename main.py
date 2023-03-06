# Example usage: clear; python3 main.py /home/jayson/logbook
import os
import os.path as path
import re
import sys

def getHeader(levelFromStart, title):
  relPath = '../' * (levelFromStart)
  logbookJs = relPath + 'logbook.js'
  logbookMathJaxJs = relPath + 'logbook-mathjax-config.js'
  logbookCss = relPath + 'logbook.css'
  mainPage = relPath + 'index.html'
  bioPage = relPath + 'bio/jjwt.html'
  prevPage = ''
  rootPage = ''
  nextPage = ''

  header = f'''
<!DOCTYPE html>
<html>
<head>
  <title>{title}</title>
  <meta name="{title}" content="text/html; charset=utf-8;" />
  <script type="text/javascript" src="{logbookJs}"></script>

  <script src="{logbookMathJaxJs}" defer></script> 
  <script type="text/javascript" id="MathJax-script" defer
    src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js">
  </script>

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/atom-one-light.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js"></script>
  <script>hljs.initHighlightingOnLoad();</script>

  <link rel="stylesheet" type="text/css" href="{logbookCss}" />
</head>

<body onload="loadChapter('');">  

  <div data-type="titlepage" pdf="no">
    <header>
      <h1><a href="{mainPage}" style="text-decoration:none;">Logbook</a></h1>
      <p style="font-size: 18px;"><a href="{bioPage}">Jayson Wynne-Thomas</a></p>
      <p style="font-size: 14px; text-align: right;"> 
        Last modified <span id="last_modified"></span>.</br>
        <script>
        var d = new Date(document.lastModified);
        document.getElementById("last_modified").innerHTML = d.getFullYear() + "-" + (d.getMonth()+1) + "-" + d.getDate();</script>
      </p>
    </header>
  </div>

  <table style="width:100%;" pdf="no"><tr style="width:100%">
    <td style="width:33%;text-align:left;">
      <a class="previous_chapter" href="{prevPage}">Prev Chapter</a>
    </td>
    
    <td style="width:33%;text-align:center;">
      <a href="{rootPage}">Root Chapter</a>
    </td>
    
    <td style="width:33%;text-align:right;">
      <a class="next_chapter" href="{nextPage}">Next Chapter</a>
    </td>
  </tr></table>
  '''
  return header

def getSidebar(headings):
  sidebar = f'''
  <div id="main" class="sidebar1">
    <span style="font-size:10px;cursor:pointer" onclick="openNav()">&#9776;</span>
  </div>

  <div id="mySidenav" class="sidebar">
  '''

  i = 0
  for key, value in headings.items():
    sidebar += f'\n<a href="#{i}">{key}</a>'
    
    for j in range(0, len(value)):
      if (j==0):
        sidebar += f'\n<ul class="no-bullets">'
      sidebar += f'\n  <li><a href="#{i}.{j}">{value[j]}</a></li>'

      if (j==len(value)-1):
        sidebar += f'\n</ul>'
    i += 1

  sidebar += f'\n</div>\n\n'
  return sidebar

def getFooter():
  footer = f'''
</body>
</html>
'''
  return footer

def writeHeaderSidebarAndFooter(levelFromStart, file):
  content = ''
  body = ''
  title = ''
  isMainBodyContent = 0
  sideDict = {}
  sectionHeading = ''
  sid = -1
  ssid = -1
  with open(file, 'r', encoding='utf-8') as f:
    for line in f:
      if (line.find('<chapter') == -1) & (isMainBodyContent == 0):
        continue
      
      try:
        if (isMainBodyContent == 0):
          title = re.search(r'<h1>(.*)</h1>', line).group(1)
          isMainBodyContent = 1 

        if (line.find('<section') != -1):
          sid += 1
          ssid = -1
          
          sectionHeading = re.search(r'<h1>(.*)</h1>', line).group(1)
          if sectionHeading != None:
            sideDict[sectionHeading] = []
          line = f'<section id="{sid}"><h1>{sectionHeading}</h1>\n'
        elif (line.find('<subsection') != -1):
          ssid += 1
          subsectionHeading = re.search(r'<h1>(.*)</h1>', line).group(1)
          if subsectionHeading != None:
            sideDict[sectionHeading].append(subsectionHeading)
          line = f'  <subsection id="{sid}.{ssid}"><h1>{subsectionHeading}</h1>\n'
        elif (line.find('</chapter') != -1):
          body += line
          break
      except AttributeError:
        print(f'{line} in {file}\n\n')
      body += line

  header = getHeader(levelFromStart, title)
  sidebar = getSidebar(sideDict)
  footer = getFooter()
  
  content = header + sidebar + body + footer
  
  with open(file, 'w', encoding='utf-8') as f:        
    f.writelines(content)

if __name__ == "__main__":
  fileCount = 0
  if (len(sys.argv) != 2):
    print(f'Need 2 arguments\n')
  else:
    startpath = sys.argv[1]
    for root, dirs, files in os.walk(startpath):
      if (('.git' in root) or ('toBin' in root) or ('bio' in root)):
        continue
      elif (root == startpath):
        levelFromStart = 0
      else:
        levelFromStart = root.replace(startpath, '').count(path.sep)
        
      for f in files:
        if (('.html' not in f) or 
            ('slides' in root and f!='main.html')):
          continue
        fileCount += 1
        print(root+path.sep+f)
        writeHeaderSidebarAndFooter(levelFromStart, root+path.sep+f)

  print(f'Total file count: {fileCount}.\n')