<div align="center">

# 🎥 Video Insight AI

**An intelligent AI-powered system that analyzes video content to extract meaningful insights using Computer Vision and Deep Learning.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Databricks](https://img.shields.io/badge/Databricks-Pipeline-FF3621?style=for-the-badge&logo=databricks&logoColor=white)](https://databricks.com)
[![Delta Lake](https://img.shields.io/badge/Delta_Lake-Storage-003366?style=for-the-badge&logo=apachespark&logoColor=white)](https://delta.io)
[![OpenCV](https://img.shields.io/badge/OpenCV-CV2-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Configuration](#️-configuration)
- [🔌 API Reference](#-api-reference)
- [🔥 Databricks Pipeline](#-databricks-pipeline)
- [🗃️ Delta Lake Tables](#️-delta-lake-tables)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎯 **Object Detection** | Identify and track objects across video frames in real-time |
| 🧠 **AI Analysis** | Extract semantic insights using deep learning models |
| ⚡ **Real-time Processing** | Fast, efficient pipeline via FastAPI and Databricks clusters |
| 📊 **Insight Generation** | Auto-generate summaries, highlights, and key moments |
| 🗃️ **Delta Lake Storage** | ACID-compliant, versioned data storage for all processed results |
| 🖥️ **Interactive UI** | Streamlit frontend for uploading and exploring video insights |

---
 ## 🛠️ Tech Stack

<table>
<tr>
<td><strong>🎨 Frontend</strong></td>
<td>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>⚙️ Backend</strong></td>
<td>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Uvicorn-000000?style=flat-square&logo=python&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>🧠 AI / ML</strong></td>
<td>
  <img src="https://img.shields.io/badge/Whisper-000000?style=flat-square"/>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>☁️ Data Platform</strong></td>
<td>
  <img src="https://img.shields.io/badge/Databricks-FF3621?style=flat-square&logo=databricks&logoColor=white"/>
  <img src="https://img.shields.io/badge/Delta%20Lake-003366?style=flat-square"/>
  <img src="https://img.shields.io/badge/PySpark-FDEE21?style=flat-square&logo=apache-spark&logoColor=black"/>
</td>
</tr>
<tr>
<td><strong>📊 Data Tools</strong></td>
<td>
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
</td>
</tr>
<tr>
<td><strong>📈 Model Tracking</strong></td>
<td>
  <img src="https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white"/>
</td>
</tr>
</table>


<img width="1440" height="1312" alt="image" src="https://github.com/user-attachments/assets/1d26da8c-9f0a-47f6-893d-7f43de1ed011" />

---

## 📁 Project Structure

```
video-insight-ai/
│
├── backend/
│   └── api.py              ✅  FastAPI application & endpoints
│
├── frontend/
│   └── app.py              ✅  Streamlit UI
│
├── data/                       Uploaded videos & processed outputs
│
├── notebooks/                  Databricks notebooks
│   └── pipeline.ipynb          Main Spark processing pipeline
│
├── models/                     Saved AI model weights
│
└── requirements.txt        ✅  Python dependencies
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/DeepNema7/video-insight-aiv.git
cd video-insight-aiv
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABRICKS_HOST=https://<workspace>.azuredatabricks.net
DATABRICKS_TOKEN=dapi...
DATABRICKS_CLUSTER_ID=0101-...
DELTA_TABLE_PATH=/mnt/delta/video_results
```

### 5. Start the FastAPI backend

```bash
uvicorn backend.api:app --reload --port 8000
```

### 6. Launch the Streamlit frontend

```bash
streamlit run frontend/app.py
```

Open **http://localhost:8501** in your browser. 🎉

---

## ⚙️ Configuration

| Variable | Description | Example |
|---|---|---|
| `DATABRICKS_HOST` | Databricks workspace URL | `https://adb-xxx.azuredatabricks.net` |
| `DATABRICKS_TOKEN` | Personal access token | `dapi1234abcd...` |
| `DATABRICKS_CLUSTER_ID` | Target cluster ID | `0101-123456-abc123` |
| `DELTA_TABLE_PATH` | Delta Lake storage path | `/mnt/delta/video_results` |

---

## 🔌 API Reference

Base URL: `http://localhost:8000`

Interactive docs available at: `http://localhost:8000/docs` (Swagger UI)

### Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/analyze` | Upload video, trigger Databricks pipeline |
| `GET` | `/results/{job_id}` | Poll for processed results |
| `GET` | `/health` | Service health check |
| `GET` | `/docs` | Auto-generated Swagger UI |

### Example — upload and analyze a video

```python
import requests

# Upload video
with open("sample.mp4", "rb") as f:
    response = requests.post(
        "http://localhost:8000/analyze",
        files={"video": f}
    )

job = response.json()
print(job["job_id"])   # e.g. "run_20240101_abc123"
```

### Example — poll for results

```python
import requests, time

job_id = "run_20240101_abc123"

while True:
    r = requests.get(f"http://localhost:8000/results/{job_id}")
    data = r.json()

    if data["status"] == "complete":
        print(data["insights"])   # list of frame-level insight dicts
        break
    elif data["status"] == "failed":
        print("Pipeline failed:", data["error"])
        break

    time.sleep(5)
```

### Example response

```json
{
  "job_id": "run_20240101_abc123",
  "status": "complete",
  "insights": [
    {
      "frame": 0,
      "timestamp_sec": 0.0,
      "objects": [
        { "label": "person", "confidence": 0.97, "bbox": [10, 20, 200, 400] },
        { "label": "car",    "confidence": 0.88, "bbox": [300, 150, 600, 350] }
      ]
    }
  ],
  "summary": "Video contains persons and vehicles in an outdoor scene."
}
```

---

## 🔥 Databricks Pipeline

The pipeline is triggered by FastAPI via the Databricks Jobs REST API and runs the following stages:

```
1. Ingest      →  Video file written to DBFS (/mnt/videos/)
       ↓
2. Extract     →  OpenCV extracts frames at configurable FPS
       ↓
3. Distribute  →  Frames serialized and partitioned across Spark workers
       ↓
4. Inference   →  TF/PyTorch UDF runs object detection on each partition
       ↓
5. Aggregate   →  Frame results reduced to scene & video-level summaries
       ↓
6. Persist     →  Results written to Delta Lake tables (ACID)
       ↓
7. Notify      →  FastAPI polls Jobs API → reads Delta → returns to frontend
```

### Triggering via Python SDK

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

run = w.jobs.run_now(
    job_id=12345,
    notebook_params={"video_path": "/mnt/videos/sample.mp4"}
)

print(run.run_id)
```

---

## 🗃️ Delta Lake Tables

| Table | Description |
|---|---|
| `video_metadata` | Video filename, duration, FPS, upload timestamp |
| `frame_results` | Per-frame bounding boxes, labels, confidence scores |
| `insight_summaries` | Video-level aggregated insight report |
| `model_runs` | MLflow experiment IDs and model versions used |

### Time-travel query example

```python
from delta.tables import DeltaTable
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Read results as of a specific version
df = spark.read.format("delta") \
    .option("versionAsOf", 3) \
    .load("/mnt/delta/video_results/frame_results")

df.show()
```

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes
   ```bash
   git commit -m "feat: add your feature description"
   ```
4. **Push** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** on GitHub

Please make sure your code follows PEP 8 and includes docstrings for new functions.

---
 
---

<div align="center">

Made with ❤️ by [DeepNema7](https://github.com/DeepNema7)

⭐ Star this repo if you find it useful!

</div>
