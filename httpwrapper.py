
class httpencode:
    def __init__(self, url, method="PUT", version="HTTP/1.1"):
        self.url = url
        self.method = method
        self.version = version
        self.headers = {}
        self.body = ""
    
    def addheader(self, key, value):
        self.headers[key] = value
    def delheader(self, key)
        del self.headers[key]
    
    def appendbody(self, data):
        self.body.append(data)
    def resetbody(self):
        self.body = ""
    
    def encode(self):
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

class httpdecode:
    def __init__(self, str):
        self.all = str
        self.body = ""
        self.method = ""
        self.url = ""
        self.version = ""
        self.headers = {}
    
def decode(self):
        index0 = self.all.find(b"\r\n\r\n")
        request_predata = self.all[0:index0]
        index1 = request_predata.find(b"\r\n")
        request_first_data = request_predata[0:index1]
        tags = request_first_data.split(" ")
        self.method = tags[0]
        self.url = tags[1]
        self.version = tags[2]
        request_header_data = request_predata[index1:]
        for line in request_header_data.split("\r\n"):
            if line != "":
                line = line.replace(" ","")
                restemp = line.split(":")
                if restemp[0] == "Host" and len(restemp) == 3:
                    restemp[1] = restemp[1] + ":" +restemp[2]
                self.headers[restemp[0]] = restemp[1]
        if index0 >= 0:
            self.body = self.all[index0+4:]
    
    
    
    
    
