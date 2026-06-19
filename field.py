from pydantic import BaseModel,EmailStr,Field,field_validator
from typing import List,Dict,Optional, Annotated


class Patient(BaseModel):
    name:str= Annotated[str, Field(max_length=50, description='Enter the name', title='Name?', examples=['Aarish', 'Amit'])]
    age:int=Field(gt=1 , lt = 101)
    email: EmailStr
    weight:Annotated[float, Field(gt=0)]
    married:Annotated[bool, Field(default=None, description='is the patient married')]
    allergy: Optional[list[str]] = None
    contact: Dict[str,str]

    @field_validator('email')
    @classmethod

    def email_validator (cls,value):

        valid_domains = ['hdfc.com', 'sbi.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise TypeError('not applicable')
        

        return value
    

    @field_validator('name')
    @classmethod

    def transform_name(cls,value):
        return value.upper()
    
    
    @field_validator('age', mode='after')
    @classmethod


    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError('AGE DEKHJO')        
    




    







def update_info(patient:Patient):


    print(patient.name)                    
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('updated')




patient_info ={'name':"aarish", "age": '40',"email":'abc@sbi.com', 'weight': 90.8,   'contact': {'main': 'house 1', "okay": "yes"}}
patient1 =Patient(**patient_info)   #TYPE COERCISON YAHA HPTA HAI 

update_info(patient1)