import yt_dlp

def download_video(video_url, output_path, filename):
    ydl_opts = {
        'format': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
        'outtmpl': f'{output_path}/{filename}'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f'Downloaded: {video_url}')

# Example usage
video_url = 'https://www.youtube.com/watch?v=POwhs6eTeZQ'
output_path = './videos'
filename = 'test0.mp4'

download_video(video_url, output_path, filename)
