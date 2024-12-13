# BestBuy Staff-Service

## Overview
The **Staff-Service Microservice** is a RESTful service that manages staff information. It supports CRUD (Create, Read, Update, Delete) operations for staff data stored in memory (no database required). The service adheres to the **12-factor principles** as much as possible and is implemented in Python using the FastAPI framework.

### Features:
- Manage staff information including:
  - `id`: Unique identifier for each staff member.
  - `name`: Full name of the staff member.
  - `position`: Role of the staff member.
  - `department`: Department where the staff works.
  - `email`: Contact email.
  - `phone`: Contact phone number.
- Exposes REST APIs for CRUD operations.
- Containerized with Docker.
- Deployed to Azure Kubernetes Service (AKS).
- CI/CD pipeline configured using GitHub Actions.

---

## Endpoints

### 1. Create a Staff Member
**Method**: `POST`
**Endpoint**: `/staff`
**Request Body**:
```json
{
  "name": "John Doe",
  "position": "Manager",
  "department": "Sales",
  "email": "john.doe@example.com",
  "phone": "123-456-7890"
}
```
**Response**:
```json
{
  "id": "unique-id",
  "name": "John Doe",
  "position": "Manager",
  "department": "Sales",
  "email": "john.doe@example.com",
  "phone": "123-456-7890"
}
```

### 2. Get All Staff Members
**Method**: `GET`
**Endpoint**: `/staff`
**Response**:
```json
[
  {
    "id": "unique-id",
    "name": "John Doe",
    "position": "Manager",
    "department": "Sales",
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
  }
]
```

### 3. Get a Staff Member by ID
**Method**: `GET`
**Endpoint**: `/staff/{id}`
**Response**:
```json
{
  "id": "unique-id",
  "name": "John Doe",
  "position": "Manager",
  "department": "Sales",
  "email": "john.doe@example.com",
  "phone": "123-456-7890"
}
```

### 4. Update a Staff Member
**Method**: `PUT`
**Endpoint**: `/staff/{id}`
**Request Body**:
```json
{
  "name": "Jane Doe",
  "position": "Director",
  "department": "Marketing",
  "email": "jane.doe@example.com",
  "phone": "987-654-3210"
}
```
**Response**:
```json
{
  "id": "unique-id",
  "name": "Jane Doe",
  "position": "Director",
  "department": "Marketing",
  "email": "jane.doe@example.com",
  "phone": "987-654-3210"
}
```

### 5. Delete a Staff Member
**Method**: `DELETE`
**Endpoint**: `/staff/{id}`
**Response**: `204 No Content`

---

## Tasks Completed

### 1. Develop the Staff-Service Microservice
- Implemented the service in Python using FastAPI.
- Added endpoints for CRUD operations.
- Stored staff data in memory as a simple list of objects.
- Initial commit message: `"Initial Commit"`.

### 2. Containerize the Service
- Created a `Dockerfile` for the service.
- Built the Docker image locally.
- Pushed the Docker image to Docker Hub.
- Added the `Dockerfile` to the repository with the commit message: `"Adding Dockerfile"`.

**Docker Hub Image**: [Docker Hub Link](https://hub.docker.com/r/jamesngugi/bestbuy-staff-service)

### 3. Deploy to Azure Kubernetes Service (AKS)
- Created an AKS cluster with one master and one worker node.
- Wrote a Kubernetes deployment YAML file for the service.
- Exposed the service using a Kubernetes `Service` resource.
- Added the YAML file to the repository with the commit message: `"Adding AKS deployment file"`.

### 4. Set Up CI/CD Pipeline
- Configured a GitHub Actions workflow (`ci_cd.yaml`) to:
  - Build the Docker image.
  - Run tests.
  - Push the image to Docker Hub.
  - Deploy the service to AKS.
- Added the workflow file to the repository with the commit message: `"Adding CI/CD pipeline"`.

### 5. Test the CI/CD Pipeline
- Triggered the GitHub Actions workflow.
- Verified the build, test, and deployment jobs were successful.

---

## Technical Issues Encountered
1. **Docker Networking Issue**:
   - Resolved by exposing the correct port in the `Dockerfile` and Kubernetes deployment.
2. **Dependency Errors**:
   - Fixed by specifying dependencies explicitly in `requirements.txt`.
3. **Kubernetes Service Configuration**:
   - Resolved by using a `LoadBalancer` service type for external access.

---

## How to Run the Service

### Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application:
   ```bash
   python app/main.py
   ```
3. Access the service at:
   ```
   http://127.0.0.1:8080
   ```

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t staff-service .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8080:8080 staff-service
   ```
3. Access the service at:
   ```
   http://127.0.0.1:8080
   ```

### On Kubernetes
1. Apply the Kubernetes deployment YAML file:
   ```bash
   kubectl apply -f deployment.yaml
   ```
2. Access the service using the external IP of the `LoadBalancer`:
   ```
   kubectl get services
   ```


**Docker Hub Image**: [Docker Hub Link](https://hub.docker.com/r/jamesngugi/bestbuy-staff-service)
