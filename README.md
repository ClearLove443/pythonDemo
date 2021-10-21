Ues fastapi framework

# environment

```bash
python -m pip install virtualenv
python -m virtualenv env --python=python3.7
source env/Scripts/activate
```

# installation

```bash
# pip install autopep8
# pip install fastapi
# pip install "uvicorn[standard]"
```

```bash
pip install -r requirements.txt
```
# run it

```bash
uvicorn main:app --reload
```

# Interactive Api docs upgrad
go to http://127.0.0.1:8000/docs

# sasl issue in windows

thrift.transport.TTransport.TTransportException: Could not start SASL
exec sasl.reg
