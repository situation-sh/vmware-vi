# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RecommendationReasonCodeEnum(str, Enum):
    """
    List of defined migration reason codes:  Possible values: - `fairnessCpuAvg`: Balance average CPU utilization. - `fairnessMemAvg`: Balance average memory utilization. - `jointAffin`: Fulfill affinity rule. - `antiAffin`: Fulfill anti-affinity rule. - `hostMaint`: Host entering maintenance mode. - `enterStandby`: Host entering standby mode. - `reservationCpu`: balance CPU reservations - `reservationMem`: balance memory reservations - `powerOnVm`: Power on virtual machine - `powerSaving`: Power off host for power savings - `increaseCapacity`: Power on host to increase cluster capacity - `checkResource`: Sanity-check resource pool hierarchy      ***Since:*** vSphere API 4.0 - `unreservedCapacity`: Maintain unreserved capacity      ***Since:*** vSphere API 4.0 - `colocateCommunicatingVM`: Co-locate communicating VMs      ***Since:*** vim disabled version - `balanceNetworkBandwidthUsage`: Balance average network bandwidth utilization      ***Since:*** vim disabled version - `vmHostHardAffinity`: Fix hard VM/host affinity rule violation      ***Since:*** vSphere API 4.1 - `vmHostSoftAffinity`: Fix soft VM/host affinity rule violation      ***Since:*** vSphere API 4.1 - `increaseAllocation`: Increase resource allocation for a VM or VMs      ***Since:*** vim disabled version - `balanceDatastoreSpaceUsage`: Balance datastore space usage.      ***Since:*** vSphere API 5.0 - `balanceDatastoreIOLoad`: Balance datastore I/O workload.      ***Since:*** vSphere API 5.0 - `balanceDatastoreIOPSReservation`: Balance datastore IOPS reservation      ***Since:*** vSphere API 6.0 - `datastoreMaint`: Datastore entering maintenance mode.      ***Since:*** vSphere API 5.0 - `virtualDiskJointAffin`: Fix virtual disk affinity rule violation.      ***Since:*** vSphere API 5.0 - `virtualDiskAntiAffin`: Fix virtual disk anti-affinity rule violation.      ***Since:*** vSphere API 5.0 - `datastoreSpaceOutage`: Fix the issue that a datastore run out of space.      ***Since:*** vSphere API 5.0 - `storagePlacement`: Satisfy storage initial placement requests.      ***Since:*** vSphere API 5.0 - `iolbDisabledInternal`: IO load balancing was disabled internally.      ***Since:*** vSphere API 5.0 - `xvmotionPlacement`: Satisfy unified vmotion placement requests.      ***Since:*** vSphere API 6.0 - `networkBandwidthReservation`: Fix network bandwidth reservation violation      ***Since:*** vSphere API 6.0 - `hostInDegradation`: Host is partially degraded.      ***Since:*** vSphere API 6.5 - `hostExitDegradation`: Host is not degraded.      ***Since:*** vSphere API 6.5 - `maxVmsConstraint`: Fix maxVms constraint violation      ***Since:*** vSphere API 6.5 - `ftConstraints`: Fix ft maxVMs and maxVcpus constraint violations      ***Since:*** vSphere API 6.5 - `vmHostAffinityPolicy`: Fix VM/host affinity policy violation      ***Since:*** vSphere API 6.8.7 - `vmHostAntiAffinityPolicy`: Fix VM/host anti-affinity policy violation      ***Since:*** vSphere API 6.8.7 - `vmAntiAffinityPolicy`: Fix VM-VM anti-affinity policy violations      ***Since:*** vSphere API 6.8.7 - `balanceVsanUsage`: ***Since:*** vSphere API 7.0.2.0  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    FAIRNESSCPUAVG = 'fairnessCpuAvg'
    FAIRNESSMEMAVG = 'fairnessMemAvg'
    JOINTAFFIN = 'jointAffin'
    ANTIAFFIN = 'antiAffin'
    HOSTMAINT = 'hostMaint'
    ENTERSTANDBY = 'enterStandby'
    RESERVATIONCPU = 'reservationCpu'
    RESERVATIONMEM = 'reservationMem'
    POWERONVM = 'powerOnVm'
    POWERSAVING = 'powerSaving'
    INCREASECAPACITY = 'increaseCapacity'
    CHECKRESOURCE = 'checkResource'
    UNRESERVEDCAPACITY = 'unreservedCapacity'
    COLOCATECOMMUNICATINGVM = 'colocateCommunicatingVM'
    BALANCENETWORKBANDWIDTHUSAGE = 'balanceNetworkBandwidthUsage'
    VMHOSTHARDAFFINITY = 'vmHostHardAffinity'
    VMHOSTSOFTAFFINITY = 'vmHostSoftAffinity'
    INCREASEALLOCATION = 'increaseAllocation'
    BALANCEDATASTORESPACEUSAGE = 'balanceDatastoreSpaceUsage'
    BALANCEDATASTOREIOLOAD = 'balanceDatastoreIOLoad'
    BALANCEDATASTOREIOPSRESERVATION = 'balanceDatastoreIOPSReservation'
    DATASTOREMAINT = 'datastoreMaint'
    VIRTUALDISKJOINTAFFIN = 'virtualDiskJointAffin'
    VIRTUALDISKANTIAFFIN = 'virtualDiskAntiAffin'
    DATASTORESPACEOUTAGE = 'datastoreSpaceOutage'
    STORAGEPLACEMENT = 'storagePlacement'
    IOLBDISABLEDINTERNAL = 'iolbDisabledInternal'
    XVMOTIONPLACEMENT = 'xvmotionPlacement'
    NETWORKBANDWIDTHRESERVATION = 'networkBandwidthReservation'
    HOSTINDEGRADATION = 'hostInDegradation'
    HOSTEXITDEGRADATION = 'hostExitDegradation'
    MAXVMSCONSTRAINT = 'maxVmsConstraint'
    FTCONSTRAINTS = 'ftConstraints'
    VMHOSTAFFINITYPOLICY = 'vmHostAffinityPolicy'
    VMHOSTANTIAFFINITYPOLICY = 'vmHostAntiAffinityPolicy'
    VMANTIAFFINITYPOLICY = 'vmAntiAffinityPolicy'
    BALANCEVSANUSAGE = 'balanceVsanUsage'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RecommendationReasonCodeEnum from a JSON string"""
        return cls(json.loads(json_str))


