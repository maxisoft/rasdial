__author__ = 'maxisoft'

import subprocess
import shlex

_DEFAULT_CMD = "rasdial"
_CONNECT_PARAMS = ('domain', 'phone', 'callback', 'phonebook', 'prefixsuffix')


def get_current_vpn(return_popen=False):
    popen = subprocess.Popen(shlex.split(_DEFAULT_CMD), stdout=subprocess.PIPE)
    if return_popen:
        return popen
    stdoutdata, _ = popen.communicate()
    spliteddata = stdoutdata.split(b'\n')
    if len(spliteddata) > 3:
        return str(spliteddata[1])
    return None


def is_connected():
    return bool(get_current_vpn())


def _returnResult(popen, return_popen, wait):
    ret = None
    if wait:
        ret = popen.wait() == 0
    if return_popen:
        return popen
    return ret


def connect(entryname, user, password, wait=True, return_popen=False, **kwargs):
    cmd = '{} "{}" "{}" "{}"'.format(_DEFAULT_CMD, entryname, user, password)
    if kwargs:
        for param in _CONNECT_PARAMS:
            kparam = kwargs.get(param)
            if kparam is not None:
                cmd += ' /{}:"{}"'.format(param, kparam)
    popen = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    return _returnResult(popen, return_popen, wait)


def disconnect(entryname, wait=True, return_popen=False):
    cmd = '{} "{}" /disconnect '.format(_DEFAULT_CMD, entryname)
    popen = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    return _returnResult(popen, return_popen, wait)


def reconnect(entryname, user, password, wait=True, return_popen=False, **kwargs):
    return disconnect(entryname, wait=True, return_popen=return_popen), connect(entryname, user, password, wait=wait,
                                                                                return_popen=return_popen, **kwargs)