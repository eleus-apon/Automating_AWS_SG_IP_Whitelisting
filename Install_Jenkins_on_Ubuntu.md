# Jenkins
Jenkins is an open-source automation server that automates the repetitive technical tasks involved in the continuous integration and delivery of software.
We will use Jenkins to automate our process.

# Prerequisites
To install Jenkins on our Ubuntu server Java 8 must be installed.
```
sudo apt install openjdk-8-jdk
```

We will also install git
```
sudo apt install git
```

# Installing Jenkins
## Step 1
The version of Jenkins included with the default Ubuntu packages is often behind the latest available version from the project itself. To take advantage of the latest fixes and features, we can use the project-maintained packages to install Jenkins.

First, add the repository key to the system:
```
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
```
When the key is added, the system will return `OK`. Next, append the Debian package repository address to the server’s sources.list:
```
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
```
When both of these are in place, run update so that apt will use the new repository:
```
sudo apt-get update
```
Finally, install Jenkins and its dependencies:
```
sudo apt-get install jenkins
```
Now that Jenkins and its dependencies are in place, we’ll start the Jenkins server.
