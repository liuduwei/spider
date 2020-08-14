from pyquery import PyQuery as pq

html = '''
<div>
    <ul id= "2">
         <li class="list">first item</li>
         <li id="container"><a class = "list" href="link2.html">second item</a></li>
         <li id="container"><a class = "list" href="link3.html"><span>third item</span></a></li>
         <li><a href="link4.html">fourth item</a></li>
         <li><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

doc = pq(html)
items = doc('#container')
li = items.siblings('li')
print(li)
