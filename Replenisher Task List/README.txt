 BACKEND DESIGN OF THE APP:
 Java Spring MVC 
 My SQL 
 
 ---------------------------------------------------------------
 INSTRUCTIONS TO RUN APP: 
 Run Walmart.WAR file on APACHE TOMCAT.
 
 ---------------------------------------------------------------
 ASSUMPTIONS OF THE APP:
 
 1) The User would login with its username and password in the app.
 2) Tasks are displayed once user has successfully loggedin.
 3) While creating a task, user would input taskname,notes,feedback, status, assignedto, assignedby, priority, and estimated hours it would require to complete the task.
 ---------------------------------------------------------------
 Tables for the app:
 CREATE TABLE task 
                 ( 
                              `taskname`  VARCHAR(45) NOT NULL, 
                              `notes`  VARCHAR(45) NULL, 
                              `feedback` VARCHAR(45) NOT NULL, 
                              `status`  VARCHAR(45) NULL, 
                              `assignedto`     VARCHAR(45) NULL, 
                              `assignedby`   VARCHAR(45) NULL, 
                              `taskid`     INT NOT NULL, 
							  `priority`   VARCHAR(45) NULL, 
                              `createdTime`     DATETIME, 
							  `endTime`   DATETIME, 
                              `estHours`     INT NOT NULL, 
                              
                 )
 CREATE TABLE `sys.users` 
                 ( 
                              `username`  VARCHAR(45) NOT NULL, 
                              `password`  VARCHAR(45) NULL, 
                              `firstname` VARCHAR(45) NOT NULL, 
                              `lastname`  VARCHAR(45) NULL, 
                              `email`     VARCHAR(45) NULL, 
                              `role`   VARCHAR(45) NULL, 
                              `roleid`     INT NULL, 
                              PRIMARY KEY (`username`) 
                 )