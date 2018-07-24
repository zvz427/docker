 1258  uname -r
 1259  wget -q0- https:get.docker.com/ | sh
 1260  wget -qO- https://get.docker.com/ | sh
 1261  sudo service docker start
 1262  docker run hello-world
 1263  curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -
 1264  sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
 1265  sudo apt-get update
 1266  sudo apt-get install apt-transport-https ca-certificates
 1267  sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
 1268  echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
 1269  sudo apt-get update
 1270  sudo apt-get install docker-engine
 1271  sudo systemctl start docker
 1272  docker run ubuntu:15.10 /bin/echo "Hello world"
 1273  sudo docker run ubuntu:15.10 /bin/echo "Hello world"
 1276  sudo docker run hello-world
 1277  sudo docker run -i -t ubuntu:15.10 /bin/echo 
 1278  docker run -i -t ubuntu:15.10 /bin/bash
 1279  sudo docker run -i -t ubuntu:15.10 /bin/bash
 1280  cat /proc/version
 1282  sudo docker -i -t ubuntu:15.10 /bin/bash
 1283  sudo run docker -i -t ubuntu:15.10 /bin/bash
 1284  sudo docker run -i -t ubuntu:15.10 /bin/bash
 1285  docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
 1286  sudo docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
 1290  docker ps
 1291  docker logs
 1292  docker logs 909f9cb82a30 
 1293  docker ps
 1294  docker logs piring_heyrovsky
 1295  docker logs inspiring_heyrovsky
 1296  docker stop inspiring_heyrovsky
 1299  docker stats --help
 1300  docker stats -a
 1301  docker start b4b8c61f99a3
 1302  docker ps -a
 1303  docker ps -l
 1304  yum install -y util-linux
 1305  apt-get install -y util-linux
 1306  docker inspect --format '{{.State.Pid}}' mynginx

 1308  nsenter --target 6479 --mount --uts --ipc --net --pid
 1315  history 100 > docker_history.txt







帮助
docker version
docker info
docker --help

镜像
docker images 
docker images -a  所有镜像（包括中间镜像层）
docker images -q  显示镜像id
docker images -aq
docker images --digests  显示摘要信息
docker images --digests  --no-trunc  显示所有，不截取

docker search tomcat
docker search -s 30 tomcat 收藏数大于30
docker search -s 30 --no-trunc tomcat 
docker search -s 30 --no-trunc --automated tomcat 自动构建的 

docker pull tomcat
docker pull tomcat:latest

docker rmi hello-world  删除镜像
docker rmi hello-world:latest
docker rmi -f hello-world:latest 强制删除正在运行的镜像
docker rmi hello-world tomcat 删除多个镜像
docker rmi -f $(docker images -qa) 批量删除镜像

新建启动容器(交互式)
-i 交互模式
-t 为容器分配伪终端tty
-d 后台运行容器，返回容器id
--name 为容器指定名称
-P 随机端口映射
-p 指定端口映射

docker run -it 88acsdsd32
docker run -it centos
docker run -it --name mycentos centos
exit 关闭容器退出
ctrl+P+Q 不关闭容器退出
docker ps  当前正在运行的
docker ps -a  所有的
docker ps -l  最近的
docker ps -n 3  最近的3个
docker ps -q  静默模式，只显示容器id
docker ps -lq  
docker ps --no-trunc 不截断输出  

docker start 容器id或容器名  开启容器
docker restart 容器id  重启启容器
docker stop 容器id  停止容器
docker kill 容器id  强制停止容器
docker rm 容器id 删除容器
docker rm -f 容器id 强制删除容器
docker rm -f $(docker ps -aq) 批量强制删除容器
docker ps -aq | xargs docker rm 批量删除容器

新建启动容器(守护式)
docker run -d centos(因为没有前台交互任务，启动后会立刻退出，docker机制决定，docke容器后台运行，必须有一个前台进程)
docker run -d centos /bin/bash -c "while true;do echo zxy;sleep;done"
docker logs -f -t --tail 3 容器id  查看容器日志
	-t 时间戳
	-f 跟随最新打印日志
	--tail 数字，显示最后多少条
