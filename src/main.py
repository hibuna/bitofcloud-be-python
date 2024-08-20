from os import environ

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from sqlalchemy import text

# from auth.secrets import Secrets
from containers import Kernel


app = FastAPI(
    debug=bool(int(environ.get("DEBUG"))),
    title="bitofcloud-api",
    default_response_class=ORJSONResponse,
    root_path="/api/v1",
)


@app.get("/async/")
async def read_async():
    session = Kernel.database(async_=True).async_scoped_session()
    data = (await session.execute(text("SELECT 1;"))).fetchone()
    await session.remove()
    return {"test value": str(data)}


@app.get("/")
def read_root():
    session = Kernel.database(async_=False).scoped_session()
    data = session.execute(text("SELECT 1;")).fetchone()
    session.remove()
    return {"test value": str(data)}
