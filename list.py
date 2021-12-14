from main import days_to_units, x
import os
import logging
import datetime

print("OS " + os.name)
print("OS " + str(os.environ))

logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
loggerMain = logging.getLogger("MAIN")
loggerMain.error("Test d erreur")
loggerMain.debug('This message should go to the log file')
loggerMain.info('So should this')
loggerMain.warning('And this, too')
loggerMain.error('And non-ASCII stuff, too, like Øresund and Malmö')

loggerTutu = logging.getLogger("TUTU")

my_list = ["janvier", "fevrier", "mars"]

print(my_list[0])

my_list.append("avril")

print(my_list[len(my_list)-1])

loggerTutu.info("Mois lu: " + my_list[0])
