import os   
import pathlib                                                                                                                                                                                                       
import dotenv

dotenv.load_dotenv(pathlib.Path(".env"))
auth_key=os.getenv("DEEPLAUTH")