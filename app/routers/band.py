from fastapi import APIRouter


router=APIRouter()

@router.get("/band")
async def band():
    #return{"../Front-end/band.html"}
    return {"we are working"}