class SYLFKException(Exception):
    def __init__(self,code='',message='Error'):
        self.code=code #异常编号
        self.message=message ＃异常信息
    
    def __str__(self):
        return self.message #当作为字符串使用时，返回异常信息

#节点已经存在
class EndpointExistsError(SYLFKException):
    def __init__(self,message='Endpoint exists'):
        super(EndpointExistsError,self).__init__(message)
#URL已经存在异常

class URLExistsError(SYLFKException):
    def __init__(sekf,message='URL exists'):
        super(URLExistsError,self).__init__(message)
