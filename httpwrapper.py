
class httpwrapper:
    def __init__(self, url, method="PUT", version="HTTP/1.1"):
        self.url = url
        self.method = method
        self.version = version
        self.headers = {}
        self.body = ""
    
    def addheader(self, key, value):
        self.headers[key] = value
    
    def appendbody(self, data):
        self.body.append(data)
    
    def build(self):
        url = "%s %s %s\r\n" %(self.method, self.url, self.version)
        if self.method == "POST":
            self.addheader("Connection", "Keep-Alive")
        self.addheader("Content-Length", str(len(self.body)))
        headerlist = [ "%s: %s" %(k, v) for k, v in self.headers.items()]
        header = "\r\n".join(headerlist)
        
        if len(self.body) > 0:
            return url + header + "\r\n\r\n" + self.body
        else:
            return url + header + "\r\n"
            
            
#User-Agent：产生请求的浏览器类型。
#Accept：客户端可识别的内容类型列表。
#Host：请求的主机名，允许多个域名同处一个IP地址，即虚拟主机。
#Connection: Keep-Alive

