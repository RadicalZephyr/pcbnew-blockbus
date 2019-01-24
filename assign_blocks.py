#!/usr/bin/env python2.7

# board = pcbnew.LoadBoard("/home/geoff/work/provel/printer/board/printer-board.kicad_pcb")

from pcbnew import GetBoard


def get_pad_info(pad):
    return (pad.GetName(), {'netcode': pad.GetNetCode(), 'netname': pad.GetNetname()})


def get_module_info(module):
    pads = {padname: pad for padname, pad in map(get_pad_info, module.Pads())}
    return {'refdes': module.GetReference(), 'description': module.GetDescription(), 'pads': pads}


def main():
    board = GetBoard()

    modules = [get_module_info(m) for m in board.GetModules()]


if __name__ == "__main__":
    main()
