
# Image Stream to Server with gRPC

- image convert to base64
- transfer image by stream

## Install 

```bash
pip install --upgrade protobuf
pip install grpcio
pip install grpcio-tools
```

## Pre_work

```bash
python  -m  grpc_tools.protoc  --python_out=.  --grpc_python_out=.  -I. stream.proto

#说明：
-I=：在proto文件中远程调用的内容，导入路径为实际调用的上一级目录即可。
python_out：指定xxx_pb2.py的输出路径，编译生成处理protobuf相关的代码路径。传入.，则默认生成到当前目录。
grpc_python_out：指定xxx_pb2_grpc.py的输出路径，编译生成处理grpc相关的代码路径，传入.，则默认生成到当前目录。
grpc_tools.protoc：工具包，刚安装的。
-I：这个参数指定协议文件的查找目录。

# 生成的文件中：
xxx_pb2.py：里面有消息序列化类。是用来和protobuf数据进行交互。
xxx_pb2_grpc.py：包含了服务器Stub类和客户端Stub类，以及待实现的服务RPC接口。是用来和grpc进行交互。
```


## Server

```bash
python server_grpc.py
```

## Client
```bash
python client_grpc.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

  
