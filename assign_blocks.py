#!/usr/bin/env python2.7

# board = pcbnew.LoadBoard("/home/geoff/work/provel/printer/board/printer-board.kicad_pcb")

from collections import defaultdict
from pcbnew import GetBoard


def get_pad_info(pad):
    pin_name = str(pad.GetName())
    return (pin_name,
            {'pin_name': pin_name,
             'net_code': pad.GetNetCode(),
             'net_name': pad.GetNetname()})


def get_module_info(module):
    pads = {padname: pad for padname, pad in map(get_pad_info, module.Pads())}
    ref_des = module.GetReference()
    return (ref_des,
            {'ref_des': ref_des,
             'description': module.GetDescription(),
             'pads': pads})


def get_all_module_info(board):
    return {ref_des: module for ref_des, module in
            map(get_module_info, board.GetModules())}


def make_net_list(modules):
    nets = defaultdict(lambda: {'pads': []})
    for ref_des, module in modules.items():
        for pin_name, pin in module['pads'].items():
            net = nets[pin['net_code']]
            net['net_name'] = pin['net_name']
            net['pads'].append((ref_des, pin_name))

    return nets


def main():
    modules = get_all_module_info(GetBoard())
    net_list = make_net_list(modules)


if __name__ == "__main__":
    main()
