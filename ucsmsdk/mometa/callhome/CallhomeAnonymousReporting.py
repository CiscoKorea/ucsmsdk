"""This module contains the general information for CallhomeAnonymousReporting ManagedObject."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from ucsmo import ManagedObject
from ucscoremeta import UcsVersion, MoPropertyMeta, MoMeta
from ucsmeta import VersionMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class CallhomeAnonymousReportingConsts():
    ADMIN_STATE_OFF = "off"
    ADMIN_STATE_ON = "on"
    USER_ACKNOWLEDGED_FALSE = "false"
    USER_ACKNOWLEDGED_NO = "no"
    USER_ACKNOWLEDGED_TRUE = "true"
    USER_ACKNOWLEDGED_YES = "yes"


class CallhomeAnonymousReporting(ManagedObject):
    """This is CallhomeAnonymousReporting class."""

    consts = CallhomeAnonymousReportingConsts()
    naming_props = set([])

    mo_meta = MoMeta("CallhomeAnonymousReporting", "callhomeAnonymousReporting", "anonymousreporting", VersionMeta.Version223a, "InputOutput", 0x3fL, [], ["admin"], [u'callhomeEp'], [], [None])

    prop_meta = {
        "admin_state": MoPropertyMeta("admin_state", "adminState", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x1L, None, None, None, ["off", "on"], []), 
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version223a, MoPropertyMeta.INTERNAL, 0x2L, None, None, """((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "count": MoPropertyMeta("count", "count", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x4L, 0, 256, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, 0x8L, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302a, MoPropertyMeta.READ_ONLY, None, None, None, """((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "sleep_interval": MoPropertyMeta("sleep_interval", "sleepInterval", "uint", VersionMeta.Version223a, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x10L, None, None, """((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "user_acknowledged": MoPropertyMeta("user_acknowledged", "userAcknowledged", "string", VersionMeta.Version223a, MoPropertyMeta.READ_WRITE, 0x20L, None, None, None, ["false", "no", "true", "yes"], []), 
    }

    prop_map = {
        "adminState": "admin_state", 
        "childAction": "child_action", 
        "count": "count", 
        "dn": "dn", 
        "rn": "rn", 
        "sacl": "sacl", 
        "sleepInterval": "sleep_interval", 
        "status": "status", 
        "userAcknowledged": "user_acknowledged", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.admin_state = None
        self.child_action = None
        self.count = None
        self.sacl = None
        self.sleep_interval = None
        self.status = None
        self.user_acknowledged = None

        ManagedObject.__init__(self, "CallhomeAnonymousReporting", parent_mo_or_dn, **kwargs)
