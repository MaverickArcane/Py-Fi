docker build -t py-fi .
docker run --rm -p 8000:8000 --name py-fi py-fi

# deploy
docker run -d --restart always -p 8000:8000 --name py-fi py-fi
