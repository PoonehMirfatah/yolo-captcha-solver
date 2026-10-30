import io
import time
from pathlib import Path

from PIL import Image
from ultralytics import YOLO

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from class_map import map_class_name

PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "models" / "best.pt"
HTML_PATH = PROJECT_ROOT / "website.html"
CHROME_DRIVER_PATH = PROJECT_ROOT / "chromedriver.exe"

TOTAL_ROUNDS = 5
IMG_SIZE = 224
CONF_THRESHOLD = 0.2


def normalize_name(name):
    return name.strip().lower().replace(" ", "_").replace("-", "_")

def same_label(a, b):
    return normalize_name(a) == normalize_name(b)


def predict_tile(model, tile, target_name):
    png_bytes = tile.screenshot_as_png
    image = Image.open(io.BytesIO(png_bytes)).convert("RGB")

    w, h = image.size
    image = image.crop((
        int(w * 0.06),
        int(h * 0.12),
        int(w * 0.98),
        int(h * 0.98)
    )).resize((w, h))

    result = model.predict(
        source=image,
        imgsz=IMG_SIZE,
        verbose=False
    )[0]

    top1_idx = int(result.probs.top1)
    top1_conf = float(result.probs.top1conf)
    top1_name = result.names[top1_idx]

    name_to_idx = {
    normalize_name(map_class_name(name)): idx
    for idx, name in result.names.items()
    }
    target_key = normalize_name(map_class_name(target_name))

    if target_key in name_to_idx:
        target_idx = name_to_idx[target_key]
        target_score = float(result.probs.data[target_idx])
    else:
        target_score = 0.0

    return top1_name, top1_conf, target_score


def solve_round(driver, model, round_num):
    wait = WebDriverWait(driver, 10)

    target_el = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#targetName"))
    )
    target_name = target_el.text.strip()

    print(f"\n========== Round {round_num} ==========")
    print(f"Target: {target_name}")

    tiles = wait.until(
        lambda d: d.find_elements(By.CSS_SELECTOR, ".tile")
    )

    print(f"Tiles found: {len(tiles)}")

    selected = 0

    for i, tile in enumerate(tiles):
        pred_raw, conf, target_score = predict_tile(model, tile, target_name)
        pred_mapped = map_class_name(pred_raw)

        print(
        f"Tile {i + 1}: top1={pred_raw}, "
        f"mapped={pred_mapped}, top1_conf={conf:.4f}, "
        f"target_score={target_score:.6f}"
        )
        
        if target_score >= CONF_THRESHOLD:
            tile.click()
            selected += 1
            time.sleep(0.15)

    print(f"Selected tiles: {selected}")

    check_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkBtn"))
    )
    check_btn.click()

    time.sleep(0.8)

    status = driver.find_element(By.CSS_SELECTOR, "#status").text.strip()
    print("Status:", status)


def main():
    model = YOLO(str(MODEL_PATH))

    service = Service(str(CHROME_DRIVER_PATH))
    driver = webdriver.Chrome(service=service)

    html_url = HTML_PATH.resolve().as_uri()
    print("Opening:", html_url)

    driver.get(html_url)

    try:
        for round_num in range(1, TOTAL_ROUNDS + 1):
            solve_round(driver, model, round_num)

            if round_num < TOTAL_ROUNDS:
                reset_btn = driver.find_element(By.CSS_SELECTOR, "#resetBtn")
                reset_btn.click()
                time.sleep(1)

        print("\n========== FINAL ==========")

        try:
            wins = driver.find_element(By.CSS_SELECTOR, "#wins").text
            losses = driver.find_element(By.CSS_SELECTOR, "#losses").text
            print("Wins:", wins)
            print("Losses:", losses)
        except Exception:
            print("Could not read wins/losses.")

        input("\nPress Enter to close browser...")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()