import weather_pb2, weather_pb2_grpc
import sys, os
import grpc
def main():
    with grpc.insecure_channel("localhost:3333", options=(('grpc.enable_http_proxy', 0),)) as chan:
        stub = weather_pb2_grpc.ServiceStub(chan)
        city = sys.argv[1]
        res = stub.getWeather(weather_pb2.WeatherRequest(city=city))
        val = int(res.temp_info)
        print(f"The Temperature in {city} {val} degrees")


if __name__ == "__main__":
    main()