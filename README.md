#python TCP/HTTPServer behind NGINX (Docker)
A python TCP/HTTP server (no frameworks)behind an NGINX proxy with basic auth and self-signed SSL, run
 with Docker compose.
##Prerequisities
- Docker and Docker compose
## Build and run
1. Clone the repo:
   git clone https://github.com/Barnabaschidera/python-nginx-docker-project.git
   cd python-nginx-docker-project
2. Build and start both container:
   docker compose up --build
3. Test (self-signed cert, so use -k):
   curl -k -u chidera: Chidex14 https://localhost
   without -u you should get 401 Unauthorised.
4. Stop:
   docker compose down
