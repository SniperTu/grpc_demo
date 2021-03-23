import grpc
from base_package import data_pb2_grpc, data_pb2

_HOST = 'localhost'
_PORT = '8080'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = data_pb2_grpc.FormatDataStub(channel=conn)  # 客户端使用Stub类发送请求，参数为频道，为了绑定连接
    response = client.DoFormat(data_pb2.actionrequest(text='hello World!'))  # 返回的结果就是proto中定义的类
    print(response)
    print('received: ' + response.text)


if __name__ == '__main__':
    run()
