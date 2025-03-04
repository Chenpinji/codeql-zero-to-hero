import pickle
from socket import socket


def load_data():
    s = socket()
    s.bind(('0.0.0.0', 9999))
    data, addr = s.accept()
    data = s.recv(1024)  
    return data, "OK"

def deserialize(data,nouses):
    b, other = load_data()
    a = data
    pickle.loads(a)  
# Module(
#     body=[Import(names=[alias(name='pickle')]), 
#           Import(names=[alias(name='socket')]), 
#           FunctionDef(name='load_data', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), 
#                       body=[Assign(targets=[Name(id='s', ctx=Store())], 
#                       value=Call(func=Attribute(value=Name(id='socket', ctx=Load()), 
#                       attr='socket', ctx=Load()), args=[], keywords=[])), 
#                       Expr(value=Call(func=Attribute(value=Name(id='s', ctx=Load()), attr='bind', ctx=Load()), args=[Tuple(elts=[Constant(value='0.0.0.0'), Constant(value=9999)], ctx=Load())], keywords=[])), 
#                       Assign(targets=[Tuple(elts=[Name(id='conn', ctx=Store()), Name(id='addr', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='s', ctx=Load()), attr='accept', ctx=Load()), args=[], keywords=[])), 
#                       Assign(targets=[Name(id='a', ctx=Store())], value=Call(func=Attribute(value=Name(id='conn', ctx=Load()), attr='recv', ctx=Load()), args=[Constant(value=1024)], keywords=[])), Return(value=Name(id='a', ctx=Load()))], decorator_list=[], type_params=[]
#                       ), 
#           Assign(targets=[Name(id='data', ctx=Store())], value=Call(func=Name(id='load_data', ctx=Load()), args=[], keywords=[])), 
#           Expr(value=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='loads', ctx=Load()), args=[Name(id='data', ctx=Load())], keywords=[]))], type_ignores=[])

# Module(body=[Import(names=[alias(name='pickle')]), 
#              Import(names=[alias(name='socket')]), 
#              FunctionDef(name='load_data', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='s', ctx=Store())], value=Call(func=Attribute(value=Name(id='socket', ctx=Load()), attr='socket', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='s', ctx=Load()), attr='bind', ctx=Load()), args=[Tuple(elts=[Constant(value='0.0.0.0'), Constant(value=9999)], ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='conn', ctx=Store()), Name(id='addr', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='s', ctx=Load()), attr='accept', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='data', ctx=Store())], value=Call(func=Attribute(value=Name(id='conn', ctx=Load()), attr='recv', ctx=Load()), args=[Constant(value=1024)], keywords=[])), Return(value=Name(id='data', ctx=Load()))], decorator_list=[], type_params=[]), 
#              Assign(targets=[Name(id='data', ctx=Store())], value=Constant(value='1')), 
#              Assign(targets=[Name(id='data', ctx=Store())], value=Call(func=Name(id='load_data', ctx=Load()), args=[], keywords=[])), 
#              Expr(value=Call(func=Attribute(value=Name(id='pickle', ctx=Load()), attr='loads', ctx=Load()), args=[Name(id='data', ctx=Load())], keywords=[]))], type_ignores=[])