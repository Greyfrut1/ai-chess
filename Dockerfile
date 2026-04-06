# This is an example Dockerfile. Modify it to match your needs
# Use the official image as a parent image
FROM python:3.14
ADD . /code
WORKDIR /code
# Install the dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
# Run the application
CMD ["fastapi", "run", "ai-chess/src/main.py", "--port", "8000"]
