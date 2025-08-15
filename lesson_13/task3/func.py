import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("xml_check")

def find_by_number(number_value):
    try:
        tree = ET.parse('groups.xml')
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(number_value):
                timing = group.find('timingExbytes')
                if timing is not None:
                    incoming = timing.find('incoming')
                    incoming_text = incoming.text
                    logger.info(f"Group_id: {number_value}, Incoming: {incoming_text}")
                    return
        logger.info(f"Group_id {number_value} not found")
    except Exception as e:
        logger.error(f"Помилка: {str(e)}")

find_by_number('0')
find_by_number('1')
find_by_number('2')
find_by_number('3')
find_by_number('4')
find_by_number('5')