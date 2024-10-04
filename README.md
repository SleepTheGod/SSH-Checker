![SSH Checker Banner](https://i.imgur.com/0DGuMrJ.png) 

SSH Checker
Overview
Welcome to SSH Checker! This lightweight Python script is designed to help you verify the availability and responsiveness of SSH servers. Whether you’re a system administrator or a security professional, this tool will make managing multiple SSH servers a breeze. With SSH Checker, you can quickly check the status of your SSH services and ensure everything is running smoothly.

Features
Fast Checking The script uses threading to rapidly check the status of multiple SSH servers simultaneously, saving you time
Error Handling It catches connection errors and displays appropriate messages, so you know exactly what’s going on
Customizable Feel free to modify the script to suit your specific needs—it’s flexible and user-friendly
ASCII Art Banner Enjoy a visually appealing banner that greets you when you start the script
Getting Started
Prerequisites
Before you dive in, make sure you have the following

Python 3.x installed on your machine
The required library paramiko
Installation
Let’s get SSH Checker up and running

Clone the repository

git clone https://github.com/SleepTheGod/SSH-Checker.git

Change to the project directory

cd SSH-Checker

Install the required dependencies

pip install paramiko

Usage
Running the script is simple! Just use the following command

python ssh_checker.py <host_file.txt>

Make sure to replace <host_file.txt> with the path to your text file that contains the list of SSH servers you want to check (one server per line)

Example
Here’s a quick example to get you started

Create a file named hosts.txt with the following content

192.168.1.1 192.168.1.2 example.com

Run the SSH Checker script with

python ssh_checker.py hosts.txt

And that’s it! You’re all set to start checking your SSH servers. Enjoy using SSH Checker and feel free to modify it to better fit your needs. Happy checking!
