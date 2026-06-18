from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool = False
    allergy: Optional[list[str]] = None
    contact: Dict[str,str]

def insert_info(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('inserted')

def update_info(patient:Patient):

    print(patient.name)                    
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('updated')


patient_info ={'name':"aarish", "age": 50, 'weight': 55.6,   'contact': {'main': 'house 1', "okay": "yes"}}
patient1 =Patient(**patient_info)    

update_info(patient1)