docker top 容器id  查看容器进程
docker inspect 容器id  查看容器内部细节---josn格式显示容器细节
docker run -it centos /bin/bash
docker run -it centos 与上一个相同
docker attach 容器id  重新进入到正在运行的容器，启动命令终端，不启动新进程
docker exec -it 容器id /bin/bash 与上一个相同
docker exec -it 容器id ls -l /tmp 在正在运行的容器执行命令，不进入容器,在外面显示结果，打开新终端，启动新进程
docker cp 容器id：/tmp/a.txt 主机目录  从运行的容器中复制文件


联合文件系统底层unionFS
bootfs(boot加载器和内核公用)
rootfs

分层结构
tomcat = kernal + centos + jdk8 + tomcat
多个镜像从相同的基础镜像，共享资源

docker镜像只读，容器启动，新的可写层被加载到镜像顶部，叫容器层，之下叫镜像层

docker commit 提交容器的副本使之成为镜像
docker run -it -p 8888:8080 tomcat  (tomcat服务默认端口为8080，本机的8888映射到tomcat的8080，p指定端口)
docker run -it -P tomcat  (P随机分配，docker ps查看分配的端口)
docker commit -a='zxy' -m='without docs' 容器id zxy/tomcat:v2  提交容器副本，在本地生成新的镜像
docker run -d -p 6666:8080 tomcat  后台方式启动tomcat


docker容器数据卷，主机，容器，容器之间共享数据，保存数据
docker run -it -v /宿主机目录的绝对路径:容器的目录绝对路径 镜像名 会创建文件夹 
docker run -it -v /宿主机目录的绝对路径:容器的目录绝对路径 --privileged=true 镜像名   可解决报错问题
两边的目录可以实现共享
容器停止后，主机修改文件后，数据也可以同步
docker inspect 容器id  可查看挂载的卷的信息

docker run -it -v /宿主机目录的绝对路径:容器的目录绝对路径:ro 镜像名 
容器只能读文件，主机才有读写权限

ls -l --->  ll

dockerfile 是镜像的描述文件
mkdir /mydocker
vim Dockerfile
docker build -f /mydocker/Dockerfile -t zxy/centos .  使用dockerfile生成镜像，使用镜像生成容器，容器内含有目录卷，在主机host上的/var/lib/docker/volumes/下会生成对应的共享目录卷，可用docker inspect 容器id来查看对应的信息

多个容器之间共享容器卷
docker run -it --name node01 zxy/centos  含有自带的容器卷，名为node01
docker run -it --name node02 --volumes-from node01 zxy/centos  定义容器的卷来自node01
docker run -it --name node03 --volumes-from node01 zxy/centos  定义容器的卷来自node01
node02和node03继承自node01的目录卷，在删除容器node01后，共享的目录卷仍然存在
结论：容器之间配置信息的传递，数据卷的生命周期一直持续到没有容器使用它为止，即引用计数为0

dockerfile解析
1、编写dockerfile文件
2、docker bilud 命令执行，获得自定义的镜像
3、docker run

centos的dockerfile的文件内容，继承自元镜像scratch，类似java，python的object类
每条指令都会创建新的镜像层，并对镜像进行提交
保留字指令
FROM
MAINTAINER
RUN
EXPOSE 容器对外暴露的端口
WORKDIR 创建容器后，终端默认登录进来的工作目录
ENV
ADD 将宿主机目录下文件拷贝进镜像，并自动解压tar和url
COPY 只是拷贝
VOLUMES 保存数据并持久化
CMD 指定容器启动时运行的命令，只有最后一个生效
ENTRYPOINT 指定容器启动时运行的命令，
ONBUILD 父镜像被继承后，父镜像可以触发某些操作

FROM centos
MAINTAINER zhuxiangyu<zvz427@163.com>
ENV MYPATH /tmp
WORKDIR $MYPATH
RUN yum -y install vim
RUN yum -y install net-tools
EXPOSE 80
CMD echo $MYPATH
CMD echo 'success-----'
CMD /bin/bash


