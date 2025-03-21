# Cloud Logging is automatically enabled for Cloud Run and GKE when using GCP runtime.
# For local use, install and use the google-cloud-logging Python client:

# pip install google-cloud-logging

import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging

client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)

# Optionally integrate with standard logging
import logging
setup_logging(handler)

logging.info("🚀 Cloud Logging initialized.")
