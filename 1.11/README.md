#  write a code to generate random string
#  create Dockerfile to build image
#     docker build -f Dockerfile.logoutput -t amolmagdum25/log_output_pvc:1.0 .
#     docker build -f Dockerfile.pingpong -t amolmagdum25/pingpong_pvc:1.0 .

#  to try docker image locally execute : docker run -it amolmagdum25/log_write_pod:1.0 sh

#  push image to dockerhub (you need to have sockerhub login), use below commands
#    docker login
#    docker push amolmagdum25/log_output_pvc:1.0
#    docker push amolmagdum25/pingpong_pvc:1.0

# command in pod.yaml is commented because each apps docker file has cmd added.