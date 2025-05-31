import subprocess
import sys
import gc


class VideoService:
    
    def __init__(self, config=None):
        self.config = config or {}
        self.ydl_opts = {
            'quiet': self.config.get('YT_DLP_QUIET', True),
            'no_warnings': self.config.get('YT_DLP_NO_WARNINGS', True),
            'extract_flat': False,
            'cachedir': False,
            'writeinfojson': False,
            'writeautomaticsub': False,
            'writesubtitles': False,
        }   
        
    def get_video_info(self, url):
        import yt_dlp
        
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                result = {
                    'title': info.get('title', 'video'),
                    'ext': info.get('ext', 'mp4'),
                    'filesize': info.get('filesize'),
                }
                
                del info
                gc.collect()

                return result
        except Exception:
            gc.collect()
            return None

    def stream_video_download(self, url):
        cmd = [
            sys.executable, '-m', 'yt_dlp',
            '--quiet',
            '--no-warnings',
            '--no-cache-dir',
            '--buffer-size', '8192',
            '-o', '-',  # Output to stdout
            url
        ]
        
        try:
            chunk_size = self.config.get('YT_DLP_CHUNK_SIZE', 8192)
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=chunk_size
            )
            
            while True:
                chunk = process.stdout.read(chunk_size)
                if not chunk:
                    break
                yield chunk
            
            process.wait()
            
            if process.stdout:
                process.stdout.close()
            if process.stderr:
                process.stderr.close()
            
            if process.returncode != 0:
                stderr_output = process.stderr.read().decode('utf-8', errors='ignore')
                if stderr_output:
                    yield f'Error: {stderr_output}'.encode()
                    
        except Exception as e:
            yield f'Error downloading video: {str(e)}'.encode()
        finally:
            gc.collect()
