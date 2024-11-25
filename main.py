import uvicorn
from fastapi import FastAPI
from fastapi import FastAPI, Depends
from routers import secure, public
from auth import get_user
from routers.public import router as public_router
from routers.secure import router as secure_router

app = FastAPI(
    title="API Documentation",
    description="Comprehensive documentation for the API endpoints.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Public Endpoints",
            "description": "Endpoints accessible without authentication."
        },
        {
            "name": "Secure Endpoints",
            "description": "Endpoints that require API key authentication."
        }
    ],
)

# Include routers
app.include_router(public_router, prefix="/public", tags=["Public Endpoints"])
app.include_router(secure_router, prefix="/secure", tags=["Secure Endpoints"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# app.include_router(
#     public.router,
#     prefix="/api/v1/public"
# )
# app.include_router(
#     secure.router,
#     prefix="/api/v1/secure",
#     dependencies=[Depends(get_user)]
# )


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI! (TST 18222043 - Ricky Wijaya)"}

