
import yaml
import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s')
logging.getLogger().setLevel(logging.INFO)

with open('config.yaml') as file:
    try:
        cfg = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        logging.error(exc)

logging.info(cfg)
while True:
    print('Your name is:', cfg['first_name'], ' ',
          cfg['middle_name'], ' ', cfg['last_name'])
    time.sleep(10)
