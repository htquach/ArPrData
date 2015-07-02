# Copyright (c) 2015 Hong Quach

# This source file is licensed under the "MIT License."  Please see the LICENSE
# in this distribution for license terms.


class APD(object):
    def get_db_source_connection(self):
        return {}

    def get_db_destination_connection(self):
        return {}

    def run(self):
        raise NotImplemented


def main():
    apd = APD()
    apd.run()


if __name__ == "__main__":
    main()


