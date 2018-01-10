# Starter file for Hmmmwork6, updated for python3
# hw6 problem 3
#
# name: Yury Namgung
# date: 10/18/17
#
# Hmmm...
#
#

# These statements are to set up Hmmm...
# You'll need the files that are in this folder.
import importlib
import hmmmAssembler ; importlib.reload(hmmmAssembler)
import hmmmSimulator ; importlib.reload(hmmmSimulator)
import sys

# For cs5gold, you'll write a fibonacci program
# For cs5black, it's a recursive Hanoi-solving program

# Either way, be sure to call it Problem3 !

# This is a placeholder by that name whose code you'll replace:
Problem3 = """
00 read r1          # get Disks from user// start of main()
01 read r2          # get FromPeg from user
02 read r3          # get ToPeg from user
03 setn r15 100     # r15 = 100
04 calln r14 6      # r14 = 5, jump to line 6
05 halt             # stop
06 copy r4 r1       # r4 = r1// Start of hanoi(D, F, T)
07 addn r4 -1       # r4 = r1 - 1
08 jnezn r4 12      # if r1 != 1 jump to else case
09 write r2         # print fromPeg
10 write r3         # print ToPeg
11 jumpr r14        # jump to halt recursion 
12 add r5 r2 r3     # r5 = r2 + r3 
13 setn r6 6        # r6 = 6 (sum num of pegs)
14 sub r6 r6 r5     # r6 = other peg
15 nop
16 storer r1 r15    # store Disks into RAM memory 100
17 addn r15 1       # r15 = memory 101
18 storer r2 r15    # store FromPeg into mem 101
19 addn r15 1       # incr mem
20 storer r3 r15    # store ToPeg into mem 102
21 addn r15 1       # incr mem
22 storer r6 r15    # store OtherPeg into mem 103
23 addn r15 1       # r15 = 104
24 storer r14 r15   # store halt line into mem 104
25 addn r15 1       # mem pointer points at empty slot
26 addn r1 -1       # disk -1
27 copy r3 r6       # ToPeg = OtherPeg
28 calln r14 6      # recurse hanoi, jump back here after
29 addn r15 -1      # pointer at first content mem
30 loadr r14 r15    # load mem 104 into r14
31 addn r15 -1      # r15 = 103
32 loadr r6 r15     # load m103 into OtherPeg
33 addn r15 -1      # r15 = 102
34 loadr r3 r15     # load m102 into ToPeg
35 addn r15 -1      # r15 = 101
36 loadr r2 r15     # load m101 into FromPeg
37 addn r15 -1      # r15 = 100
38 loadr r1 r15     # load m100 into Disks
39 nop
40 storer r1 r15    # store Disks into RAM memory 100
41 addn r15 1       # r15 = memory 101
42 storer r2 r15    # store FromPeg into mem 101
43 addn r15 1       # incr mem
44 storer r3 r15    # store ToPeg into mem 102
45 addn r15 1       # incr mem
46 storer r6 r15    # store OtherPeg into mem 103
47 addn r15 1       # r15 = 104
48 storer r14 r15   # store halt line into mem 104
49 addn r15 1       # pointer points at empty mem
50 setn r1 1        # disk = 1
51 calln r14 6      # recurse hanoi
52 addn r15 -1      # pointer at first content mem
53 loadr r14 r15    # load mem 104 into r14
54 addn r15 -1      # r15 = 103
55 loadr r6 r15     # load m103 into OtherPeg
56 addn r15 -1      # r15 = 102
57 loadr r3 r15     # load m102 into ToPeg
58 addn r15 -1      # r15 = 101
59 loadr r2 r15     # load m101 into FromPeg
60 addn r15 -1      # r15 = 100
61 loadr r1 r15     # load m100 into Disks
62 nop
63 storer r1 r15    # store Disks into RAM memory 100
64 addn r15 1       # r15 = memory 101
65 storer r2 r15    # store FromPeg into mem 101
66 addn r15 1       # incr mem
67 storer r3 r15    # store ToPeg into mem 102
68 addn r15 1       # incr mem
69 storer r6 r15    # store OtherPeg into mem 103
70 addn r15 1       # r15 = 104
71 storer r14 r15   # store halt line into mem 104
72 addn r15 1       # point @ empty mem
73 addn r1 -1       # disk -1
74 copy r2 r6       # FromPeg = OtherPeg
75 calln r14 6      # recurse hanoi
76 addn r15 -1      # load from content mem
77 loadr r14 r15    # load mem 104 into r14
78 addn r15 -1      # r15 = 103
79 loadr r6 r15     # load m103 into OtherPeg
80 addn r15 -1      # r15 = 102
81 loadr r3 r15     # load m102 into ToPeg
82 addn r15 -1      # r15 = 101
83 loadr r2 r15     # load m101 into FromPeg
84 addn r15 -1      # r15 = 100
85 loadr r1 r15     # load m100 into Disks
86 jumpr r14
"""

# This function runs the Hmmm program specified by prog
#
def Hmmm(prog):
    """ This function, named Hmmm, takes in a triple-quoted Python string,
        named prog. That string, prog, should be a Hmmm program.

        See the docstring in hw6pr1.py for a full explanation!
    """
    importlib.reload(hmmmAssembler)  # make sure we're using the latest version
    importlib.reload(hmmmSimulator)  # for both assembler and simulator
    fail = hmmmAssembler.main(prog)  # assemble input into machine code
    if fail is None:
        hmmmSimulator.main(['-n'])   # run that code, don't ask for debugging...
