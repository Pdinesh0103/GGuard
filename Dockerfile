# 1. Use the official lightweight Python image
# We use 3.11-slim because it's small and compatible with your AI libraries
FROM python:3.11-slim

# 2. Optimize Python for Containers
# Keeps Python from buffering stdout/stderr so you see logs immediately
ENV PYTHONUNBUFFERED True

# 3. Set the working directory inside the container
ENV APP_HOME /app
WORKDIR $APP_HOME

# 4. Copy your code files into the container
# Copy everything from your current folder (.) to the container folder (./)
COPY . ./

# 5. Install dependencies
# We use --no-cache-dir to keep the image small
RUN pip install --no-cache-dir -r requirements.txt

# 6. The Command to Run Your App
# We use 'gunicorn' instead of 'flask run' for production stability.
# It binds to the specific port Google Cloud gives us ($PORT).
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
