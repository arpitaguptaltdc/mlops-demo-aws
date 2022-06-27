#Directory structure of the flask application

Flask_application
├── app.py
├── Feature selection.ipynb
├── Dockerfile
├── Credit Risk Analysi ML bootcamp.csv
├── preprocess.py
|-- Procfile 
|-- runtime.txt
├── __pycache__
│   └── preprocess.cpython-39.pyc
├── Readme.md
├── requirements.txt
├── rf_model.pkl
├── static
│   └── styles
│       └── style.css
└── templates
    └── index.html

app.py --> contain all the code of the flask application
credit_risk.ipynb --> contain the eda and model training code 
Credit Risk Analysi ML bootcamp.csv.csv --> dataset 
preprocess.py --> contain helper function 
requirements.txt --> all the necessary packages used to build the application
final_data.csv --> final trainable dataset
rf_model --> trained random forest model file 
static/styles/styles.css --> contain code for styling html document
templates --> contain the index.html file
Procfile --> Contain information that are executed during by app on startup
runtime --> specified the runtime (python 3.9.1)

-----------------------------------------------------------------------
To run the application type the following command 

On Linux :

	Step1: Create a virtual environment 
		python3 -m venv dir_name 
	
	Step2: Activate the virtual environment
		source bin/activate
	
	Step3: Install the required dependencies and packages from the requirments.txt
		pip3 install -r requirments.txt
	
	Step4: Run the application
		python3 app.py


On Windows :
		Step1 : Create a virtual environment 
			python -m venv dir_name	
   	
		Step2 : Activate the virtual environment
			Scripts\activate
		
		Step3 : Install the required packages needed to run the application
			pip install -r requirements.txt

		Step4 : Run the application 
			python app.py
		
		Step5 : To deactivate the virtual environment type the command
			deactivate






To make the application a docker container:
	First make sure docker is installed on your system

	Step1 : Build the images from the dockerfile 
	
		docker build --tag images_name:tag .

	Step3 : See all the images we built 
		
		docker images
	
	Step3 : Create a docker container from the docker image just created (our application is configured to be run on port 8000, by default flask app runs on port 5000 ) 
		
		docker run --name container_name -p 8000:8000 application_name:tag
	
	Step4 : You can see the conatiner running 
		
		docker ps -a
	
	Step5 : To stop a running container 
		
		docker stop conatiner_id 
		
	Step6 : To start a stopped a container 
		
		docker start container_id
	
	
		
