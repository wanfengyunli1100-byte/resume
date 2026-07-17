import pathlib, os, sys
tmp = pathlib.Path(r'D:\study files\codex\projects\resume\weasy_tmp')
tmp.mkdir(exist_ok=True)
os.environ['TMP'] = str(tmp)
os.environ['TEMP'] = str(tmp)
C = {}
C['N'] = '\u97E6\u6587\u8F69'
C['T'] = '\u7535\u8BDD\uFF1A15112188850'
C['E'] = '\u90AE\u7BB1\uFF1A1446974278@qq.com'
C['J'] = '\u5D4C\u5165\u5F0F\u8F6F\u4EF6\u5F00\u53D1'
C['S'] = '\u5927\u8FDE\u5927\u5B66'
C['M'] = '\u7535\u5B50\u4FE1\u606F\u5DE5\u7A0B'
C['K'] = '\u534E\u4E3AOD\u673A\u8003\u6210\u7EE9'
C['KH'] = '\u524D\u4E24\u9898\u5B8C\u5168\u901A\u8FC7\uFF0C\u7B2C\u4E09\u9898DFS/\u8F83\u96BE\u83B7\u5F97\u90E8\u5206\u5206'
C['K2'] = '\u5168\u7A0B\u4F7F\u7528Python\uFF0C\u72EC\u7ACB\u5B8C\u6210\uFF0C\u672A\u501F\u52A9\u4EFB\u4F55\u5916\u90E8\u5DE5\u5177\u6216\u63D0\u793A'
C['K3'] = '\u5DF2\u901A\u8FC7\u7EFC\u6D4B'
C['S1'] = '\u7F16\u7A0B\u8BED\u8A00'
C['S1V'] = 'Python\uFF08\u719F\u7EC3/\u673A\u8003\u9A8C\u8BC1\uFF09\u3001C/C++\uFF08\u57FA\u7840\u624E\u5B9E\uFF09'
C['S2'] = '\u5D4C\u5165\u5F0F\u5F00\u53D1'
C['S2V'] = 'STM32\u3001ARM Cortex-M\u3001Keil/CubeIDE\u3001UART/SPI/IIC/UDP'
C['S3'] = 'AI\u90E8\u7F72'
C['S3V'] = 'Ollama\u3001QLoRA\u5FAE\u8C03\u3001\u672C\u5730\u6A21\u578B\u90E8\u7F72\uFF08PC\u7AEF\uFF09'
C['S4'] = '\u7B97\u6CD5\u4E0E\u6570\u636E\u7ED3\u6784'
C['S4V'] = '\u54C8\u5E0C\u8868\u3001DFS/BFS\u3001\u5355\u8C03\u6808\u3001\u6ED1\u52A8\u7A97\u53E3\u3001\u52A8\u6001\u89C4\u5212\uFF08\u673A\u8003\u9A8C\u8BC1\uFF09'
C['S5'] = '\u5E94\u7528\u5F00\u53D1'
C['S5V'] = 'Qt/PyQt6\u3001\u5FAE\u4FE1\u5C0F\u7A0B\u5E8F\u3001SQLite\u3001Git\u3001Linux'
C['EDU'] = '\u672C\u79D1'
C['R1'] = '\u5206\u5E03\u5F0F\u667A\u80FD\u5BB6\u5C45\u8BED\u97F3\u63A7\u5236\u7CFB\u7EDF'
C['R1T'] = 'STM32 / Qt (C++) / UDP / AI\u51B3\u7B56\u5F15\u64CE'
C['R1H'] = '\u6838\u5FC3\u4EAE\u70B9\uFF1A\u591A\u8282\u70B9\u5206\u5E03\u5F0F\u67B6\u6784 + AI\u51B3\u7B56\u4E0E\u5D4C\u5165\u5F0F\u8BBE\u5907\u8054\u52A8'
C['R2'] = 'Chatty-Bot \u4E2A\u6027\u5316AI\u684C\u9762\u52A9\u624B'
C['R2T'] = 'Python / PyQt6 / Ollama / QLoRA / n8n / Docker'
C['R2H'] = '\u6838\u5FC3\u4EAE\u70B9\uFF1A\u72EC\u7ACB\u653B\u514B4GB\u663E\u5B58\u90E8\u7F72\u5927\u6A21\u578B + \u53CCAgent\u5DE5\u4F5C\u6D41\u8BBE\u8BA1'
C['R3'] = '\u665A\u98CE\u4E91\u91CC\u2014\u2014\u4E2A\u4EBA\u4F5C\u54C1\u96C6\u5FAE\u4FE1\u5C0F\u7A0B\u5E8F'
C['R3T'] = '\u5FAE\u4FE1\u5C0F\u7A0B\u5E8F / \u4E91\u5F00\u53D1 / JavaScript'
C['R3H'] = '\u6838\u5FC3\u4EAE\u70B9\uFF1A\u5DF2\u5907\u6848\u4E0A\u67B6\uFF0C\u5177\u5907\u5B8C\u6574\u4EA7\u54C1\u843D\u5730\u7ECF\u9A8C'
html = '<!DOCTYPE html>'
html += '<html lang=\"zh-CN\"><head><meta charset=\"UTF-8\"><title>' + C['N'] + '</title>'
html += '</head><body><h1>' + C['N'] + '</h1></body></html>'
f = pathlib.Path(r'D:\study files\codex\projects\resume\resume_od.html')
f.write_text(html, encoding='utf-8')
print('Written:', f.stat().st_size, 'bytes')
import pathlib, os, sys
tmp = pathlib.Path(r'D:\study files\codex\projects\resume\weasy_tmp')
tmp.mkdir(exist_ok=True)
(tmp/'cache').mkdir(exist_ok=True)
os.environ['TMP']=str(tmp); os.environ['TEMP']=str(tmp)
os.chdir(str(tmp))
def S(*cs): return ''.join(chr(c) for c in cs)
C=lambda:0
C.N=S(38886,25991,36713)  # 韦文轩
C.T='15112188850'
C.E='1446974278@qq.com'
C.SCH=S(22823,36830,22823,23398)  # 大连大学
C.MAJ=S(30005,23376,20449,24687,24037,31243)  # 电子信息工程
C.JOB=S(23481,24337,24335,26519,24320,21457)  # 嵌入式软件开发
C.SCOREB=S(21326,20026,79,68,26426,32771,25104,32491)  # 华为OD机考成绩
C.SCORE1=S(21069,20004,39064,23436,20940,20998)  # 前两题完全通过
C.SCORE2=' DFS/'+S(36739,38590,33719,21040,37096,20998,28857)  # /较难获得部分分
C.SCORE3=S(20840,31243,20351,29992)+'Python'+S(65292,29420,31435,23436,25104,65292,26410,20511,21161,20219,20309,22806,25552,31034,12290)  # 全程使用Python，独立完成，未借助任何外部工具或提示。
C.SCORE4=S(24050,36890,36807,32508,21512,32463,27979)  # 已通过综测
# Skills
def SK(t,v): return f'<div class=\"sg\"><span class=\"sg-l\">{t}</span><span class=\"sg-v\">{v}</span></div>'
C.S1=S(32534,31243,35328,35328)  # 编程语言
C.S1V='Python'+S(65288,29087,32451,26426,32771,35777,35781,65289)+'C/C++'+S(65288,22522,30784,25166,23454,65289)  # Python（熟练/机考验证）、C/C++（基础扎实）
C.S2=S(23481,20837,24335,24320,21457)  # 嵌入式开发
C.S2V='STM32 ARM Cortex-M Keil CubeIDE UART SPI IIC UDP'
C.S3='AI '+S(37096,32622)  # AI部署
C.S3V='Ollama QLoRA '+S(24494,35843,27169,22411,37096,32622,65288,80,67,31471,65289)  # Ollama QLoRA 本地模型部署（PC端）
C.S4=S(31639,27861,19982,25968,25454,26519,26500,32467)  # 算法与数据结构
C.S4V=S(21704,24052,34920)+' DFS/BFS '+S(21333,35843,26632)+' '+S(28369,21160,31383,21475)+' '+S(21160,24577,35268,21040,21010)  # 哈希表 DFS/BFS 单调栈 滑动窗口 动态规划+（机考验证）
C.S5=S(24212,29992,24320,21457)  # 应用开发
C.S5V='Qt/PyQt6 '+S(24494,20449,23567,31243,24207)+' SQLite Git Linux'  # Qt/PyQt6 微信小程序 SQLite Git Linux
# Projects
C.P1=S(20998,24067,24335,33021,33030,23478,23621,35828,38899,22768,21046,31995,32479,32473)  # 分布式智能家居语音控制系统
C.P1T='STM32 Qt(C++) UDP AI'+S(20915,31574,24341,25490)  # 决策引擎
C.P1H=S(26680,24515,20142,28857)+' '+'3'+S(20010,'STM32',33410,28857)  # 核心亮点 3个STM32节点
# ... will add more below
html='''<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><title>'''+C.N+'''</title></head><body><h1>'''+C.N+'''</h1><p>'''+C.SCH+''' '''+C.MAJ+'''</p><p>'''+C.JOB+''' '''+C.T+'''</p></body></html>'''
out=pathlib.Path(r'D:\study files\codex\projects\resume\resume_od_new.html')
out.write_text(html, encoding='utf-8')
print('Written:', out.stat().st_size)
