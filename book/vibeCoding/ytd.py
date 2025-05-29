from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    yt = YouTube(url)
    try:
        stream = yt.streams.get_highest_resolution()
        print(f"正在下載: {yt.title}")
        stream.download(output_path)
        print("下載完成！")
    except Exception as e:
        print(f"下載失敗: {e}")


if __name__ == "__main__":
    url = input("請輸入YouTube影片網址: ")
    download_youtube_video(url)

    #https://www.youtube.com/watch?v=wmduMu0vd8E
