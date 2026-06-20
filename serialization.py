from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state:str
    pin:str



class Patient(BaseModel):

    name:str
    gender:str
    age:int
    address:Address


address_dict= {'city':'jsr','state': 'jhar', 'pin':'82110'}
address1= Address(**address_dict)


patient_dict = {'name': 'Aarish',
                'gender': 'male',
                'age': 32,
                'address': address1}
patient1 =Patient(**patient_dict)   #TYPE COERCISON YAHA HPTA HAI 

temp = patient1.model_dump()
print(temp)

json_temp = patient1.model_dump_json()
print(json_temp)