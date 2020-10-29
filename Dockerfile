FROM jenkins/jenkins:alpine
	
ENV JENKINS_USER admin
ENV JENKINS_PASS admin
ENV NEW_USER user-1
ENV NEW_USER_PASSWORD user-1	

# Skip initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
	
COPY plugins.txt /usr/share/jenkins/plugins.txt
COPY config.xml /var/jenkins_home/config.xml
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/plugins.txt
USER root
RUN apk add docker
RUN apk add py-pip
RUN apk add --update --no-cache build-base python3-dev python3 libffi-dev libressl-dev bash git gettext curl \
 && curl -O https://bootstrap.pypa.io/get-pip.py \
 && python3 get-pip.py \
 && pip install --upgrade six awscli awsebcli
RUN apk add openssl-dev gcc libc-dev make
RUN pip install docker-compose
USER jenkins

