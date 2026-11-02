"""공식 체크섬을 확인한 GitHub CLI와 jq를 작업 경로에 준비"""

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

if not shutil.which("jq"):
	root = Path(os.environ["RUNNER_TEMP"]) / "network-copier-jq"
	root.mkdir(parents=True, exist_ok=True)
	binary = root / "jq"
	address = "https://github.com/jqlang/jq/releases/download/jq-1.8.1/jq-linux-amd64"
	with urllib.request.urlopen(address, timeout=60) as response:
		content = response.read()

	if hashlib.sha256(content).hexdigest() != "020468de7539ce70ef1bceaf7cde2e8c4f2ca6c3afb84642aabc5c97d9fc2a0d":
		raise RuntimeError("jq checksum mismatch")

	binary.write_bytes(content)
	binary.chmod(0o755)
	with Path(os.environ["GITHUB_PATH"]).open("a", encoding="utf-8") as stream:
		stream.write(str(root) + "\n")
