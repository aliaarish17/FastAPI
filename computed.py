from pydantic import BaseModel,EmailStr,computed_field

from typing import List,Dict


class Patient(BaseModel):
    name:str
    age:int
    email: EmailStr
    weight:float
    height:float
    married:bool
    allergy: List[str]
    contact: Dict[str,str]

    @computed_field
    @property

    def bmi_calc(self)-> float:
        bmi= self.weight/ (self.height**2)
        return bmi

    







def update_info(patient:Patient):


    print(patient.name)                    
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.married)
    print(patient.allergy)
    print(patient.contact)
    print('BMI', patient.bmi_calc) ##function name hi use hota 
    print('updated')




patient_info ={'name':"aarish", "age": '80',"email":'abc@sbi.com', 'weight': 90.8,'height': 1.76, 'married': True, 'allergy': ['pollen', 'chics'],  'contact': {'main': 'house 1', 'contact': '9697979', 'emergency':'9589583530'}}
patient1 =Patient(**patient_info)   #TYPE COERCISON YAHA HPTA HAI 

update_info(patient1)