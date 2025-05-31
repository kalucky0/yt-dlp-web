import subprocess
import sys
import yt_dlp


class VideoService:
    
    def __init__(self, config=None):
        self.config = config or {}
        self.ydl_opts = {
            'quiet': self.config.get('YT_DLP_QUIET', True),
            'no_warnings': self.config.get('YT_DLP_NO_WARNINGS', True),
        }
    
    def get_video_info(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                return {
                    'title': info.get('title', 'video'),
                    'ext': info.get('ext', 'mp4'),
                    'filesize': info.get('filesize'),
                }
            except Exception as e:
                return None
    
    def stream_video_download(self, url):
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            '--quiet',
            '--no-warnings',
            '-o', '-',  # Output to stdout
            url
        ]
        
        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=0  # Unbuffered for real-time streaming
            )
            
            chunk_size = self.config.get('YT_DLP_CHUNK_SIZE', 8192)
            while True:
                chunk = process.stdout.read(chunk_size)
                if not chunk:
                    break
                yield chunk
            
            process.wait()
            
            if process.returncode != 0:
                stderr_output = process.stderr.read().decode('utf-8', errors='ignore')
                if stderr_output:
                    yield f'Error: {stderr_output}'.encode()
                    
        except Exception as e:
            yield f'Error downloading video: {str(e)}'.encode()
