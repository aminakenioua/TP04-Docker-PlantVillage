# TP04 – Docker-Based PlantVillage Data Analysis

## 1. Project Overview

This project demonstrates how to use **Docker** to create a portable and isolated environment for analyzing the PlantVillage dataset using Python and Pandas.

The application reads a CSV dataset, displays basic information about the data, and verifies that the dataset is accessible inside the Docker container.

## 2. Objectives

- Understand the basic concepts of Docker.
- Build a Docker image using a Dockerfile.
- Run a Python application inside a Docker container.
- Use Docker volumes to access external datasets.
- Use Docker Compose to manage the application.
- Publish the Docker image to Docker Hub.
- Store and share the project files using GitHub.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| Pandas | Data reading and inspection |
| Docker | Containerization |
| Docker Compose | Container management |
| Docker Hub | Docker image repository |
| GitHub | Source code and report hosting |
| PlantVillage | Dataset source |

## 4. Project Structure

```text
TP04_Docker/
│
├── Dockerfile
├── app.py
├── compose.yaml
├── create_dataset.py
├── .gitignore
│
├── data/
│   └── PlantVillage_PowerBI.csv
│
└── report/
    └── docker.pdf
```

**Note:** The original `Tomato` image folder is excluded from GitHub because of its large size (approximately 8 GB).

## 5. Dataset Description

The project uses the `PlantVillage_PowerBI.csv` dataset.

- Number of records: 246,993
- Number of columns: 5
- File format: CSV

The dataset contains the following columns:

| Column | Description |
|---|---|
| Image_Name | Image filename |
| Plant_Class | Plant class |
| Plant_Name | Plant name |
| Disease | Disease category |
| Image_Path | Image file path |

## 6. Application Description

The Python application (`app.py`) performs basic data inspection:

1. Checks whether the dataset exists.
2. Reads the CSV file using Pandas.
3. Displays the dataset filename.
4. Displays the number of rows and columns.
5. Prints the column names.
6. Displays the first five records.

## 7. How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/aminakenioua/TP04-Docker-PlantVillage.git
```

### Step 2: Enter the Project Directory

```bash
cd TP04-Docker-PlantVillage
```

### Step 3: Build the Docker Image

```bash
docker build -t tp04-analysis .
```

### Step 4: Run the Container

```bash
docker run --rm \
-v "$(pwd)/data:/app/data:ro" \
tp04-analysis
```

The volume mount provides read-only access to the dataset inside the container.

### Alternative: Using Docker Compose

```bash
docker compose up --build
```

To stop and remove the Compose container:

```bash
docker compose down
```

## 8. Docker Hub

The Docker image is also available on Docker Hub:

**Image:** `amina2003/tp04-analysis:1.0`

Pull the image using:

```bash
docker pull amina2003/tp04-analysis:1.0
```

Run it using:

```bash
docker run --rm \
-v "$(pwd)/data:/app/data:ro" \
amina2003/tp04-analysis:1.0
```

## 9. Results

The application successfully reads the dataset and displays:

- 246,993 records.
- 5 columns.
- Column names.
- The first five rows.

The Docker container completed execution successfully.

## 10. Limitations

- The current application performs basic data inspection rather than advanced statistical analysis.
- No machine learning model is trained in this project.
- Running multiple containers does not automatically implement distributed data processing.
- The original image dataset is not included in the GitHub repository.

## 11. Conclusion

This practical work provided hands-on experience with Docker and containerized Python applications. It demonstrated how to build images, run containers, mount external datasets, use Docker Compose, and publish a Docker image on Docker Hub.

The project also provides a foundation for future extensions, such as statistical analysis, distributed processing, and machine learning.

## 12. Author

**Project:** TP04 – Docker

**GitHub:** [aminakenioua](https://github.com/aminakenioua)

**Repository:** [TP04-Docker-PlantVillage](https://github.com/aminakenioua/TP04-Docker-PlantVillage)