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


class ReplicationVmConfigFaultReasonForFaultEnum(str, Enum):
    """
    Possible values: - `incompatibleHwVersion`: Incompatible VM hardware version - `invalidVmReplicationId`: Invalid VM Replication ID string - `invalidGenerationNumber`: Invalid generation number in VM's configuration - `outOfBoundsRpoValue`: Invalid RPO value (out of bounds) - `invalidDestinationIpAddress`: Invalid destination IP address - `invalidDestinationPort`: Invalid destination port - `invalidExtraVmOptions`: Malformed extra options list - `staleGenerationNumber`: Mis-matching generation number (stale) - `reconfigureVmReplicationIdNotAllowed`: Attempting to re-configure the VM replication ID - `cannotRetrieveVmReplicationConfiguration`: Could not retrieve the VM configuration - `replicationAlreadyEnabled`: Attempting to re-enable replication for the VM - `invalidPriorConfiguration`: The existing replication configuration of the VM is broken   (applicable to re-configuration only). - `replicationNotEnabled`: Attempting to re-configure or disable replication for a VM   for which replication has not been enabled. - `replicationConfigurationFailed`: Failed to commit the new replication properties for the VM. - `encryptedVm`: VM is encrypted      ***Since:*** vSphere API 6.5 - `invalidThumbprint`: Remote certificate thumbprint is invalid      ***Since:*** vSphere API 6.7 - `incompatibleDevice`: VM hardware contains devices incompatible with replication      ***Since:*** vSphere API 6.7  ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    INCOMPATIBLEHWVERSION = 'incompatibleHwVersion'
    INVALIDVMREPLICATIONID = 'invalidVmReplicationId'
    INVALIDGENERATIONNUMBER = 'invalidGenerationNumber'
    OUTOFBOUNDSRPOVALUE = 'outOfBoundsRpoValue'
    INVALIDDESTINATIONIPADDRESS = 'invalidDestinationIpAddress'
    INVALIDDESTINATIONPORT = 'invalidDestinationPort'
    INVALIDEXTRAVMOPTIONS = 'invalidExtraVmOptions'
    STALEGENERATIONNUMBER = 'staleGenerationNumber'
    RECONFIGUREVMREPLICATIONIDNOTALLOWED = 'reconfigureVmReplicationIdNotAllowed'
    CANNOTRETRIEVEVMREPLICATIONCONFIGURATION = 'cannotRetrieveVmReplicationConfiguration'
    REPLICATIONALREADYENABLED = 'replicationAlreadyEnabled'
    INVALIDPRIORCONFIGURATION = 'invalidPriorConfiguration'
    REPLICATIONNOTENABLED = 'replicationNotEnabled'
    REPLICATIONCONFIGURATIONFAILED = 'replicationConfigurationFailed'
    ENCRYPTEDVM = 'encryptedVm'
    INVALIDTHUMBPRINT = 'invalidThumbprint'
    INCOMPATIBLEDEVICE = 'incompatibleDevice'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReplicationVmConfigFaultReasonForFaultEnum from a JSON string"""
        return cls(json.loads(json_str))


