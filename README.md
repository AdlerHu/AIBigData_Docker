# Docker

Docker-Compose
  https://docs.docker.com/compose/install/
  
Docker
  For Linux
  https://docs.docker.com/engine/install/centos/
  
Auto-start the Docker
  systemctl enable docker
  systemctl daemon-reload
  
Linux
  su
  yum install git
  mkdir -p /opt/nlp
  cd /opt/nlp
  git clone https://github.com/justin2061/2019_nlp.git
  cd 2019_nlp
  chmod 777 work
  
  ls -la
  cd /opt/nlp/2019_nlp
  docker-compose up -d
  docker-compose logs -f
