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


class ActionTypeEnum(str, Enum):
    """
    Pre-defined constants for possible action types.  Virtual Center uses this information to coordinate with the clients.  Possible values: - `MigrationV1`: Migration action type - `VmPowerV1`: Virtual machine power action type - `HostPowerV1`: Host power action type - `IncreaseLimitV1`: Increase resource limit action type      ***Since:*** vim disabled version - `IncreaseSizeV1`: Increase VM size, e.g., number of vcpus and memory size, action type      ***Since:*** vim disabled version - `IncreaseSharesV1`: Increase resource shares action type      ***Since:*** vim disabled version - `IncreaseReservationV1`: Increase resource reservation action type      ***Since:*** vim disabled version - `DecreaseOthersReservationV1`: Decrease other VMs' or RPs' resource reservation action type      ***Since:*** vim disabled version - `IncreaseClusterCapacityV1`: Increase cluster capacity action type      ***Since:*** vim disabled version - `DecreaseMigrationThresholdV1`: Decrease migration threshold action type      ***Since:*** vim disabled version - `HostMaintenanceV1`: Host entering maintenance mode action type      ***Since:*** vSphere API 5.0 - `StorageMigrationV1`: Storage migration action type      ***Since:*** vSphere API 5.0 - `StoragePlacementV1`: Initial placement action for a virtual machine or a virtual disk      ***Since:*** vSphere API 5.0 - `PlacementV1`: Initial placement action for a virtual machine and its virtual disks      ***Since:*** vSphere API 6.0 - `HostInfraUpdateHaV1`: Host changing infrastructure update ha mode action type.      ***Since:*** vSphere API 6.5  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    MIGRATIONV1 = 'MigrationV1'
    VMPOWERV1 = 'VmPowerV1'
    HOSTPOWERV1 = 'HostPowerV1'
    INCREASELIMITV1 = 'IncreaseLimitV1'
    INCREASESIZEV1 = 'IncreaseSizeV1'
    INCREASESHARESV1 = 'IncreaseSharesV1'
    INCREASERESERVATIONV1 = 'IncreaseReservationV1'
    DECREASEOTHERSRESERVATIONV1 = 'DecreaseOthersReservationV1'
    INCREASECLUSTERCAPACITYV1 = 'IncreaseClusterCapacityV1'
    DECREASEMIGRATIONTHRESHOLDV1 = 'DecreaseMigrationThresholdV1'
    HOSTMAINTENANCEV1 = 'HostMaintenanceV1'
    STORAGEMIGRATIONV1 = 'StorageMigrationV1'
    STORAGEPLACEMENTV1 = 'StoragePlacementV1'
    PLACEMENTV1 = 'PlacementV1'
    HOSTINFRAUPDATEHAV1 = 'HostInfraUpdateHaV1'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionTypeEnum from a JSON string"""
        return cls(json.loads(json_str))

