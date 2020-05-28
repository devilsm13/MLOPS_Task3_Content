# MLOPS_Task3_Content

MLOPS

You might have heard the fact that 90% of the Machine Learning models never make it to the production. There are numerous obstacles in the path. One such obstacle is that the data science guys and the IT guys are not getting an opportunity to work together.

A solution to the above problem: MLOPS (A combination of ML and DevOps) that gives both the IT team as well as the Data Science team to work together in order to push the ML model into the production. With the help of this latest technology, both the teams could work together, deploy the model, monitor it, and manage the model in production. 

So, here is a task which was given by @Vimal Daga sir in which I have tried to integrate ML with DevOps. I have used some of the most demanding technologies in this project such as Git, Github, Jenkins, Docker, and Machine Learning. Finally, I have created a delivery pipeline by using the build pipeline plugin in Jenkins that automates the production of ML model without the interference of any human being. 

#TASK DESCRIPTION

1.	Create a container image that has Python3 and Keras or NumPy installed  using docker file 

2.	When we launch this image, it should automatically start to train the model in the container.

3.	Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4.	 Job1: Pull the Github repo automatically when some developers push the repo to Github.

5.	 Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the software required for the CNN processing).

6.	Job3: Train your model and predict accuracy or metrics.

7.	Job4: if metrics accuracy is less than 80%, then tweak the machine learning model architecture.

8.	Job5: Retrain the model or notify that the best model is being created

9.	Create One extra job job6 for monitoring: If the container where the app is running, fails due to any reason then this job should automatically start the container again from where the last trained model left

So, Let’s try to achieve the following requirements:

The first step is to create a DockerFile that installs all the required libraries of python and builds an image from the file.
 
Check 1st Screenshot in the screenshots folder to see the content of Docker file.


After successfully creating the Dockerfile, it is the time to create a docker image using this Dockerfile. Check 2nd screenshot to get the code. 


The creation of a docker image with all the above requirements has been started.


And hence, the image has been successfully created. 

Now let us move towards the Jobs in Jenkins.

The first job is to pull the code from GitHub.

For automatic pulling of code from GitHub, I have used Poll SCM trigger in the first job of Jenkins and then the pulled code will be copied to the root directory of the Redhat (whichever OS/environment you are using).

JOB1:




This Job will pull the code from the GitHub repository and then copy all the files from the workspace of Jenkins to the root directory of my RedHat8. 

Now, here comes the Job2 where a docker container is launched and the copied python code is run. Then, the accuracy of the model is saved in a file named accuracy.txt. 
JOB2:



The second job will only run when Job1 successfully runs. 



This is the code in Job2 that will launch the container and run the python code in order to create a model. 



I have used the concept of the loop in which changing the value of “filt” variable will change the number of filters and changing the value of “parameter” variable will increase the number of layers in the model. 

Here is the GitHub link where you can find the above Machine Learning code:

https://github.com/devilsm13/MLOps1



The accuracy has been retrieved from the model and has been stored in a text file in the RedHat8. 

Now let us move towards the third job. This is the most important part where the accuracy of the model will be compared with some value and if this accuracy is less than that expected value, then the model will change the hyperparameters (such as filters, the number of layers, etc.) itself until and unless the accuracy matches the expected one. 

In Job 3, I have used the “sed” concept of Linux using which I have done changes in the python code in which the model is being trained. 

JOB3:


This job will check whether the accuracy of the model is 95% or not. And if it is less than the job will do necessary changes (increasing the number of layers and the number of filters) in the code. The value of the parameter variable keeps on increasing and every time the loop runs, the number of layers will be doubled and the number of filters will also be increased than the previous one. 





Now, after getting the expected accuracy, Job 3 will trigger Job 4 which will send an email to the authority.

JOB4:



Hence, all the jobs have been completed. And here comes the role of the fifth Job that will keep monitoring the container in which the Machine Learning code is running. If the container is running properly, there is no problem at all!!

However, at any moment, if the container fails, Job 5 will restart the container and on the other hand, it will also send an email to the authority regarding the issue. 


JOB5:



Here, Job4 will trigger Job5 for the very first time and after that, this job will keep on monitoring the container until and unless it is stopped manually. 



For testing purpose, I manually stopped the container to check whether the second part of the code is working or not. It worked!!





And thus, we have successfully achieved our requirements by integrating GitHub, RedHat, Docker, and Jenkins. Here, we created a total of 5 Jobs and then visualized them using the BIULD PIPELINE in Jenkins. 

Hope you liked the project. Thanks a lot for your time. 

(To get the respective codes of all the above jobs and their outputs, you can either check the screenshots or the text files at: https://github.com/devilsm13/MLOPS_Task3_Content) 
