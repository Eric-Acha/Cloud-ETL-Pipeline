From python:3.11-slim

#Set the working directory in the container
WORKDIR /app

#Copy the requirements file into the container
COPY requirements.txt .

#Install the dependencies 
RUN pip install --no-cache-dir -r requirements.txt 

#Copy project files into the container
COPY . .

#Create logs directory inside the container
RUN mkdir -p logs

#Default command to run the application
CMD ["python", "main.py"] 