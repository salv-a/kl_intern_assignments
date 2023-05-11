from fastapi import FastAPI
from fastapi import Query
import math

app = FastAPI()


@app.get("/circle")
async def shape_circle(circle_radius: int = Query(..., description="Enter the radius")):
    return {"area": math.pi * pow(circle_radius, 2), "perimeter": 2 * math.pi * circle_radius}


@app.get("/triangle")
async def shape_triangle(side_1: int = Query(..., description="Enter first side"),
                         side_2: int = Query(..., description="Enter second side"),
                         side_3: int = Query(..., description="Enter third side")):
    semi_perimeter = (side_1 + side_2 + side_3) / 2
    return {"area": math.sqrt(
        semi_perimeter * (semi_perimeter - side_1) * (semi_perimeter - side_2) * (semi_perimeter - side_3)),
        "perimeter": side_1 + side_2 + side_3}


@app.get("/square")
async def shape_square(side: int = Query(..., description="Enter the side")):
    return {"area": side * side, "perimeter": 4 * side}


@app.get("/rectangle")
async def shape_rectangle(side_1: int = Query(..., description="Enter first side"),
                          side_2: int = Query(..., description="Enter second side")):
    return {"area": side_1 * side_2, "perimeter": 2 * (side_1 + side_2)}
