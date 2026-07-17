 import pathlib, os, subprocess, sys
 N='\u97E6\u6587\u8F69'; T='15112188850'; E='1446974278@qq.com'
 S='\u5927\u8FDE\u5927\u5B66'; M='\u7535\u5B50\u4FE1\u606F\u5DE5\u7A0B'
 title='\u5D4C\u5165\u5F0F\u8F6F\u4EF6\u5F00\u53D1'
 html = '<!DOCTYPE html>\n<html>\n<head>\n<title>'+N+'</title>\n<style>\nbody{font-family:sans-serif}\n</style>\n</head>\n<body>\n<h1>'+N+'</h1>\n<p>'+S+' '+M+'</p>\n</body>\n</html>'
 pathlib.Path(r'D:\study files\codex\projects\resume\resume_od.html').write_text(html, encoding='utf-8')
 print('Written:', len(html))
