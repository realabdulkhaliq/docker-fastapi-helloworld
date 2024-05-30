# docker-fastapi-helloworld

Docker Containerization FastAPI Hello World

1. Create Poetry Project
2. Add FastAPI & UVICORN
3. RUN the code
4. Write Test
5. Add Pytest
6. Run Pytest
7. Create Dockerfile
   [Download WSL 2](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
8. Build Docker Image

   ```
   docker build -f Dockerfile.dev -t fastapi-helloworld-image .
   ```

   _If login error occur_

   ```
   docker login
   ```

9. Run Image
