from flask import Blueprint, request, jsonify, current_app
from urllib.parse import unquote

from ..services import VideoService
from ..utils import slugify

api_bp = Blueprint('api', __name__)


@api_bp.route('/info')
def video_info():
    url = request.args.get('url')
    
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400
    
    url = unquote(url)
    
    video_service = VideoService(current_app.config)
    info = video_service.get_video_info(url)
    
    if not info:
        return jsonify({'error': 'Unable to extract video information'}), 400
    
    slugified_title = slugify(info['title'])
    
    return jsonify({
        'title': info['title'],
        'slugified_title': slugified_title,
        'extension': info['ext'],
        'filename': f"{slugified_title}.{info['ext']}",
        'filesize': info['filesize'],
    })
