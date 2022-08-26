import os
import json
from importlib import resources

def modify_json(filename, *args):
    """
    :param args: multiple string args that are removed from nested json
    :return: void
    """
    et = json.loads(resources.read_text('resources',
                                        'test_payload.json'))

    function_dict =  lambda remove:   \
        {k: function_dict(v) if isinstance(v, dict) else
        [i for i in v if i not in args] if isinstance(v, list) else v for k, v in remove.items()
                                     if k not in args}
    with open(os.path.join('resources',
                           filename), 'w+') as output:
        et = function_dict(et)
        output.write(json.dumps(et, indent=4))

# remove suggested fields
modify_json("test_payload_output.json", "appdate", "outParams")

# remove different fields including memebers of list
modify_json("test_payload_output2.json", "planselect_1", "dateterm", "covgsummary", "deptdt")
