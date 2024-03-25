from fastapi import FastAPI, File, UploadFile

app=FastAPI(title="API")

building_coord=[]
camera_coord=[]

@app.post("/load")
def loadinfo(building:str="0000.000,00000.000", camera:str="0000.000,00000.000", file: UploadFile=File(...)):
    try:
        contents=file.file.read()
        with open(file.filename,'wb') as f:
            f.write(contents)
    except Exception:
        return {"status":"error"}
    finally:
        file.file.close()
    building_coord.append(float(i) for i in building.split(","))
    camera_coord.append(float(i) for i in camera.split(","))
    return {"status":"success", "info":{"building": building_coord, "camera":camera_coord, "file":file.filename}}