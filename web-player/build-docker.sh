docker build -t web-player .

docker run -d -p 3000:3000  -e STORAGE_SERVER_URL=http://localhost:8080 -t  web-player