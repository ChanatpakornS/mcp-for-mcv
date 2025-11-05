from fastmcp import FastMCP
from controllers.info import get_mcv_info, get_help
from config.contants import MCV, INFOS
from utils.strings import resources_path

def register(mcp: FastMCP): 
    mcp.resource(resources_path(MCV,INFOS))(get_mcv_info)
    mcp.resource(resources_path(MCV,INFOS, "help"))(get_help)