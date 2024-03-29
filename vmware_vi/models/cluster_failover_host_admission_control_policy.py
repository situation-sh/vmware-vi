# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import StrictInt
from pydantic import Field
from vmware_vi.models.cluster_das_admission_control_policy import ClusterDasAdmissionControlPolicy
from vmware_vi.models.managed_object_reference import ManagedObjectReference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterFailoverHostAdmissionControlPolicy(ClusterDasAdmissionControlPolicy):
    """
    The *ClusterFailoverHostAdmissionControlPolicy* dedicates one or more hosts for use during failover.  When a host fails with this policy in place, vSphere HA attempts to restart its virtual machines on a dedicated failover host. If this is not possible, for example the failover host itself has failed or it has insufficient resources, HA attempts to restart those virtual machines on another host in the cluster.  To support the availabilty of a failover host, the vCenter Server will prevent users from powering on virtual machines on that host, or from using vMotion to migrate virtual machines to the host. Also, DRS does not use the failover host for load balancing.  To obtain the status of a failover host, use the *ClusterFailoverHostAdmissionControlInfo.hostStatus* property (*ClusterComputeResourceSummary*.*ClusterComputeResourceSummary.admissionControlInfo*.*ClusterFailoverHostAdmissionControlInfo.hostStatus*).  ***Since:*** vSphere API 4.0 
    """ # noqa: E501
    failover_hosts: Optional[List[ManagedObjectReference]] = Field(default=None, description="List of managed object references to failover hosts.  ***Since:*** vSphere API 4.0  Refers instances of *HostSystem*. ", alias="failoverHosts")
    failover_level: Optional[StrictInt] = Field(default=None, description="Number of host failures that should be tolerated, still guaranteeing sufficient resources to restart virtual machines on available hosts.  If not set, we assume 1.  ***Since:*** vSphere API 6.5 ", alias="failoverLevel")
    __properties: ClassVar[List[str]] = ["_typeName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterFailoverHostAdmissionControlPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ClusterFailoverHostAdmissionControlPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


