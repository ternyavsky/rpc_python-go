package server

import (
	"context"
	"log"
	"net"
	"net/http"

	"google.golang.org/grpc"
)

type gServer struct {
	UnimplementedServiceServer
}

func (m *gServer) GetWeather(ctx context.Context, request *WeatherRequest) (*WeatherResponse, error) {
	log.Println("Create called")
	url := "https://api.openweathermap.org/data/2.5/weather/?appid=9fa3767c8c72bdd4a47e7c82897e6841&units=metric&q=" + request.GetCity()

	req, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(req)
	return &WeatherResponse{TempInfo: req}, nil

}

func Run() {
	lis, err := net.Listen("tcp", ":3333")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	myInvoicerServer := &gServer{}
	RegisterServiceServer(s, myInvoicerServer)
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
