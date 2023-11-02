def initialize_app():
    from fastapi import FastAPI
    app = FastAPI()

    from core.routers import user, task
    app.include_router(user.router)
    app.include_router(task.router)

    return app

app = initialize_app()
