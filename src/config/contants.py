import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "mcv-mcp-server")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8001))
TRANSPORT = os.getenv("TRANSPORT", "http")

MCV = "mycourseville"
INFOS = "infos"
DEPARTMENTS = "departments"
COURSES = "courses"
USERS = "users"