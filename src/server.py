from fastmcp import FastMCP
from config.contants import APP_NAME, HOST, PORT, TRANSPORT
from routes import root, infos, courses, users 

mcp = FastMCP(APP_NAME)

root.register(mcp)
infos.register(mcp)
courses.register(mcp)
users.register(mcp)

if __name__ == "__main__":
    print(f"🚀 Starting {APP_NAME} on {TRANSPORT}://{HOST}:{PORT}")
    mcp.run(transport=TRANSPORT, host=HOST, port=PORT)
