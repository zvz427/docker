cat /etc/redhat-release 

cat /proc/cpuinfo

free -m

df -h


安装python3
https://www.cnblogs.com/s-seven/p/9105973.html
docker容器启动
https://www.cnblogs.com/yanyouqiang/p/8306348.html
安装mysql（mariadb）
https://www.cnblogs.com/river2005/p/6813618.html


 1  systemctl start mariadb
    2  systemctl start mariadb.seervice
    3  cd /usr/bin/
    4  systemctl start mariadb
    5  yum -y install MariaDB-server MariaDB-client
    6  yum -y install mariadb-server mariadb-client
    7  systemctl start mariadb
    8  systemctl enable mariadb
    9  systemctl restart mariadb
   10  mysql_secure_installation
   11  mysql_secure_installation
   12  mysql -uroot -p
   13  vi /etc/my.cnf.d/server.cnf 
   14  vi /etc/my.cnf.d/client.cnf 
   15  vi /etc/my.cnf.d/mysql-clients.cnf 
   16  systemctl restart mariadb
   17  mysql -uroot -p
   18  vi /etc/my.cnf.d/server.cnf 
   19  vi /etc/my.cnf.d/server.cnf 
   20  vi /etc/my.cnf.d/client.cnf 
   21  vi /etc/my.cnf.d/mysql-clients.cnf 
   22  systemctl restart mariadb
   23  mysql -uroot -p
   24  cd /root
   25  wget -c https://nginx.org/download/nginx-1.12.0.tar.gz
   26  history
   27  yum install wget
   28  ll
   29  python3
   30  wget -c https://nginx.org/download/nginx-1.12.0.tar.gz
   31  https://www.cnblogs.com/s-seven/p/9105973.html
   32  yum -y groupinstall "Development tools"
   33  yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   34  wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
   35  mkdir /usr/local/python3 
   36  ll
   37  tar -xvJf  Python-3.6.2.tar.xz
   38  cd Python-3.6.2
   39  ./configure --prefix=/usr/local/python3
   40  make && make install
   41  ln -s /usr/local/python3/bin/python3 /usr/bin/python3
   42  ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
   43  python3
   44  yum install -y gcc gcc-c++
   45  yum install -y openssl_devel
   46  yum install -y openssl-devel
   47  yum install -y httpd-tools
   48  cd ../
   49  ll
   50  tar -zxf nginx-1.12.0.tar.gz 
   51  ll
   52  cd nginx-1.12.0
   53  useradd nginx
   54  ll
   55  ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-http_ssl_module --with-http_mp4_module --with-http_flv_module --with-http_avi_module
   56  ./configure --prefix=/usr/local/nginx --user=nginx --group=nginx --with-http_ssl_module --with-http_mp4_module --with-http_flv_module
   57  make && make install 
   58  ln -s /usr/local/nginx/sbin/nginx /usr/sbin/
   59  nginx
   66  yum install net-tools
   67  netstat -anptu | grep nginx
   68  ifconfig
   69  history
   70  history | a.txt
   71  history | > a.txt


