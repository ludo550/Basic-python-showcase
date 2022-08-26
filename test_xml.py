from datetime import datetime, timedelta

import os
import xml.etree.ElementTree as ET

def modify_xml(X, Y):
    """
    :param X: integer in days to be added to date now and assigned to DEPART element
    :param Y: integer in days to be added to date now and assigned to RETURN element
    :return: void
    """
    et = ET.parse(os.path.join('resources',
                               'test_payload1.xml'))
    root_elem = et.getroot()
    _depart = root_elem.iter('DEPART')
    _return = root_elem.iter('RETURN')
    for d in _depart:
        d.text = (datetime.now() + timedelta(days=int(X))).strftime("%Y%m%d")
    for r in _return:
        r.text = (datetime.now() + timedelta(days=int(Y))).strftime("%Y%m%d")
    et.write(os.path.join('resources', 'test_payload1_Output.xml'))

modify_xml(10, 5)