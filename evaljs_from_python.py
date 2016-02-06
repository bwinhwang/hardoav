# coding: utf-8

js = """eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('$("5").6("4","3://0.1.2.7/8/d.e?c=b&9=a-f");',16,16,'abc|cdn|vizplay|http|src|video|attr|org|v|hash|3ieZp1nNyLRaBvW2oHC|dlj10pcwuKgzBJAQs0dT4Q|st|f5af40b68b861a2edab05d55d4ff610a|mp4|Gw'.split('|'),0,{}))
"""
js = js.strip()
js
import jsbeautifier
get_ipython().set_next_input(u'res = jsbeautifier.beautify');get_ipython().magic(u'pinfo jsbeautifier.beautify')
res = jsbeautifier.beautify(js)
res
get_ipython().magic(u'ls ')
res = jsbeautifier.beautify_file("./iframe.html")
print(res)
res = jsbeautifier.beautify(js)
res
js
content = open("./iframe.html").read()
content
import re
p = re.compile(r"eval\(*\)")
p.search(js)
p.search(content)
p = re.compile(r"eval")
p.search(content)
import execjs
ajs = """eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('n={"m":l,"k":"4","o":"p","u":"1:\\/\\/0.2\\/t\\/4\\/q","j":"7%","i":"c","b":"a","6":"1:\\/\\/s-9.0.2\\/d\\/e\\/h\\/5.g","f":"1:\\/\\/v.0.2\\/w\\/5.L","K":"7%","J":[],"N":{"6":"1:\\/\\/0.2\\/8\\/R\\/Q.P","I":"1:\\/\\/0.2","H":A,"z":"y-x","B":C},"G":{"F":E,"D":S},"O":"1:\\/\\/0.2\\/8\\/3\\/M.r.3"};',55,55,'videowood|http|tv|swf|pa81|vd56b45bdf197e0|file|100|assets|36193ed7|start|startparam|bestfit|video|n80EE_gSNtt51ZgGYOryng|image|mp4|1454669306|stretching|height|id|167|duration|config|skin|glow|e70630f7de2923138d8c5c2494f4354173cfafe35c18d35e235d5669021dd6e3|flash||view|updateurl|ust|screenshot|right|top|position|true|margin|30|fontsize|false|back|captions|hide|link|tracks|width|jpg|jwplayer|logo|flashplayer|png|videowood_jw|images|20'.split('|')))
"""
execjs.eval(ajs)
execjs.eval(ajs)
ajs = r"""eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('n={"m":l,"k":"4","o":"p","u":"1:\\/\\/0.2\\/t\\/4\\/q","j":"7%","i":"c","b":"a","6":"1:\\/\\/s-9.0.2\\/d\\/e\\/h\\/5.g","f":"1:\\/\\/v.0.2\\/w\\/5.L","K":"7%","J":[],"N":{"6":"1:\\/\\/0.2\\/8\\/R\\/Q.P","I":"1:\\/\\/0.2","H":A,"z":"y-x","B":C},"G":{"F":E,"D":S},"O":"1:\\/\\/0.2\\/8\\/3\\/M.r.3"};',55,55,'videowood|http|tv|swf|pa81|vd56b45bdf197e0|file|100|assets|36193ed7|start|startparam|bestfit|video|n80EE_gSNtt51ZgGYOryng|image|mp4|1454669306|stretching|height|id|167|duration|config|skin|glow|e70630f7de2923138d8c5c2494f4354173cfafe35c18d35e235d5669021dd6e3|flash||view|updateurl|ust|screenshot|right|top|position|true|margin|30|fontsize|false|back|captions|hide|link|tracks|width|jpg|jwplayer|logo|flashplayer|png|videowood_jw|images|20'.split('|')))
"""
execjs.eval(ajs)
js
js = """eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('$("4").5("3","2://0.1.6.7/c/d.b?a=8&9=e");',15,15,'abc|cdn|http|src|video|attr|vizplay|org|dlj10pcwuKgzBJAQs0dT4Q|hash|st|mp4|v|f5af40b68b861a2edab05d55d4ff610a|ZxEwj3fUyO4ypLWYS_qgIw'.split('|'),0,{}))
"""
js
js = r"""eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('$("4").5("3","2://0.1.6.7/c/d.b?a=8&9=e");',15,15,'abc|cdn|http|src|video|attr|vizplay|org|dlj10pcwuKgzBJAQs0dT4Q|hash|st|mp4|v|f5af40b68b861a2edab05d55d4ff610a|ZxEwj3fUyO4ypLWYS_qgIw'.split('|'),0,{}))
"""
js
execjs.eval(js)
jsbeautifier.beautify(ajs)
ajs
res = jsbeautifier.beautify(ajs)
ajs = """eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('n={"m":l,"k":"4","o":"p","u":"1:\\/\\/0.2\\/t\\/4\\/q","j":"7%","i":"c","b":"a","6":"1:\\/\\/s-9.0.2\\/d\\/e\\/h\\/5.g","f":"1:\\/\\/v.0.2\\/w\\/5.L","K":"7%","J":[],"N":{"6":"1:\\/\\/0.2\\/8\\/R\\/Q.P","I":"1:\\/\\/0.2","H":A,"z":"y-x","B":C},"G":{"F":E,"D":S},"O":"1:\\/\\/0.2\\/8\\/3\\/M.r.3"};',55,55,'videowood|http|tv|swf|pa81|vd56b45bdf197e0|file|100|assets|36193ed7|start|startparam|bestfit|video|n80EE_gSNtt51ZgGYOryng|image|mp4|1454669306|stretching|height|id|167|duration|config|skin|glow|e70630f7de2923138d8c5c2494f4354173cfafe35c18d35e235d5669021dd6e3|flash||view|updateurl|ust|screenshot|right|top|position|true|margin|30|fontsize|false|back|captions|hide|link|tracks|width|jpg|jwplayer|logo|flashplayer|png|videowood_jw|images|20'.split('|')))
"""
res = jsbeautifier.beautify(ajs)
res
ajs = r"""eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('n={"m":l,"k":"4","o":"p","u":"1:\\/\\/0.2\\/t\\/4\\/q","j":"7%","i":"c","b":"a","6":"1:\\/\\/s-9.0.2\\/d\\/e\\/h\\/5.g","f":"1:\\/\\/v.0.2\\/w\\/5.L","K":"7%","J":[],"N":{"6":"1:\\/\\/0.2\\/8\\/R\\/Q.P","I":"1:\\/\\/0.2","H":A,"z":"y-x","B":C},"G":{"F":E,"D":S},"O":"1:\\/\\/0.2\\/8\\/3\\/M.r.3"};',55,55,'videowood|http|tv|swf|pa81|vd56b45bdf197e0|file|100|assets|36193ed7|start|startparam|bestfit|video|n80EE_gSNtt51ZgGYOryng|image|mp4|1454669306|stretching|height|id|167|duration|config|skin|glow|e70630f7de2923138d8c5c2494f4354173cfafe35c18d35e235d5669021dd6e3|flash||view|updateurl|ust|screenshot|right|top|position|true|margin|30|fontsize|false|back|captions|hide|link|tracks|width|jpg|jwplayer|logo|flashplayer|png|videowood_jw|images|20'.split('|')))
"""
res = jsbeautifier.beautify(ajs)
res = jsbeautifier.beautify(ajs)
execjs.eval(ajs)
execjs.available_runtimes
execjs.available_runtimes()
execjs.available_runtimes()
p = re.compile(r"eval\(.*\)")
ret = p.search(content)
ret.start
ret.start()
ret.end()
ret.string()
ret.string
get_ipython().magic(u'pinfo2 ret')
get_ipython().magic(u'pinfo ret')
ret.group
ret.group()
ret.groups()
get_ipython().magic(u'pinfo re.search')
re.search(r"eval\(.*\)", js)
re.search(r"eval\(.*\)", ajs)
re.search(r"eval\(.*\)", content)
import jsbeautifier
res = jsbeautifier.beautify(ajs)
res = jsbeautifier.beautify(js)
res
res.split('"')
res.rsplit('"', 2)
res.rsplit('"', 2)[-1]
res.rsplit('"', 2)[-2]
ret = execjs.eval(ajs)
ret.keys()
ret["file"]
