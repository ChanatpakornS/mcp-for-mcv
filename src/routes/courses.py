from fastmcp import FastMCP
from controllers.courses import get_departments,get_courses 
from config.contants import MCV, DEPARTMENTS, COURSES
from utils.strings import resources_path

def register(mcp: FastMCP): 
    mcp.resource(resources_path(MCV,DEPARTMENTS))(get_departments)
    mcp.resource(resources_path(MCV,COURSES, "{?search}{?department}"))(get_courses)