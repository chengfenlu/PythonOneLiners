from pytube import YouTube

def download_youtube_audio(url, output_path='.'):
    yt = YouTube(url)
    try:
        stream = yt.streams.filter(only_audio=True).first()
        print(f"正在下載音訊: {yt.title}")
        out_file = stream.download(output_path)
        # 重新命名副檔名為 .mp3
        import os
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("音訊下載完成！")
    except Exception as e:
        print(f"下載失敗: {e}")

if __name__ == "__main__":
    url = input("請輸入YouTube影片網址: ")
    download_youtube_audio(url).from pytube import YouTube

def download_youtube_audio(url, output_path='.'):
    yt = YouTube(url)
    try:
        stream = yt.streams.filter(only_audio=True).first()
        print(f"正在下載音訊: {yt.title}")
        out_file = stream.download(output_path)
        # 重新命名副檔名為 .mp3
        import os
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("音訊下載完成！")
    except Exception as e:
        print(f"下載失敗: {e}")

if __name__ == "__main__":
    url = input("請輸入YouTube影片網址: ")
    download_youtube_audio(url)
