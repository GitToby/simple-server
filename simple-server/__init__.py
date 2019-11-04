import os

import uvicorn as uvicorn
from fastapi import FastAPI, Query
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

CODEBASE_ROOT = os.sep.join(os.getcwd().split(os.sep)[:-1])
UI_ASSETS_ROOT = f'{CODEBASE_ROOT}{os.sep}simple-server-ui{os.sep}build'
print(UI_ASSETS_ROOT)
app = FastAPI(
    title='Just an API'
)


@app.get("/", tags=["UI"])
async def get_ui():
    return FileResponse(f'{UI_ASSETS_ROOT}{os.sep}index.html')


@app.get("/hello")
async def hello_world(name: str = Query("world")):
    return {'hello': name}


app.mount("/", StaticFiles(directory=UI_ASSETS_ROOT))

uvicorn.run(app,
            # host="0.0.0.0", # run on external network?
            port=8001,
            debug=True)
