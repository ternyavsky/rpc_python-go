import weather_pb2, weather_pb2_grpc
import grpc
def main():
    with grpc.insecure_channel("localhost:3333", options=(('grpc.enable_http_proxy', 0),)) as chan:
        stub = weather_pb2_grpc.ServiceStub(chan)
        res = stub.getWeather(weather_pb2.WeatherRequest(city='Lipetsk'))
        print(type(res))

if __name__ == "__main__":
    main()