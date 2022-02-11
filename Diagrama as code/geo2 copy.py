from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.compute import EC2

centos = Custom("CentOS", "./png/centos.png")
github = Custom("github", "./png/github.png")
maven = Custom("maven", "./png/maven.png")
tomcat = Custom("TomCat", "./png/tomcat.png")
ubuntu = Custom("Ubuntu", "./png/ubuntu.png")
graph_attr = {
    "fontsize": "15",
    "bgcolor": "beige"
}

with Diagram("Geo2", show=False, graph_attr=graph_attr):
    with Cluster ("Jankins"):
        with Cluster("Terraform"):
            EC2("HOST")
            EC2 >> ubuntu
            EC2 >> centos
            ubuntu - centos


    



 

