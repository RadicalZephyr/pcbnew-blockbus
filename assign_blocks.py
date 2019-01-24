#!/usr/bin/env python2.7

# board = pcbnew.LoadBoard("/home/geoff/work/provel/printer/board/printer-board.kicad_pcb")

def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

from pcbnew import *

def main():
    board = GetBoard()

    modules = board.GetModules() # Iterable, not indexable
    for module in modules:
        pads = list(module.Pads())
        if len(pads) > 0:
            for pad in pads:
                net = pad.GetNet()



if __name__ == "__main__":
    main()
