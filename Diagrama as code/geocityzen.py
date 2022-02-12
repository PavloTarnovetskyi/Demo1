from re import U
from tokenize import group
from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.aws.compute import EC2

graph_attr = {
    "fontsize": "35",
    "bgcolor": "beige"
}

with Diagram("GeoCityzen", show=True, graph_attr=graph_attr):
    
    github = Custom("github", "./png/github.png")
    devops = Custom("DevOps", "./png/DevOps.png")
    jenkins = Custom("", "./png/jenkins.png")
    user = Custom("User", "./png/user.png")
    terraform = Custom("", "./png/terraform.png")
    ansible = Custom("", "./png/ansible.png")
    with Cluster ("AWS"):
        with Cluster("CentOS instance"):
            EC2_1=EC2("EC2")
            centos = Custom("CentOS", "./png/centos.png")
            postgre = Custom("PostgreSQL", "./png/postgre.png")           
        with Cluster("Ubuntu instance"):
            
            EC2_2=EC2("EC2")
            ubuntu = Custom("Ubuntu", "./png/ubuntu.png")
            maven = Custom("", "./png/maven.png")
            tomcat = Custom("TomCat", "./png/tomcat.png")
            geo = Custom("Geocit134", "./png/geo.png")
            java = Custom("", "./png/java.png")
            
           
           
    
    devops >> Edge(label="push")>>jenkins   
    jenkins >> Edge(label="step 1")<<terraform 
    jenkins >> Edge(label="step 2")<<ansible 
    ansible >> Edge(label="setup")>>ubuntu
    ansible >> Edge(label="setup")>>centos
    terraform >> Edge(label="start") >> EC2_1
    terraform >> Edge(label="start") >> EC2_2
    EC2_1 >> Edge(label="create")>> centos
    EC2_2 >> Edge(label="create")>> ubuntu
    tomcat >> geo
    github >> Edge(label="download project")>> ubuntu
    maven >>Edge(label="use")>>java
    user >>Edge(label="")<<tomcat
    ubuntu - Edge(label="ssh") - centos
    tomcat >>Edge(label="use")>>java
    postgre >>Edge(label="")<< geo 
    
   


        