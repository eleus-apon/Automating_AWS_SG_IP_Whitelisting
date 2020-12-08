# Jenkins
Jenkins is an open-source automation server that automates the repetitive technical tasks involved in the continuous integration and delivery of software.
We will use Jenkins to automate our process.

# Prerequisites
To install Jenkins on our Ubuntu server Java 8 must be installed.
```
sudo apt install openjdk-8-jdk
```
![_Capture](https://user-images.githubusercontent.com/35254833/101490751-00b58480-398d-11eb-81fc-96d58258c573.PNG)

We will also install git
```
sudo apt install git
```
![_Capture1](https://user-images.githubusercontent.com/35254833/101490863-2773bb00-398d-11eb-91e9-74630772677b.PNG)

# Installing Jenkins
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
![_Capture2](https://user-images.githubusercontent.com/35254833/101490974-538f3c00-398d-11eb-9d68-076e594abc5f.PNG)

Finally, install Jenkins and its dependencies:
```
sudo apt-get install jenkins
```
Now that Jenkins and its dependencies are in place, we’ll start the Jenkins server.


Let’s start Jenkins using systemctl:
```
sudo systemctl start jenkins
```
Since systemctl doesn’t display output, you can use its status command to verify that Jenkins started successfully:
```
sudo systemctl status jenkins
```
If everything went well, the beginning of the output should show that the service is active and configured to start at boot:

Output:
![_Capture3](https://user-images.githubusercontent.com/35254833/101491849-72420280-398e-11eb-892d-2515ffdc42c7.PNG)


Now that Jenkins is running, let’s adjust our firewall rules so that we can reach it from a web browser to complete the initial setup.

By default, Jenkins runs on port 8080, so let’s open that port using ufw:
```
sudo ufw allow 8080
```
Check ufw’s status to confirm the new rules:
```
sudo ufw status
```
![_Capture4](https://user-images.githubusercontent.com/35254833/101492315-f8f6df80-398e-11eb-89a6-ca125fdb7d98.PNG)

Oh! The output is showing our Firewall is inactive. Let's active the Firewall first.
the following commands will allow OpenSSH and enable the firewall:
```
sudo ufw allow OpenSSH
sudo ufw enable
```
![_Capture5](https://user-images.githubusercontent.com/35254833/101492887-7cb0cc00-398f-11eb-9c45-b3002f89c702.PNG)

Now the port is open.
![_Capture6](https://user-images.githubusercontent.com/35254833/101493178-e5984400-398f-11eb-9ef9-2c2a7abc2e8b.PNG)

Now is our final step. To set up our installation, we need to visit Jenkins on its default port, 8080, using our server domain name or IP address: http://server_ip_or_domain:8080

You will see the Unlock Jenkins screen, which displays the location of the initial password:
![_Capture7](https://user-images.githubusercontent.com/35254833/101493585-77a04c80-3990-11eb-8674-2b63c11fa403.PNG)

In the terminal window, we need to use the cat command to display the password:
```
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```
Now we need to copy the 32-character alphanumeric password from the terminal and paste it into the Administrator password field, then click Continue.
