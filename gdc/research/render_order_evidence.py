"""Download the public benchmark source and render page 12 for read-only review."""
import argparse
import hashlib
import subprocess
from pathlib import Path
from urllib.request import urlopen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdftoppm", required=True)
    args = parser.parse_args()
    url = ("https://raw.githubusercontent.com/tomcardoso/watchdog/"
           "8cb766fa003f4bacd10f4a101f4b0f013596b35d/benchmarks/corpora/extract/"
           "CV-21-00656040-00CL%20Laurentian%20U%20Initial%20Order%201%20FEB%202021.pdf")
    folder = Path(__file__).parent / "source_review"
    folder.mkdir(exist_ok=True)
    pdf = folder / "laurentian_initial_order_2021_02_01.pdf"
    with urlopen(url, timeout=30) as response:
        raw = response.read()
    if not raw.startswith(b"%PDF"):
        raise ValueError("Unexpected non-PDF response")
    pdf.write_bytes(raw)
    print("source_sha256", hashlib.sha256(raw).hexdigest())
    subprocess.run([args.pdftoppm, "-f", "12", "-l", "12", "-singlefile", "-r", "110",
                    "-png", str(pdf), str(folder / "priority_page_12")], check=True)
    print(folder / "priority_page_12.png")


if __name__ == "__main__":
    main()
