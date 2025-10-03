#  write a code to generate random string
#  create Dockerfile to build image
docker build -f /path/to/your/Dockerfile -t your_image_name:tag .

#   docker build -t amolmagdum25/todo-frontend:1.0 .
#   docker build -t amolmagdum25/todo-backend:1.0 .

#  to try docker image locally execute : docker run -p hostport:containerport -it amolmagdum25/todo:3.0 

#  push image to dockerhub (you need to have sockerhub login), use below commands
#    docker login
#    docker push amolmagdum25/todo-frontend:1.0
#    docker push amolmagdum25/todo-backend:1.0

# command in pod.yaml is commented because each apps docker file has cmd added.