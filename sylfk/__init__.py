from werkzeug.serving import run_simple
from sylfk.wsgi_adapter import wsgi_app
from werkzeug.wrappers import Response
from sylfk.exceptions as exceptions
class ExecFunc:
    def __init__(self,func,func_type,**options):
        self.func=func  ＃处理函数
        self.options=options ＃附带函数
        self.func_type=func_type ＃函数类型
class SYLFK:
    def __init__(self,static,folder='static'):
        self.host='127.0.0.1' #默认主机
        self.port=8086 ＃默认端口
        self.url_map={} ＃存放url与Endpoint的映射
        self.static_map={}  ＃存放URL与静态资源的映射
        self.function_map={} ＃存放Endpoint与请求的处理函数的映射
        self.static_folder=static_folder ＃静态资源本地存放路径，默认放在应用目录的static文件夹下

    def dispatch_request(self,request):
        status=200
        headers={
            'Server':'Shiyanlou Framework'
            }

        return Response('<h1>heloo framework</h1>',content_type='text/html',headers=headers,status=status)

    def run(self,host=None,port=None,**options):
        for key,value in options.items():
            if value is not None:
                self.__setattr_(key,value)
        if host:
            self.host=host
        if port:
            self.port=port

        run_simple(hostname=self.host,port=self.port,application=self,**options)


    def __call__(self,environ,start_response):
        return wsgi_app(self,environ,start_response)
    #添加路由规则
    def add_url_rule(self,url,func,func_type,endpoint=None,**options):
        ＃如果节点未命名，使用处理函数的名字
        if endpoint is None:
            endpoint=func.__name__

         ＃抛出url已经存在的异常
         if url in self.url_map:
             raise exceptions.URLExistsError

        #如果类型不是静态资源，并且节点已存在，则抛出节点已经存在异常
        if endpoint in self.function_map and func_type !='static':
            raise exceptions.EndpointExistsError
        #添加URL与节点映射
        self.url_map[url]=endpoint
        #添加节点与请求处理函数的映射
        self.function_map[endpoint]=ExecFunc(func,func_type,**options)
