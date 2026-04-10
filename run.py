import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host        = "0.0.0.0",
        port        = 8000,
        reload      = True,
        reload_dirs = ["connectors", "utils"],  # ← only watch these folders for changes
        # dags/ folder does not watch → no more restarts
    )