
import sys
from bl.dict import Dict
from bl.string import String

class Styles(Dict):
    
    @classmethod
    def render(Class, styles, margin="", indent="\t", log=print):
        """output css text from styles. 
        margin is what to put at the beginning of every line in the output.
        indent is how much to indent indented lines (such as inside braces).
        """
        from unum import Unum
        def render_dict(d):
            return ('{\n' 
                    + Class.render(styles[k], 
                        margin=margin+indent,   # add indent to margin
                        indent=indent) 
                    + '}')

        # render the css text
        s = ""
        for k in styles.keys():
            s += margin + k + ' '
            if type(styles[k]) in [str, String]:
                s += styles[k] + ';'
            elif type(styles[k])==Unum:
                s += str(styles[k]) + ';'
            elif type(styles[k]) in [dict, Dict]:
                s += render_dict(styles[k])
            elif type(styles[k]) in [tuple, list]:
                for i in styles[k]:
                    if type(i) in [str, String]:
                        s += i + ' '
                    if type(i) == bytes:
                        s += str(i, 'utf-8') + ' '
                    elif type(i) in [dict, Dict]:
                        s += render_dict(i)
            else:
                log(margin, type(styles[k]), k, styles[k], file=sys.stderr)
                s += ';'
            s += '\n'
        return s

