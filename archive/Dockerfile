FROM public.ecr.aws/lambda/python:3.7

WORKDIR /Users/chrishart/Documents/Coding_Challenges/Serverless-Dog-App/lambda

# Copy requirements.txt
COPY requirements.txt ./

# Copy function code
COPY main.py ./

# Install the specified packages
RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "main.lambda_handler" ]