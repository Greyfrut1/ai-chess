# This is an example Dockerfile. Modify it to match your needs
# Use the official image as a parent image
FROM <image name>
ADD . /<container directory>
WORKDIR /<container directory>
# Install the dependencies
RUN pip install -r requirements.txt
# Run the application
CMD python app.py
