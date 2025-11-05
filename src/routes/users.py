from fastmcp import FastMCP
from controllers.users import get_myprofile
from config.contants import MCV, USERS
from utils.strings import resources_path

def register(mcp: FastMCP): 
    mcp.resource(resources_path(MCV, USERS, "{user_id}"))(get_myprofile)
