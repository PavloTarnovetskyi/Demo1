from tokenize import group
from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from diagrams.aws.compute import EC2


graph_attr = {
    "fontsize": "15",
    "bgcolor": "beige"
}

with Diagram("Geo2", show=True, graph_attr=graph_attr):
    with Cluster ("Jankins"):
        github = Custom("github", "./png/github.png")        
        with Cluster("Terraform"):
            EC2=EC2("VirtualBox")
            centos = Custom("CentOS", "./png/centos.png")
            ubuntu = Custom("Ubuntu", "./png/ubuntu.png")
            EC2 >> ubuntu
            EC2 >> centos
            ubuntu - centos
        with Cluster("Ansible"): 
            maven = Custom("", "./png/maven.png")
            tomcat = Custom("TomCat", "./png/tomcat.png")
            geo = Custom("GeoAPP", "./png/geo.png")
            postgre = Custom("PostgreSQL", "./png/postgre.png")
            java = Custom("", "./png/java.png")
            ubuntu - maven 
            ubuntu - tomcat >> geo
            java - maven
            java - tomcat
            java - ubuntu


        github >> ubuntu   
        maven - postgre - centos
        postgre >> geo