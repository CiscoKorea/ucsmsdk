"""This module contains the general information for ComputeIOHubEnvStatsHist ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class ComputeIOHubEnvStatsHistConsts:
    MOST_RECENT_FALSE = "false"
    MOST_RECENT_NO = "no"
    MOST_RECENT_TRUE = "true"
    MOST_RECENT_YES = "yes"
    SUSPECT_FALSE = "false"
    SUSPECT_NO = "no"
    SUSPECT_TRUE = "true"
    SUSPECT_YES = "yes"
    TEMPERATURE_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_AVG_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MAX_NOT_APPLICABLE = "not-applicable"
    TEMPERATURE_MIN_NOT_APPLICABLE = "not-applicable"


class ComputeIOHubEnvStatsHist(ManagedObject):
    """This is ComputeIOHubEnvStatsHist class."""

    consts = ComputeIOHubEnvStatsHistConsts()
    naming_props = set([u'id'])

    mo_meta = MoMeta("ComputeIOHubEnvStatsHist", "computeIOHubEnvStatsHist", "[id]", VersionMeta.Version131c, "OutputOnly", 0xf, [], ["read-only"], [u'computeIOHubEnvStats'], [], ["Get"])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", VersionMeta.Version131c, MoPropertyMeta.INTERNAL, None, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x2, 0, 256, None, [], []), 
        "id": MoPropertyMeta("id", "id", "ulong", VersionMeta.Version131c, MoPropertyMeta.NAMING, None, None, None, None, [], []), 
        "most_recent": MoPropertyMeta("most_recent", "mostRecent", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", VersionMeta.Version302c, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "status": MoPropertyMeta("status", "status", "string", VersionMeta.Version131c, MoPropertyMeta.READ_WRITE, 0x8, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "suspect": MoPropertyMeta("suspect", "suspect", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "temperature": MoPropertyMeta("temperature", "temperature", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_avg": MoPropertyMeta("temperature_avg", "temperatureAvg", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_max": MoPropertyMeta("temperature_max", "temperatureMax", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "temperature_min": MoPropertyMeta("temperature_min", "temperatureMin", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, ["not-applicable"], ["0-4294967295"]), 
        "thresholded": MoPropertyMeta("thresholded", "thresholded", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, None, [], []), 
        "time_collected": MoPropertyMeta("time_collected", "timeCollected", "string", VersionMeta.Version131c, MoPropertyMeta.READ_ONLY, None, None, None, r"""([0-9]){4}-([0-9]){2}-([0-9]){2}T([0-9]){2}:([0-9]){2}:([0-9]){2}((\.([0-9]){3})){0,1}""", [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "dn": "dn", 
        "id": "id", 
        "mostRecent": "most_recent", 
        "rn": "rn", 
        "sacl": "sacl", 
        "status": "status", 
        "suspect": "suspect", 
        "temperature": "temperature", 
        "temperatureAvg": "temperature_avg", 
        "temperatureMax": "temperature_max", 
        "temperatureMin": "temperature_min", 
        "thresholded": "thresholded", 
        "timeCollected": "time_collected", 
    }

    def __init__(self, parent_mo_or_dn, id, **kwargs):
        self._dirty_mask = 0
        self.id = id
        self.child_action = None
        self.most_recent = None
        self.sacl = None
        self.status = None
        self.suspect = None
        self.temperature = None
        self.temperature_avg = None
        self.temperature_max = None
        self.temperature_min = None
        self.thresholded = None
        self.time_collected = None

        ManagedObject.__init__(self, "ComputeIOHubEnvStatsHist", parent_mo_or_dn, **kwargs)
