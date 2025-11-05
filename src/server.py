import os
from fastmcp import FastMCP
from tools.info import register_info_tools
from tools.profile import register_profile_tools
from tools.course import register_course_tools
from routes.root import register_routes
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

# Read configuration from environment
APP_NAME = os.getenv("APP_NAME", "mcv-mcp-server")
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8001))
TRANSPORT = os.getenv("TRANSPORT", "http")

# Initialize FastMCP
mcp = FastMCP(APP_NAME)

# Register tools and routes
register_info_tools(mcp)
register_profile_tools(mcp)
register_course_tools(mcp)
register_routes(mcp)

if __name__ == "__main__":
    print(f"🚀 Starting {APP_NAME} on {TRANSPORT}://{HOST}:{PORT}")
    mcp.run(transport=TRANSPORT, host=HOST, port=PORT)
