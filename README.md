# gRPC service on Golang 


Service using openweathermap api to determine the average temperature in the city

![](header.png)

## Installation

```sh
git clone https://github.com/ternyavsky/rpc_python-go.git
```

Run Golang server:

```sh
go run main.go
```

Run Python client:

```sh
cd client
. ./venv/bin/activate
pip install -r requirements.txt
```

## Usage example
```sh
python client.py [CITY]
```



## Contributing

1. Fork it (<https://github.com/ternyavsky/rpc_python-go/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

