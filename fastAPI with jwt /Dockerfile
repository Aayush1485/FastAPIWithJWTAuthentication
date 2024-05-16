FROM python:3.12.0

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies
RUN pip install -r requirement.txt
RUN pip install pydantic[email]

# Command to run the FastAPI application with Uvicorn
# CMD ["uvicorn", "main:app", "--reload"]
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]

