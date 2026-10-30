# YOLO 9-Class Classification & Local Grid Demo

A YOLOv8 image-classification project with nine visual categories and a **local mock grid demo** (`website.html`). This repository-ready package preserves the original Python scripts, Jupyter notebook, trained weights, sample images, training reports, evaluation outputs, and HTML demo.

## Project contents

- `models/best.pt` — trained 9-class model used by the local demo script.
- `yolov8n-cls.pt` — original pretrained YOLOv8 classification checkpoint.
- `scripts/YOLO.ipynb` — dataset preparation, model training, analysis and evaluation notebook.
- `scripts/class_map.py` — class-name aliases.
- `scripts/solve_local_captcha.py` — Selenium-based automation for the **included local mock website**.
- `website.html`, `images/` — local interactive image-grid demo and sample tiles.
- `runs/`, `outputs/` — training and evaluation artifacts, including `best.pt` and `last.pt` in the original run directory.

## Classes

`Bicycle`, `Bridge`, `Bus`, `Car`, `Cross`, `Hydrant`, `Motorcycle`, `Stair`, `Tlight`.

## Setup

From the **repository root** (the directory containing `website.html`):

```bash
python -m venv .venv
# Activate the environment using the command for your OS, then:
python -m pip install -r requirements.txt
```

Open `website.html` in a browser for the standalone local demonstration. The Python demo script uses Google Chrome and expects a compatible `chromedriver.exe` at the **repository root**; that executable was **not present in the provided archive**. With it installed and the dependencies available, run:

```bash
python scripts/solve_local_captcha.py
```

This is for the included local mock demo only.

## Training / evaluation notebook

Open `scripts/YOLO.ipynb` with Jupyter **while your current working directory is the repository root** (or adjust `PROJECT_ROOT` in the notebook). The notebook uses `dataset/train` and `dataset/val` to construct `dataset_9/`, which is then used for training and evaluation. **Neither `dataset/` nor `dataset_9/` was included in the uploaded source ZIP**, so retraining and full dataset evaluation require restoring those data directories separately. You can inspect the preserved training/evaluation outputs without retraining.

Some saved training metadata (`runs/.../args.yaml`) contains absolute Windows paths from the original machine; they are historical metadata, not portable config values.

## Repository packaging

This upload-friendly package keeps original source files **byte-for-byte unchanged**, except that it excludes `resultVideo.mp4` (a generated demo output, not used by any included source code). The video is available in the companion `YOLO_Demo_Video.zip` archive. The root `YOLO3/` wrapper from the source archive was removed so the extracted files can be uploaded directly as a GitHub repository.

Files added for the repository: `.gitignore`, `README.md`, `requirements.txt`, `GITHUB_UPLOAD_GUIDE_FA.md`.

> To make source code visible on GitHub, **extract this ZIP and upload its contents** or commit them with Git. Uploading the ZIP as a single file merely stores an archive in the repository.
