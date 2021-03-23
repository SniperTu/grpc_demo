import grpc
import time
from concurrent import futures
from base_package import data_pb2, data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '8080'


class FormatData(data_pb2_grpc.FormatDataServicer):
    # 重写接口函数
    def DoFormat(self, request, context):
        str = request.text
        return data_pb2.actionresponse(text=str.upper())  # 返回一个类实例


def server():
    # 定义服务器并设置最大连接数，corcurrent.futures是一个并发库，类似于线程池的概念
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))  # 创建一个服务器
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)  # 在服务器中添加派生的接口服务
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)  # 添加监听端口
    grpcServer.start()  # 启动服务器
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)  # 关闭服务器


if __name__ == '__main__':
    server()