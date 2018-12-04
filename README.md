Sequencer
=========
Automatic sequence generator for Sublime Text 3.

In short, it generates a sequence using the active edit regions on the open document.

## Sales pitch
Have you ever needed to insert a sequence of numbers into a text file -- at the *end* of a bunch of lines? Are you tired of having to open bash, type `seq 1 1 100`, try to match the number of edit points to your open text file, just to paste it in to find out that you messed up somewhere, and it inserted that sequence in 101 different places? Do you try to type it in manually? Fret no more! Introducing Sequencer, the Automatic sequence generator for Sublime Text 3! 

How does it work? Sequencer adds two menu commands:

- `Edit > Text > Generate Sequence (defaults)`
- `Edit > Text > Generate Sequence (interactive)`  
    
And adds two palette commands: 

-  `Sequencer: Generate Sequence (defaults)`
-  `Sequencer: Generate Sequence (interactive)` 

Now all you have to do is add a bunch of edit points, run the command, and presto! All your lines have numbers!

## Prompt Usage
Prompt asks user for values. Proper syntax:

    [start number] [interval] [flags]

Flags:

    f - enable floating point output (if not set, it will just take the floor value)
    w:x - enforce a minimum character width of x characters, padding with 0s if necessary
    pre - prefix mode. Inserts at beginning of regions instead of at the end of regions.

After enter is pressed, it will then insert the sequence in order starting from the first region in the file. If a cursor has made a selection, it will start at the end of the region (or beginning if overridden).

## Default Usage
Loads defaults from package settings. Think of it as automatically building the prompt input described above.

## Keybinding
I couldn't think of a good keybinding to use, so you're on your own with this. The interactive command is `sequencer_prompt`, and the command to use your settings file is `generate_sequence`.
