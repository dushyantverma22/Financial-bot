from backened.services.excel_services import (
    ExcelService
)

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

import shutil

router = APIRouter()

@router.post("/upload")
async def upload_portfolio(
    file: UploadFile = File(...)
):

    upload_path = (
        f"backened//data//uploads//{file.filename}"
    )

    with open(
        upload_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    excel_service = ExcelService(
        upload_path
    )

    result = (
        excel_service
        .ingest_to_sqlite(
            "data/portfolio.db"
        )
    )

    return result