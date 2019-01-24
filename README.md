# PCBlock

This is an extension for the pcbnew program in the Kicad EDA package.

The intent is that one way to think about laying out a circuit board
is in terms of "blocks" of components and the trace "busses" that
connect them.

To illustrate what I mean, it's common that a group of parts ought to
be colocated physically on the board, because they all serve to
accomplish a single unified purpose. Common traits of such a block of
components are that the traces in between these components should be
short, and that only a small number of traces connect the block to a
completely separate area on the board.  For instance, a digital input
pin may have several passives related to it that do signal
conditioning, but there is still essentially only one trace that needs
to connect to the micro controller.

The concept of busses comes in when several component blocks need to
be co-located, for instance because they all connect to the same
header. In this case, conceptually the header and all of the
individual line blocks become one large block of components, and
often all the lines will connect to the same component on the other
end. So a "bus" is a group of traces that really ought to be routed
together for simplicity.


My concept with this plugin is that if we can work at this higher
level of abstraction, then rearranging groups of components on a board
can be done at the level of these groups and blocks.  Each block still
needs to be routed manually (or autorouted at the smaller scope!), but
the routing of the busses should be almost trivial to do in a clean
manner while minimizing the need for traces to cross each other. It
may even be possible to give hints when the exact pinout for a bus
introduces suboptimal routing by arbitrarily causing lines within the
bus to cross each other. This would work on the assumption that all
lines in a block are for an equivalent purpose and the pins they
attach to can arbitrarily be swapped.


# License

Copyright 2019 Geoff Shannon

Released under the Apache License 2.0.
