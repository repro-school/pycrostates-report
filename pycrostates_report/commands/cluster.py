import argparse
from pathlib import Path

from .._version import __version__

def my_bids_app(bids_dir, skip_bids_validation):
    print("bids_dir: ", bids_dir)
    print("skip_bids_validation: ", skip_bids_validation)
    return()

def main():
    #Create parser
    parser = argparse.ArgumentParser(description='BIDS app for EEg microstates clustering.')
    parser.add_argument('bids_dir', action='store', type=Path, help='The BIDS dataset to analyze.')
    parser.add_argument('--skip_bids_validation', default=False,
                        help='Skip BIDS validation (default: False).',
                        action="store_true")
    parser.add_argument('-v', '--version', action='version',
                        version='BIDS-App version {}'.format(__version__))
    args = parser.parse_args()

    # Parse arguments
    bids_dir = args.bids_dir
    skip_bids_validation = args.skip_bids_validation

    # Run the BIDS App
    my_bids_app(bids_dir, skip_bids_validation)
