import os
import uuid
dirname = os.path.dirname(__file__)

STATIC_PATH = os.path.join(dirname, 'static')
TEMPLATE_PATH = os.path.join(dirname, 'templates')
COOKIE_SECRET = str(uuid.uuid4())
UPLOAD_LOCATION = "uploads/"
DOWNLOAD_LOCATION = "/static/downloads/"
host = "localhost"
user = "root"
passwd = "narayan"
db = "test"#"muoPy"

#Logger info
loggerPath = "loggers/"
mainLogger = "mainLogger.log"