package server

import (
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"net"
	"net/http"

	"github.com/perimeterx/marshmallow"
	"google.golang.org/grpc"
)

type gServer struct {
	UnimplementedServiceServer
}

type Main struct {
	Main struct {
		Temp float32 `json:"temp"`
	} `json:"main"`
}

func (m *gServer) GetWeather(ctx context.Context, request *WeatherRequest) (*WeatherResponse, error) {
	log.Println("Create called")
	url := "https://api.openweathermap.org/data/2.5/weather/?appid=9fa3767c8c72bdd4a47e7c82897e6841&units=metric&q=" + request.GetCity()

	req, err := http.Get(url)
	if err != nil {
		log.Fatalln(err)
	}
	log.Println(req)
	body, _ := ioutil.ReadAll(req.Body)
	tempData := Main{}

	fmt.Println(body)
	result, err := marshmallow.Unmarshal(body, &tempData)
	if err != nil {
		panic(err)
	}
	fmt.Println(tempData.Main.Temp)

	fmt.Println(result)
	return &WeatherResponse{TempInfo: tempData.Main.Temp}, nil

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
