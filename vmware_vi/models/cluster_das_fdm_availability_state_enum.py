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


class ClusterDasFdmAvailabilityStateEnum(str, Enum):
    """
    The *ClusterDasFdmAvailabilityState_enum* enumeration describes the availability states of hosts in a vSphere HA cluster.  In the HA architecture, a agent called the Fault Domain Manager runs on each active host. These agents elect a master and the others become its slaves. The availability state assigned to a given host is determined from information reported by the Fault Domain Manager running on the host, by a Fault Domain Manager that has been elected master, and by vCenter Server. See *ClusterDasFdmHostState* for more information about the vSphere HA architecture.  Possible values: - `uninitialized`: The Fault Domain Manager for the host has not yet been   initialized.      Hence the host is not part of a vSphere HA   fault domain. This state is reported by vCenter Server or   by the host itself. - `election`: The Fault Domain Manager on the host has been initialized and   the host is either waiting to join the existing master or   is participating in an election for a new master.      This state   is reported by vCenter Server or by the host itself. - `master`: The Fault Domain Manager on the host has been elected a   master.      This state is reported by the the host itself. - `connectedToMaster`: The normal operating state for a slave host.      In this state,   the host is exchanging heartbeats with a master over   the management network, and is thus connected to it. If   there is a management network partition, the slave will be   in this state only if it is in the same partition as the master.   This state is reported by the master of a slave host. - `networkPartitionedFromMaster`: A slave host is alive and has management network connectivity, but   the management network has been partitioned.      This state is reported   by masters that are in a partition other than the one containing the   slave host; the master in the slave's partition will report the slave state   as *connectedToMaster*. - `networkIsolated`: A host is alive but is isolated from the management network.      See *ClusterDasVmSettingsIsolationResponse_enum* for the criteria   used to determine whether a host is isolated. - `hostDown`: The slave host appears to be down.      This state is reported by the   master of a slave host. - `initializationError`: An error occurred when initilizating the Fault Domain Manager   on a host due to a problem with installing the   agent or configuring it.      This condition can often be cleared by   reconfiguring HA for the host. This state is reported by vCenter   Server. - `uninitializationError`: An error occurred when unconfiguring the Fault Domain Manager   running on a host.      In order to clear this condition the host might   need to be reconnected to the cluster and reconfigured first.   This state is reported by vCenter   Server. - `fdmUnreachable`: The Fault Domain Manager (FDM) on the host cannot be reached.      This   state is reported in two unlikely situations.   - First, it is reported by     a master if the host responds to ICMP pings sent by the master over the     management network but the FDM on the host cannot be reached by the master.     This situation will occur if the FDM is unable to run or exit the     uninitialized state.   - Second, it is reported by vCenter Server if it cannot connect to a     master nor the FDM for the host. This situation would occur if all hosts     in the cluster failed but vCenter Server is still running. It may also     occur if all FDMs are unable to run or exit the uninitialized state. - `retry`: Config/Reconfig/upgrade operation has failed in first attempt and   a retry of these operations is scheduled.      If any of the retry attempts succeed, the state is set to initialized.   If all retry attempts fail, the state is set to initializationError.   This state is reported by vCenter.  ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    UNINITIALIZED = 'uninitialized'
    ELECTION = 'election'
    MASTER = 'master'
    CONNECTEDTOMASTER = 'connectedToMaster'
    NETWORKPARTITIONEDFROMMASTER = 'networkPartitionedFromMaster'
    NETWORKISOLATED = 'networkIsolated'
    HOSTDOWN = 'hostDown'
    INITIALIZATIONERROR = 'initializationError'
    UNINITIALIZATIONERROR = 'uninitializationError'
    FDMUNREACHABLE = 'fdmUnreachable'
    RETRY = 'retry'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterDasFdmAvailabilityStateEnum from a JSON string"""
        return cls(json.loads(json_str))


