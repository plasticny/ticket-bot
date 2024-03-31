from toml import load
from typing import TypedDict, Literal

# Basic Setting
class BasicSetting (TypedDict):
  user_data_dir: str
  url : str
  start_time : str
  ticket_level : list[str]
  ticket_num : int
# Basic Setting
  
# Payment Setting
class PPISetting (TypedDict):
  """ payment personal information setting """
  name : str
  phone : str
  email : str

class PSFSetting (TypedDict):
  """ payment sf setting """
  phone : str
  country : str
  region : str
  city : str
  sub_area : str
  addr : str

class PMSetting (TypedDict):
  """ payment mail setting """
  city : str
  postal_code : str
  addr1 : str
  addr2 : str
  addr3 : str

class PDMSetting (TypedDict):
  """ payment delivery method setting """
  delivery_method : Literal[0, 1]
  sf : PSFSetting
  mail : PMSetting

class PPMI1Setting (TypedDict):
  holder : str
  card : str
  
class PPMI2Setting (TypedDict):
  expiry_month : str
  expiry_year : str
  code : str

class PPMSetting (TypedDict):
  """ payment payment method setting """
  method : Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  info_1 : PPMI1Setting
  info_2 : PPMI2Setting
  
class PaymentSetting (TypedDict):
  personal_information : PPISetting
  delivery_method : PDMSetting
  payment_method : PPMSetting
# Payment Setting

BASE_SETTING : BasicSetting = load("setting/basic.toml")
PAYMENT_SETTING : PaymentSetting = load("setting/payment.toml")
