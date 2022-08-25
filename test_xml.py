from datetime import datetime
from datetime import timedelta

import os
import xml.etree.ElementTree as ET

def modify_xml(X, Y):
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