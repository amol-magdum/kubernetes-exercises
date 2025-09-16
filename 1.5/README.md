# #Let's get started!

# write a server file todo.py
# write a docker file to build image
#     docker build -t amolmagdum25/todo:1.1 .
#  push image to dockerhub (you need to have sockerhub login), use below commands
#    docker login
#    docker push amolmagdum25/todo:1.1

# deploy 
# kubectl apply -f ./manifest/deployment.yaml

# change the port in deployment.yaml of your choice. this will set todo app port inside container
# use port-forward to map host port to container port.