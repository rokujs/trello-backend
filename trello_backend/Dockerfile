FROM lambci/lambda:build-python3.8

# Install python module needed for gdal and rasterio
RUN yum update -y && yum install mysql-devel -y && yum clean all

# fancy prompt
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "' >> /root/.bashrc

# copy and install python dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt /tmp/
RUN virtualenv /root/env -p python3 \
    && source /root/env/bin/activate \
    && pip3 install --upgrade pip \
    && pip3 install -r /tmp/requirements.txt

# create directory project
RUN mkdir -p /opt/project
WORKDIR /opt/project

# copy and assign permissions docker-entrypoint
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod u+x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]