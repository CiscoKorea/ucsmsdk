"""This module contains the meta information of ConfigInstallAllImpact ExternalMethod."""
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ucscoremeta import MethodMeta, MethodPropertyMeta
sys.path.remove(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

method_meta = MethodMeta("ConfigInstallAllImpact", "configInstallAllImpact", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "Xs:string", "Version142b", "InputOutput", False),
    "dn": MethodPropertyMeta("Dn", "dn", "ReferenceObject", "Version142b", "InputOutput", False),
    "in_blade_pack_version": MethodPropertyMeta("InBladePackVersion", "inBladePackVersion", "Xs:string", "Version142b", "Input", False),
    "in_host_pack_dns": MethodPropertyMeta("InHostPackDns", "inHostPackDns", "DnSet", "Version142b", "Input", True),
    "in_infra_pack_version": MethodPropertyMeta("InInfraPackVersion", "inInfraPackVersion", "Xs:string", "Version142b", "Input", False),
    "in_m_series_pack_version": MethodPropertyMeta("InMSeriesPackVersion", "inMSeriesPackVersion", "Xs:string", "Version142b", "Input", False),
    "in_rack_pack_version": MethodPropertyMeta("InRackPackVersion", "inRackPackVersion", "Xs:string", "Version142b", "Input", False),
    "out_config_set": MethodPropertyMeta("OutConfigSet", "outConfigSet", "ConfigSet", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "dn": "dn",
    "inBladePackVersion": "in_blade_pack_version",
    "inHostPackDns": "in_host_pack_dns",
    "inInfraPackVersion": "in_infra_pack_version",
    "inMSeriesPackVersion": "in_m_series_pack_version",
    "inRackPackVersion": "in_rack_pack_version",
    "outConfigSet": "out_config_set",
}
