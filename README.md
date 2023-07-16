# Serverless-Dog-App

**URL Link:** http://serverless-dog.s3-website.us-east-2.amazonaws.com/

**Overview:**

The serverless-dog-app calls an AWS lambda function  that retrieves and handles data from the dog api.

Note that the plan was to store the data into the google cloud firestore database, but ultimately, I was unable to make that happen.  I have documented here the app capability, where I got stuck, and areas I would investigate to resolve the issues.  

- **App Architecture:**
  ![db schema model](serverless-app-architecture.png?raw=true 'serverless-app-architecture')
- **Google Cloud Firestore Database:**
- ![db schema model](google-cloud-firestore.png?raw=true 'serverless-app-architecture')

**How to Run and/or Install the Translation App:**

1. Simply visit https://translation-app.surge.sh/ or continue reading for local installation
2. Clone the web folder to local directory
3. Open the index.html file and the app will be able to communicate with the external lambda function.
4. I was unable to create a dockerfile that would allow other developers to easily install and run the app.



**Design Approach:**

1. Per the challenge instructions, it was given that we had to create a serverless app that used AWS Lambda and Google Cloud Firestore.
2. After studying these technologies that were new to me, I saw an opportunity to host the static app via AWS s3.
3. I new I needed a static app to host on s3.  I created a simple app that would allow a user click a button, call the external lambda function, and add the retrieved dog data to the DOM. 




**Next Steps:**

* Note: See the 'archive folder for the direction I was headed to connect the firestore database
* Add a new layer to the AWS lambda function with a docker image hosted on AWS s3
	* I tried various ways to zip my venv dependencies and integrate in a layer. Unfortunately, the zipped file was too large and could not be used. I split the dependencies to create multiple layers, but even single dependencies, like firebase-admin, was too large to host as a zip file.
	* I have seen docker image sizes are drastically small at less than 1 mb. I would try direction next.

* Restrict resource permissions.  
	* I granted open public read/write access in order to obtain a proof of concept.
	* Going forward, I would confirm the minimum permissions required by the app

* Implement delete button capability to remove stored dogs from the database


**Step-by-step User guide:**

1. Go to the home page, http://serverless-dog.s3-website.us-east-2.amazonaws.com/

2. Click the button to add a new dog



**Technologies Used:**

* AWS s3
* AWS Lambda
* Google Cloud Firestore (set up, but not used)

**Additional Notes:**
I'm fairly happy with what I was able to accomplish, given that I had zero prior experience with serverless apps, aws and google cloud products and cloud infrastructure.  My end result was also satisfying considering I was traveling during the challenge period and had half the time.

While I have no prior experience with serverless technologies and docker, I find them all fascinating and would love to master these new tools.  I have a strong aptitude to learn and would enjoy the work.

Finally I would like to add that all work has been done independently by me with zero assistance from other people.  Integrity is a top value for me and if I speak openly and honestly if there was a problem I could not solve.  