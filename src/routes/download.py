from flask import Blueprint, request, Response, jsonify, current_app
from urllib.parse import unquote

from ..services import VideoService
from ..utils import slugify, safe_filename, get_content_type

download_bp = Blueprint('download', __name__)


@download_bp.route('/download')
def download_video():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400
    
    url = unquote(url)
    
    video_service = VideoService(current_app.config)
    
    video_info = video_service.get_video_info(url)
    if not video_info:
        return jsonify({'error': 'Unable to extract video information'}), 400
    
    slugified_title = slugify(video_info['title'])
    filename = f"{slugified_title}.{video_info['ext']}"
    
    content_type = get_content_type(video_info['ext'])
    
    response = Response(
        video_service.stream_video_download(url),
        mimetype=content_type,
        headers={
            'Content-Disposition': safe_filename(filename),
            'Content-Type': content_type,
            'Transfer-Encoding': 'chunked',
        }
    )
    
    return response
