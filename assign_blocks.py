#!/usr/bin/env python2.7

# board = pcbnew.LoadBoard("/home/geoff/work/provel/printer/board/printer-board.kicad_pcb")

from collections import defaultdict
from pcbnew import GetBoard


def get_pad_info(pad):
    pinname = str(pad.GetName())
    return (pinname,
            {'pinname': pinname,
             'netcode': pad.GetNetCode(),
             'netname': pad.GetNetname()})


def get_module_info(module):
    pads = {padname: pad for padname, pad in map(get_pad_info, module.Pads())}
    refdes = module.GetReference()
    return (refdes,
            {'refdes': refdes,
             'description': module.GetDescription(),
             'pads': pads})


def get_all_module_info(board):
    return {refdes: module for refdes, module in
            map(get_module_info, board.GetModules())}


def make_netlist(modules):
    nets = defaultdict(lambda: {'pads': []})
    for refdes, module in modules.items():
        for pin_name, pin in module['pads'].items():
            net = nets[pin['netcode']]
            net['netname'] = pin['netname']
            net['pads'].append((refdes, pin_name))

    return nets


def main():
    modules = get_all_module_info(GetBoard())
    netlist = make_netlist(modules)


if __name__ == "__main__":
    main()
