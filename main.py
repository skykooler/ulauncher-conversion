from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import subprocess
import os

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

UNITS_EXISTS = None

class ConverterExtension(Extension):

    def __init__(self):
        super(ConverterExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

def GoodResult(text, desc=''):
    return ExtensionResultItem(icon='images/icon.png',
                               name=text,
                               description=desc,
                               on_enter=CopyToClipboardAction(text))

def BadResult(text, desc=''):
    # TODO: Change icon for failing results.
    return ExtensionResultItem(icon='images/icon.png',
                               name=text,
                               description=desc,
                               on_enter=HideWindowAction())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        global UNITS_EXISTS
        items = []
        query = event.get_argument()
        if UNITS_EXISTS is None:
            if which('units'):
                UNITS_EXISTS = True
            else:
                UNITS_EXISTS = False
        if UNITS_EXISTS:
            if " to " in query:
                start, end = query.split(" to ")
                proc = subprocess.Popen(['units', '--terse', start, end], stdout=subprocess.PIPE)
                out, err = proc.communicate()
                out = out.decode("UTF-8").strip()
                if "Unknown" in out:
                    items.append(BadResult('Invalid units', out))
                else:
                    output_unit = '%s %s' % (out, end)
                    items.append(GoodResult(output_unit))
        else:
            items.append(BadResult('Mising library', 'Please install the "units" package.'))
        return RenderResultListAction(items)

if __name__ == '__main__':
    ConverterExtension().run()
