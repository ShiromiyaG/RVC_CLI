import os
import wget

url_base = "https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main"
models_download = [
    (
        "pretrained/",
        [
            "D32k.pth",
            "D40k.pth",
            "D48k.pth",
            "G32k.pth",
            "G40k.pth",
            "G48k.pth",
            "f0D32k.pth",
            "f0D40k.pth",
            "f0D48k.pth",
            "f0G32k.pth",
            "f0G40k.pth",
            "f0G48k.pth",
        ],
    ),
    (
        "pretrained_v2/",
        [
            "D32k.pth",
            "D40k.pth",
            "D48k.pth",
            "G32k.pth",
            "G40k.pth",
            "G48k.pth",
            "f0D32k.pth",
            "f0D40k.pth",
            "f0D48k.pth",
            "f0G32k.pth",
            "f0G40k.pth",
            "f0G48k.pth",
        ],
    ),
]

individual_files = [
    "hubert_base.pt",
    "rmvpe.pt",
    "ffmpeg.exe",
    "ffprobe.exe",
    # "rmvpe.onnx",
]

folder_mapping = {
    "pretrained/": "rvc/pretraineds/pretrained_v1/",
    "pretrained_v2/": "rvc/pretraineds/pretrained_v2/",
}

for file_name in individual_files:
    destination_path = os.path.join(file_name)
    url = f"{url_base}/{file_name}"
    if not os.path.exists(destination_path):
        os.makedirs(os.path.dirname(destination_path) or ".", exist_ok=True)
        print(f"\nDownloading {url} to {destination_path}...")
        wget.download(url, out=destination_path)

for remote_folder, file_list in models_download:
    local_folder = folder_mapping.get(remote_folder, "")
    for file in file_list:
        destination_path = os.path.join(local_folder, file)
        url = f"{url_base}/{remote_folder}{file}"
        if not os.path.exists(destination_path):
            os.makedirs(os.path.dirname(destination_path) or ".", exist_ok=True)
            print(f"\nDownloading {url} to {destination_path}...")
            wget.download(url, out=destination_path)


print("All the files needed to use this program are downloaded.")
