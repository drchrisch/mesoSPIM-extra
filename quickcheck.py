"""This example shows how to search for controllers."""

# based on code from physikinstrumente
#
# cs28may2021

from pipython import GCSDevice, pitools


def main():
    """Search controllers on interface, show dialog and connect a controller."""
    with GCSDevice() as pidevice:
        print('search for controllers...')
        devices = pidevice.EnumerateUSB()
        for i, device in enumerate(devices):
            print('{} - {}'.format(i, device))
        item = int(input('select device to connect: '))
        # ConnectUSB(devices[item])
        pidevice.ConnectUSB(devices[item])

        # Each PI controller supports the qIDN() command which returns an
        # identification string with a trailing line feed character which
        # we "strip" away.
        print('connected: {}'.format(pidevice.qIDN().strip()))

        # Show the version info which is helpful for PI support when there
        # are any issues.
        if pidevice.HasqVER():
            print('version info: {}'.format(pidevice.qVER().strip()))

        print('Number of connected axes: {}'.format(pitools.getaxeslist(pidevice, None)))
        
        if pidevice.HasqSSN():
            print('serial number: {}'.format(pidevice.qSNN().strip()))

        print('ID of configured axes: {}'.format(pidevice.qSAI()))
        if pidevice.HasqCST():
            print('connected stages:')
            for key in pidevice.qCST().keys():
                print('\tID: {}, type: {}'.format(key, pidevice.qCST()[key]))

        print('initialize connected stages...')
        pitools.startup(pidevice, stages=None) # , refmode=REFMODE)

        # get/set referencing mode
        print('referencing mode: {}'.format(pidevice.qRON(1)[1]))

        return


if __name__ == '__main__':
    main()
