import os
import json
from importlib import resources
def modify_json(*args):
    et = json.loads(resources.read_text('resources',
                                        'test_payload.json'))

    function_dict =  lambda remove:   \
        {k: function_dict(v) if isinstance(v, dict) else
        [i for i in v if i not in args] if isinstance(v, list) else v for k, v in remove.items()
                                     if k not in args}
    with open(os.path.join('resources',
                           'test_payload_output.json'), 'w+') as output:
        et = function_dict(et)
        output.write(json.dumps(et, indent=4))

modify_json("planselect_1", "dateterm", "covgsummary", "deptdt")
