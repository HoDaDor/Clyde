from __future__ import unicode_literals
# -*- coding: utf-8 -*-

from pandas import DataFrame as dtf
from pathlib import Path
import yaml
import subprocess

"""
[Package Updater]
"""


# CLI Data Framer Masterclass is meow in session...
class Clyde(object):


    '''

        Meet CLI! His real name is 'Clyde', but we call him CLI anyway because he is pretending to be the real CLI by creating a subprocess that listens for either user input or a set of pre-defined arguments and return the result in a pandas dataframe..

        He thinks he is being clever and that we haven't noticed yet but we're onto him and but we play along anyway in order to buy to us some time to find out what he did to the real CLI...

        Attributes
        ----------
        None, Nada, Zip, Nil, Null, He's not the real Clyde, run...

        Methods
        -------
        cli : list

    '''



    # Do things before students arrive
    def __init__(self):
        pass
        # self.packages = None


    # leave @profile commented out unless needed for memory profiling
    # @profile
    def cli(self, *commands):

        # Clyde opens a subprocess and passes along the information he was instructed to relay to the real CLI..
        with subprocess.Popen(
            *commands,  # relayed information for Clyde
            stdout=subprocess.PIPE,  # Pipe Clyde's response through CLI
            stderr=subprocess.STDOUT,  # Pipe any errors(STDERR and/or cries for help) through STDOUT
            shell=True,  # Use a new shell
            bufsize=1,  # Set buffer size?
            universal_newlines=True  # Set new line character so we won't need to worry about having to deal with any byte code conversion nonsense.
        ) as cli:  # Hi CLI!

            # Fake CLI makes a copy of real CLI's message
            self.cli_output = dtf(cli.stdout.readlines())

            # CLI flushes the original message down the toilet... Suuuper shady of him... What's he hiding?... What's he not telling us...
            cli.stdout.flush()

        # Deciphered the message; it appears to be some sort of list of files for something... But what is a pip? And what do these 'Packages' and 'Version' entries mean?!... Hmmm... So many mysteries...
        return dtf(
            [
                each_new_line.split(" ") for each_new_line in [
                    " ".join(entry.split()) for entry in [
                        line.replace("\n", "") for line in self.cli_output[0]
                    ]
                ]
            ][2:],
            columns=[
                "Package",
                "Version"
            ]
        )


    def archive_pip(self):
        self.cli("cmd, /c pip list")
        new_config = open(f"{Path('./packages_archive_lise.yml')}",'w')
        yaml.dump(result['Package'])


    def restore_pip(self):
        # Open and read new config in rewritable mode
        packages = yaml.safe_load(open(f"{Path('packages_archive_lise.yml')}","rb"))
        for each_package in packages:
            os.system(f'pip install {each_package} --upgrade')


# Main entry point is main
# leave @profile commented out unless needed for memory profiling
# @profile
def main():

    import argparse

    # Instantiate parser
    parser = argparse.ArgumentParser()

    # Init list vars
    old, new = ([], )*2

    # Initialize communication with Clyde
    cli = Clyde()

    # Define path to workbook argument
    parser.add_argument(
        '-archive',
        '--archive',
        help='Archive current python list to file',
    )

    # Define table selector argument
    parser.add_argument(
        '-restore',
        '--restore',
        type=int,
        help='Restore archived python libraries from file list',
    )

    # parse arguments
    parsed = parser.parse_args()

    # If the current OS this script is running on is OSX, we will need to import appscript dependencies and use the OSX specific Formatter object WBFormatter_OSX, a subclass of WBFormatter but with overloaded functions with OSX specific code.
    if parsed.archive:
        cli.archive_pip()

    if parsed.restore:
        cli.restore_pip()

    else:
        # start subprocess and log data as 'result'
        result = cli.cli(
            f"cmd, /c {input('Enter a command with arguments as you normally would if entering them directly in a terminal window: ')}",
            ).split(", ")

        print(result['Package'])
        # Inform the others about Clyde's message
        print(
            f"Your result:\n{result}"
        )


# ID the executor, if his/her/it/they/them/wtfbbq/attack-hellicopter name is "main", then run main method. Otherwise, ignore them.
if __name__ in "__main__":
    main()
