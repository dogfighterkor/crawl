from .rt import RT
from .metac_m import METAC_M
from .daum import DAUM

def run():
	list = [RT, DAUM, METAC_M]
	for item in list:
		item()
