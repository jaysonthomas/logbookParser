title = 'testTitle'
logbookJs = 'logbook.js'
logbookMathJaxJs = 'logbook-mathjax-config.js'
logbookCss = 'logbook.css'
mainPage = 'index.html'
bioPage = 'bio/jjwt.html'
prevPage = ''
rootPage = 'https://www.youtube.com/watch?v=P48QELwruQs&t=27061s'
nextPage = ''

headerSidebar = f'''
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

<div id="main" class="sidebar1">
  <span style="font-size:10px;cursor:pointer" onclick="openNav()">&#9776;</span>
</div>

<div id="mySidenav" class="sidebar">
  <a href="#1">Installation</a>
  <a href="#2">Temporary way of running Drake locally</a>
  <a href="#3">Learning resources</a>
  <a href="#4">Executing drake cpp examples</a>
  <a href="#7">Reflected inertia tutorial in cpp</a>
  <a href="#10">Questions & todo</a>
</div>
</body>
</html>
'''

content = ''
with open('index.html', 'r', encoding='utf-8') as file:
  found = 0

  for line in file:
    if line.find('<chapter') != -1:
      content += headerSidebar
      found = 1

    if (found):
        content += line

with open('index.html', 'w', encoding='utf-8') as file:        
  file.writelines(content)