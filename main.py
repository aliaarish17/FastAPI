from fastapi import FastAPI,Path, HTTPException,Query
import json 

app = FastAPI()

def load_data():
    with open  ("patients.json", "r") as f:
        data = json.load(f)

    return data


@app.get("/")
def hello():
    return{'message': 'Patient management system API'}

@app.get("/about")
def aboutme():
    return{"message": "A fully functional API  to manage patients"}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ADD PATIENT ID", example="P001")):
    data = load_data()#load all data

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found!')

@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description="Sort on the basis of height,age"), order: str= Query('asc', description="desc for DESCENDING , asc for ASCENDING")):
    valid_fields=['age','height']

    if sort_by not in valid_fields:
        raise HTTPException(status_code= 400,
                        detail=f'Invalid Request, SELECT from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException (status_code= 400, detail= 'SELECT DESC OR ASC')
    
    data =load_data()
    sort_order= True if order =='desc' else False

    sorted_data= sorted(data.values(),
                        key=lambda x:x.get(sort_by),
                        reverse= sort_order)
    
    return sorted_data