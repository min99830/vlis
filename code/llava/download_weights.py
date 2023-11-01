import os
from huggingface_hub import snapshot_download

LOCAL_DIR = '../../data/models/llava/llama-13b'

os.makedirs(LOCAL_DIR, exist_ok=True)

print("Downloading llama-13b..")
snapshot_download(repo_id='huggyllama/llama-13b', local_dir_use_symlinks=False, local_dir=LOCAL_DIR)

print("Downloading llava-13b-delta-v0..")
snapshot_download(repo_id='liuhaotian/LLaVA-13b-delta-v0')

print("Done!")