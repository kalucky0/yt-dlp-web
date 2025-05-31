# yt-dlp Web Downloader

A modern web interface for downloading videos using yt-dlp, built with Flask.

## Features

- 🎥 Download videos from YouTube and other platforms
- ⚡ Real-time streaming downloads
- 🌍 Support for multiple video platforms
- 📱 Mobile-friendly responsive design
- ℹ️ Video information preview
- 🚀 Fast and lightweight

## Project Structure

```
yt-dlp-web/
├── main.py                 # Application entry point
├── src/
│   ├── __init__.py
│   ├── app.py             # Flask app factory
│   ├── config.py          # Configuration settings
│   ├── routes/            # Route handlers
│   │   ├── __init__.py
│   │   ├── main.py        # Main routes (index)
│   │   ├── download.py    # Download functionality
│   │   └── api.py         # API endpoints
│   ├── services/          # Business logic
│   │   ├── __init__.py
│   │   └── video_service.py
│   ├── utils/             # Utility functions
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── templates/         # HTML templates
│       └── index.html
├── pyproject.toml         # Project dependencies
└── README.md             # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd yt-dlp-web
```

2. Install dependencies using uv (recommended) or pip:
```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

## Usage

### Development

Run the application in development mode:

```bash
python main.py
```

The application will be available at `http://localhost:8080`.

### Production

Set environment variables and run:

```bash
export FLASK_ENV=production
export HOST=0.0.0.0
export PORT=8080
export DEBUG=false
python main.py
```

### Environment Variables

- `FLASK_ENV`: Environment mode (`development` or `production`)
- `HOST`: Host to bind to (default: `0.0.0.0`)
- `PORT`: Port to listen on (default: `8080`)
- `DEBUG`: Enable debug mode (default: `true` in development)

## API Endpoints

### GET /
Main page with video download interface.

### GET /download?url=<video_url>
Download a video. Returns a streaming response with the video file.

### GET /info?url=<video_url>
Get video information without downloading.

Returns JSON:
```json
{
  "title": "Video Title",
  "slugified_title": "video-title",
  "extension": "mp4",
  "filename": "video-title.mp4",
  "filesize": 12345678
}
```

## Architecture

This application follows Flask best practices with:

- **App Factory Pattern**: Configurable app creation
- **Blueprint Organization**: Routes organized by functionality
- **Service Layer**: Business logic separated from routes
- **Configuration Management**: Environment-based configuration
- **Template System**: Proper Jinja2 template usage

## Dependencies

- **Flask**: Web framework
- **yt-dlp**: Video downloading library

## License

This project is open source and available under the [MIT License](LICENSE).