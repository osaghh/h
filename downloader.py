import requests
import os
from urllib.parse import urlparse

def get_file_info(url):
    try:
        response = requests.head(url, allow_redirects=True)
        size = int(response.headers.get('content-length', 0))
        filename = os.path.basename(urlparse(response.url).path)
        if not filename:
            filename = "downloaded_file"
        return filename, size
    except Exception as e:
        print(f"⚠️ Could not fetch file info for {url}: {e}")
        return "downloaded_file", 0

def download_with_progress(url):
    filename, total_size = get_file_info(url)
    print(f"\n📄 File: {filename}")
    print(f"📦 Size: {total_size / (1024*1024):.2f} MB" if total_size else "📦 Size: Unknown")

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            downloaded = 0
            for chunk in response.iter_content(chunk_size=10240):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size:
                        percent = int((downloaded / total_size) * 100)
                        print(f"⏳ Downloading: {percent}%", end="\r")
            print(f"\n✅ Download complete: {filename}")
    except Exception as e:
        print(f"❌ Error downloading {url}: {e}")

def main():
    print("🔗 Enter one or more public URLs (comma-separated):")
    urls = input().strip().split(',')

    for url in urls:
        url = url.strip()
        if url.startswith("http"):
            download_with_progress(url)
        else:
            print(f"❌ Invalid URL skipped: {url}")

if __name__ == "__main__":
    main()
