from grpc_tools import protoc

protoc.main((
    '',
    '--proto_path=proto',
    '--python_out=.',
    '--grpc_python_out=.',
    '--pyi_out=.',
    'proto/inference.proto',
))
