"""공식 체크섬을 확인한 GitHub CLI를 현재 작업 경로에 준비"""

import hashlib
import os
from pathlib import Path
import shutil
import tarfile
import urllib.request


if not shutil.which("gh"):
	version = "2.102.1"
	name = f"gh_{version}_linux_amd64.tar.gz"
	base = f"https://github.com/cli/cli/releases/download/v{version}"
	root = Path(os.environ["RUNNER_TEMP"]) / "network-copier-gh"
	root.mkdir(parents=True, exist_ok=True)
	with urllib.request.urlopen(f"{base}/gh_{version}_checksums.txt", timeout=60) as response:
		checksums = dict(line.split()[::-1] for line in response.read().decode().splitlines())

	archive = root / name
	urllib.request.urlretrieve(f"{base}/{name}", archive)
	if hashlib.sha256(archive.read_bytes()).hexdigest() != checksums[name]:
		raise RuntimeError("GitHub CLI checksum mismatch")

	with tarfile.open(archive) as bundle:
		bundle.extractall(root, filter="data")

	with Path(os.environ["GITHUB_PATH"]).open("a", encoding="utf-8") as stream:
		stream.write(str(root / f"gh_{version}_linux_amd64/bin") + "\n")
