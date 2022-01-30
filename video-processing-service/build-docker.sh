docker build -t video-processing-service .

docker run -p 8000:8080 -e STORAGE_SERVER_URL=http://localhost:8080 -t  video-processing-service