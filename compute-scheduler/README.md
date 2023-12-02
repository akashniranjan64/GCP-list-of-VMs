# API Developer Setup

## Prerequisites
The API development environment requires the following:

* Python.
* Mysql.
* Docker
* Linux or Unix is optional, as the startup script is written for Bash.
* IntelliJ IDEA is strongly recommended as an IDE. Its project config files and code formatter are version controlled.

## Getting Started

- To run the backend locally with the local database, run <br> 
```docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password -d mysql```

- Run ./deploy.sh to create the DB structure with versions
----
# UPDATE below

## IntelliJ Setup

Follow steps below to set up the pharmacy backend project on IntellJ:

### Importing project into IntelliJ

- Ensure you are using IntelliJ Ultimate (as IntelliJ CE does not have spring boot support)

### Setting up run / debug configurations


### In case of build errors

