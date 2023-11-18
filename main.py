import uvicorn
from fastapi import FastAPI

from app.router import router
from app.services.fill_db import EcomDbFiller

app = FastAPI()
app.include_router(router)

ecom_db_filler = EcomDbFiller(
    'ecom_db',
    'forms',
    'app/mock_data/forms_data.json'
)
ecom_db_filler.fill_db()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
