# -*- coding: utf-8 -*-

import logging
import time
from ucsmsdk.ucseventhandler import UcsEventHandle
from ucsmsdk.mometa.ls.LsServer import LsServerConsts
from connection.info import ucs_login, ucs_logout

handle = None
log = logging.getLogger('ucs')
log.setLevel(logging.DEBUG)

def _convert_name( name):
    if name.startswith('sys/'):
        return name[4:]
    else:
        return name

def _fault_target( name):
    if name.startswith('sys/'):
        return name.split('/')[1]
    elif name.startswith('fabric/lan/'):
        items = name.split('/')
        return items[ len(items)-2]
    else:
        return '/'.join(name.split('/')[0:-1])

def _get_inventory(handle, subject=None):
    inventories = []
    chassises = handle.query_classid(class_id='EquipmentChassis')
    if len(chassises) == 0:
        return []
    for chassis in chassises:
        blades = handle.query_children(in_mo=chassis, class_id="ComputeBlade")
        for blade in blades:
            firmware = None
            mgmts = handle.query_children(in_mo=blade, class_id="MgmtController")
            for mgmt in mgmts:
                fws = handle.query_children(in_mo=mgmt, class_id="FirmwareRunning")
                for fw in fws:
                    if fw.deployment == 'system': firmware = fw.version
            print (blade.model, blade.serial, _convert_name(blade.dn), firmware, blade.mfg_time)
    racks = handle.query_classid(class_id='ComputeRackUnit')
    if len(racks) == 0:
        return []
    for rack in racks:
        firmware = None
        mgmts = handle.query_children(in_mo=rack, class_id="MgmtController")
        for mgmt in mgmts:
            fws = handle.query_children(in_mo=mgmt, class_id="FirmwareRunning")
            for fw in fws:
                if fw.deployment == 'system': firmware = fw.version
        print( rack.model, rack.serial, _convert_name(rack.dn), firmware, rack.mfg_time)

    networks = handle.query_classid( class_id='NetworkElement')
    for network in networks:
        firmware = None
        mgmts = handle.query_children(in_mo=network, class_id="MgmtController")
        for mgmt in mgmts:
            fws = handle.query_children(in_mo=mgmt, class_id="FirmwareRunning")
            for fw in fws:
                if fw.deployment == 'system': firmware = fw.version
        print ( network.model, network.serial, network.oob_if_ip, _convert_name(network.dn), firmware)

def _print_fault_info( faults):
    for fault in faults:
        print( fault.severity, fault.code, _fault_target(fault.dn), fault.created, fault.descr, fault.occur)

def _get_faults(handle):
    #severity=critial
    faults = handle.query_classid(class_id='FaultInst', filter_str='(severity,"critical",type="eq")')
    if faults:
        _print_fault_info(faults)
    #severity=major
    faults = handle.query_classid(class_id='FaultInst', filter_str='(severity,"major",type="eq")')
    if faults:
        _print_fault_info(faults)
    #severity=warning
    faults = handle.query_classid(class_id='FaultInst', filter_str='(severity,"warning",type="eq")')
    if faults:
        _print_fault_info(faults)         


def main():
    try:
        global handle
        handle = ucs_login()
        #get faults
        _get_faults(handle)
        # get inventory 
        #_get_inventory(handle)
        ucs_logout(handle)
    except:
        ucs_logout(handle)
        raise

main()

