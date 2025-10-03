#  write a code to generate random string
#  create Dockerfile to build image
#     docker build -t amolmagdum25/todo:3.0 .

#  to try docker image locally execute : docker run -it amolmagdum25/todo:3.0 -- sh

#  push image to dockerhub (you need to have sockerhub login), use below commands
#    docker login
#    docker push amolmagdum25/todo:3.0

# command in pod.yaml is commented because each apps docker file has cmd added.

# --------------------------------------#
# image todo:3.0 pushed to dockerhub
# app exposing on port 6050
# deployment also exposing container on 6050
# use port-forward for localhost -> container 6050

# kubectl apply -f ./deployment.yaml