from pydantic import BaseModel,EmailStr,model_validator

from typing import List,Dict


class Patient(BaseModel):
    name:str
    age:int
    email: EmailStr
    weight:float
    married:bool
    allergy: List[str]
    contact: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact:
            raise ValueError('Patients older than 60 should have emergency contact')
        return model




    







def update_info(patient:Patient):


    print(patient.name)                    
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('updated')




patient_info ={'name':"aarish", "age": '80',"email":'abc@sbi.com', 'weight': 90.8, 'married': True, 'allergy': ['pollen', 'chics'],  'contact': {'main': 'house 1', 'contact': '9697979', 'emergency':'9589583530'}}
patient1 =Patient(**patient_info)   #TYPE COERCISON YAHA HPTA HAI 

update_info(patient1)