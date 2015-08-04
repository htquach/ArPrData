# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.
"""The main driver for the ArPrData application."""
import arpr

def main():
    """Main driver"""
    archive_and_purge_data = arpr.ArPr("configs/policies.yml")
    archive_and_purge_data.run()


if __name__ == "__main__":
    main()


