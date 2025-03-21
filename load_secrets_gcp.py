from google.cloud import secretmanager
import os

def access_secret(secret_id, project_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# Usage Example
project_id = "your-gcp-project-id"

# Load secrets
openai_key = access_secret("OPENAI_API_KEY", project_id)
pinecone_key = access_secret("PINECONE_API_KEY", project_id)

# Set them as environment variables
os.environ["OPENAI_API_KEY"] = openai_key
os.environ["PINECONE_API_KEY"] = pinecone_key
os.environ["PINECONE_ENV"] = "us-west1-gcp"

print("✅ Secrets loaded into environment.")