docker build -f /mydocker/dockerfile -t zxy/centos:v2 .
docker run -it zxy/centos:v2

docker history 镜像id 列出镜像的变更历史

curl -s www.baidu.com 请求网页的页面
curl -s -i www.baidu.com 请求网页的页面,并查看报文头

docker run -it -p 7777:8080 tomcat ls -l 最后的ls -l 会替换镜像的最后一行CMD命令，最后的CMD命令不会执行，tomcat也不会启动。ENTRYPOINT却不会，在原来的命令后追加，比cmd强大


FROM centos
RUN yum -y install curl
CMD ['curl','-s','http://ip.cn']

FROM centos
RUN yum -y install curl
ENTRYPOINT ['curl','-s','http://ip.cn']

FROM centos
RUN yum -y install curl
ENTRYPOINT ['curl','-s','http://ip.cn']
ONBUILD RUN echo 'father onbuild ------------------'

29节，应用docker来自定义tomcat镜像，运行一个容器，在宿主机和容器之间共享文件夹，在主机编写java服务，docker通过容器卷来同步文件，并且会自动发布应用服务，访问本机的指定端口即相当于访问了docker容器内的应用


镜像提交到阿里云
docker commit -a zxy -m'without docs' 容器id zxy/tomcat:v2
docker commit -a zxy -m 'a centos with vim and ip' f85c214eb2ba zxy/mycentos:v7
登录阿里云https://dev.aliyun.com/search.html
创建镜像仓库，本地仓库
docker login --username=zvz427@163.com registry.cn-hangzhou.aliyuncs.com输入密码需要先修改镜像列表上的本地仓库的密码，不然报错
sudo docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/zhuxy_docker/mycentos:[镜像版本号]
docker tag 5fe282a4e314 registry.cn-hangzhou.aliyuncs.com/zhuxy_docker/mycentos:v7.0
docker push registry.cn-hangzhou.aliyuncs.com/zhuxy_docker/mycentos:[镜像版本号]
docker push registry.cn-hangzhou.aliyuncs.com/zhuxy_docker/mycentos:v7.0
后端跟的是阿里云远端仓库的版本号，可与本地相同，也可不同

在阿里云的公有仓库搜索上传的镜像时，搜索名应该为创建时的命名空间/仓库名称，如zhuxy_docker/python3，而非本地的名称，

docker pull registry.cn-hangzhou.aliyuncs.com/zhuxy_docker/python3:1.1.0
下载时需要跟上版本号


centos7 安装笔记 官网

https://docs.docker.com/install/linux/docker-ce/centos/
中文https://docs.docker-cn.com/engine/installation/linux/docker-ce/centos/

cat /etc/redhat-release
lsb_release -a 7不支持

1/ yum安装gcc
	yum -y install gcc
	yum -y install gcc-c++
	gcc -v
2/ 卸载老版本
	sudo yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
3/ 安装需要的软件包
	sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
4/ 设置stable镜像仓库
	不推荐，防火墙网速慢
	sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
    推荐：
    sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
官网可选optional连接外网，不建议设置
5/ 更新yum软件包索引
	sudo yum makecache fast
6/ 安装docker-ce
	sudo yum -y install docker-ce
7/ 启动docker
	sudo systemctl start docker
8/ 测试
	docker version
	docker run hello-world
9/ 配置镜像加速
	mkdir -p /etc/docker
	vim /etc/docker/daemon.json

	sudo mkdir -p /etc/docker
	sudo tee /etc/docker/daemon.json <<-'EOF'
	{
	  "registry-mirrors": ["https://cyzry1ez.mirror.aliyuncs.com"]
	}
	EOF
	sudo systemctl daemon-reload
	sudo systemctl restart docker
	

	ps -ef | grep docker | grep -v grep
10/ 卸载
	sudo systemctl stop docker
	sudo yum -y remove docker-ce
	sudo rm -rf /var/lib/docker

