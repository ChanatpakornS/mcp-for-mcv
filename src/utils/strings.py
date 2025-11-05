def resources_path(server_path:str, service_path: str = '', another_path: str = '') -> str:
    return server_path + '://' + service_path + another_path
