"""This module contains the general information for ApeMenloVnic ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class ApeMenloVnicConsts():
    STATE_CREATE_PEND = "CreatePend"
    STATE_CREATING = "Creating"
    STATE_DESTROY_PEND = "DestroyPend"
    STATE_DESTROYING = "Destroying"
    STATE_MODIFY_PEND = "ModifyPend"
    STATE_MODIFYING = "Modifying"
    STATE_PRESENT = "Present"
    STATE_UNKNOWN = "Unknown"
    TYPE_ETH = "Eth"
    TYPE_FC = "Fc"
    TYPE_SCSI = "Scsi"
    TYPE_UNKNOWN = "Unknown"


class ApeMenloVnic(ManagedObject):
    """This is ApeMenloVnic class."""

    consts = ApeMenloVnicConsts()
    naming_props = set([u'name'])

    mo_meta = MoMeta("ApeMenloVnic", "apeMenloVnic", "AdapterVnic-[name]", VersionMeta.Version101e, "InputOutput", 0x1ffffL, [], ["read-only"], [u'apeMenlo', u'apePalo'], [u'apeMenloVnicStats', u'apePaloVnicStats'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version101e, MoPropertyMeta.INTERNAL, 0x1L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cookie": MoPropertyMeta("cookie", "cookie", "ulong", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2L, None, None, None, [], []), 
        "cos": MoPropertyMeta("cos", "cos", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4L, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "mac": MoPropertyMeta("mac", "mac", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """(([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F]))|0""", [], []), 
        "name": MoPropertyMeta("name", "name", "string", VersionMeta.Version101e, MoPropertyMeta.NAMING, 0x20L, None, None, """[\-\.:_a-zA-Z0-9]{1,16}""", [], []), 
        "nic_dn": MoPropertyMeta("nic_dn", "nicDn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, 0, 256, None, [], []), 
        "pif_id": MoPropertyMeta("pif_id", "pifId", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x40L, None, None, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, 0x80L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "state": MoPropertyMeta("state", "state", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x100L, None, None, None, ["CreatePend", "Creating", "DestroyPend", "Destroying", "ModifyPend", "Modifying", "Present", "Unknown"], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x200L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "type": MoPropertyMeta("type", "type", "string", VersionMeta.Version101e, MoPropertyMeta.READ_ONLY, None, None, None, None, ["Eth", "Fc", "Scsi", "Unknown"], []), 
        "uplink_port_id": MoPropertyMeta("uplink_port_id", "uplinkPortId", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x400L, None, None, None, [], []), 
        "vif_id": MoPropertyMeta("vif_id", "vifId", "uint", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x800L, None, None, None, [], []), 
        "vif_type": MoPropertyMeta("vif_type", "vifType", "byte", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x1000L, None, None, None, [], []), 
        "vlan_id": MoPropertyMeta("vlan_id", "vlanId", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x2000L, None, None, None, [], []), 
        "vntag": MoPropertyMeta("vntag", "vntag", "ushort", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x4000L, None, None, None, [], []), 
        "wwnn": MoPropertyMeta("wwnn", "wwnn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x8000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
        "wwpn": MoPropertyMeta("wwpn", "wwpn", "string", VersionMeta.Version101e, MoPropertyMeta.READ_WRITE, 0x10000L, 0, 256, """(([A-Fa-f0-9][A-Fa-f0-9]:){7}[A-Fa-f0-9][A-Fa-f0-9])|0""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cookie": "cookie", 
        "cos": "cos", 
        "dn": "dn", 
        "mac": "mac", 
        "name": "name", 
        "nicDn": "nic_dn", 
        "pifId": "pif_id", 
        "rn": "rn", 
        "sacl": "sacl", 
        "state": "state", 
        "status": "status", 
        "type": "type", 
        "uplinkPortId": "uplink_port_id", 
        "vifId": "vif_id", 
        "vifType": "vif_type", 
        "vlanId": "vlan_id", 
        "vntag": "vntag", 
        "wwnn": "wwnn", 
        "wwpn": "wwpn", 
    }

    def __init__(self, parent_mo_or_dn, name, **kwargs):
        self._dirty_mask = 0
        self.name = name
        self.child_action = None
        self.cookie = None
        self.cos = None
        self.mac = None
        self.nic_dn = None
        self.pif_id = None
        self.sacl = None
        self.state = None
        self.status = None
        self.type = None
        self.uplink_port_id = None
        self.vif_id = None
        self.vif_type = None
        self.vlan_id = None
        self.vntag = None
        self.wwnn = None
        self.wwpn = None

        ManagedObject.__init__(self, "ApeMenloVnic", parent_mo_or_dn, **kwargs)
