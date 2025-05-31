import os

bind = f"0.0.0.0:{os.environ.get('PORT', 8080)}"
backlog = 2048

workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

max_requests = 1000
max_requests_jitter = 50
preload_app = True

loglevel = "info"
accesslog = "-"
errorlog = "-"

proc_name = "yt-dlp-web"

timeout = 120

limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
