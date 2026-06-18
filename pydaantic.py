from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional, Annotated

class Patient(BaseModel):
    name:str= Annotated[str, Field(max_length=50, description='Enter the name', title='Name?', examples=['Aarish', 'Amit'])]
    age:int=Field(gt=1 , lt = 101)
    email: EmailStr
    weight:Annotated[float, Field(gt=0)]
    married:Annotated[bool, Field(default=None, description='is the patient married')]
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
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('updated')


patient_info ={'name':"aarish", "age": 50,"email":'abc@gmail.com', 'weight': 90.8,   'contact': {'main': 'house 1', "okay": "yes"}}
patient1 =Patient(**patient_info)    

update_info(patient1)