# 1. Use an official Python runtime as a parent image
FROM python:3.10-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Install only essential system tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy the requirements file and install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project into the container
COPY . .

# 6. Expose the port Streamlit runs on
EXPOSE 8501

# 7. Create a shell script to run Backend THEN Frontend
RUN echo "#!/bin/sh\npython Backend/src/engine.py && streamlit run Frontend/app/main.py --server.address=0.0.0.0" > run.sh
RUN chmod +x run.sh

# 8. Run the script
CMD ["./run.sh"]