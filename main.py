from fastapi import FastAPI,Path, HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated, Literal,Optional
import json 

app = FastAPI()

class Patient(BaseModel):
    id:Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name:Annotated[str, Field(..., description='NAME of the patient')]
    age:Annotated[int, Field(...,gt=0 ,lt=120, description='Age of the patient')]
    gender:Annotated[Literal['Male', 'Female'],Field(...,description='Gender of the patient')]
    bloodGroup:Annotated[str, Field(..., description='BloodGrp of the patient')]
    phone:Annotated[str, Field(...,description='PHone of the patient')]
    address:Annotated[str, Field(...,description='address of th epatient')]
    height:Annotated[float, Field(...,description='height in m', gt=0)]
    weight:Annotated[float, Field(...,description='weight in kgs')]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight / (self.height ** 2), 2)  
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi <18.5:
            return "underweight"
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi< 30:
            return'Normal'
        else:
            return 'Obese'

#2nd pydantiic model updation k liye

class PatientUpdate(BaseModel):

    name:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int], Field(default=None,gt=0,lt=100)]
    gender:Annotated[Optional[Literal['Male', 'Female']],Field(default=None)]
    bloodGroup:Annotated[Optional[str], Field(default=None)]
    phone:Annotated[Optional[str],Field(default=None)]
    address:Annotated[Optional[str], Field(default=None)]
    height:Annotated[Optional[float], Field(default=None,gt=0)]
    weight:Annotated[Optional[float], Field(default=None,gt=0)]

def load_data():
    with open  ("patients.json", "r") as f:
        data = json.load(f)

    return data

def save_data(data):
    with open ('patients.json', 'w') as f:
        json.dump(data,f)


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


@app.post('/create')
def create_patient(patient: Patient): #DATA VALIDATION YAHI PE HOTA patient(data) from client as a request-body  aata BASEMODEL usko validate krta
    #after validation:
    # load data:
    data = load_data() 

    #check if patient exists
    if patient.id in data :
        raise HTTPException(status_code=400,
                            detail='Patient exists')
    
    #new patient in the DB:

    data[patient.id]=patient.model_dump(exclude=['id'])

    #savw the data:
    save_data(data)

    return JSONResponse(status_code=201,
                        content={'message': 'patient added succesfully'})




#UPDATE

@app.put('/edit/{patient_id}')
def update_patient(patient_id:str, patient_update:PatientUpdate):


    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient doesnt exist')
    existing_patient_info = data[patient_id] # patient id se data milgya ,, before updated data hai 

    updated_info = patient_update.model_dump(exclude_unset= True)# updatwe krne ke liye bheja hua input isko store kro and obj--> dict mei convert kro --> key,valuw pair ayega

    for key,value in updated_info.items():
        existing_patient_info[key]= value   #new values chalegya

    #bmi, verdict bhi change hogya:

    #existing_patient_info---> pydantic object --> updated bmi verdict--> pyd obj -->dict--> data[patient id ]= existing_p_info -->save

    existing_patient_info['id'] = patient_id # pyd model mei id field hai toh add krna padega

    patient_pyd_obj= Patient(**existing_patient_info)

    existing_patient_info=patient_pyd_obj.model_dump(exclude='id')

    #add this dict to data
    data[patient_id]= existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200,
                        content={'message': 'done updated'})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient doesnt exist')
    
    del data[patient_id]

    save_data(data)
    return JSONResponse(status_code=200,
                        content={'message': 'done updated'})





