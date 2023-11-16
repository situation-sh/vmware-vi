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
from pydantic import StrictInt, StrictStr
from pydantic import Field
from vmware_vi.models.cluster_compute_resource_vcs_slots import ClusterComputeResourceVcsSlots
from vmware_vi.models.cluster_das_admission_control_info import ClusterDasAdmissionControlInfo
from vmware_vi.models.cluster_das_data import ClusterDasData
from vmware_vi.models.cluster_usage_summary import ClusterUsageSummary
from vmware_vi.models.compute_resource_summary import ComputeResourceSummary
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterComputeResourceSummary(ComputeResourceSummary):
    """
    The *ClusterComputeResourceSummary* data object encapsulates runtime properties of a *ClusterComputeResource*. 
    """ # noqa: E501
    current_failover_level: StrictInt = Field(description="Deprecated as of vSphere API 4.0, use *ClusterFailoverLevelAdmissionControlInfo.currentFailoverLevel*.  Current failover level.  This is the number of physical host failures that can be tolerated without impacting the ability to satisfy the minimums for all running virtual machines. This represents the current value, as opposed to desired value configured by the user. ", alias="currentFailoverLevel")
    admission_control_info: Optional[ClusterDasAdmissionControlInfo] = Field(default=None, alias="admissionControlInfo")
    num_vmotions: StrictInt = Field(description="Total number of migrations with VMotion that have been done internal to this cluster. ", alias="numVmotions")
    target_balance: Optional[StrictInt] = Field(default=None, description="The target balance, in terms of standard deviation, for a DRS cluster.  Units are thousandths. For example, 12 represents 0.012.  ***Since:*** vSphere API 4.0 ", alias="targetBalance")
    current_balance: Optional[StrictInt] = Field(default=None, description="The current balance, in terms of standard deviation, for a DRS cluster.  Units are thousandths. For example, 12 represents 0.012.  ***Since:*** vSphere API 4.0 ", alias="currentBalance")
    drs_score: Optional[StrictInt] = Field(default=None, description="The DRS score of this cluster, in percentage.  ***Since:*** vSphere API 7.0 ", alias="drsScore")
    num_vms_per_drs_score_bucket: Optional[List[StrictInt]] = Field(default=None, description="The number of VMs in this cluster corresponding to each DRS score bucket.  The buckets are defined as follows: - 0% - 20% - 21% - 40% - 41% - 60% - 61% - 80% - 81% - 100%    ***Since:*** vSphere API 7.0 ", alias="numVmsPerDrsScoreBucket")
    usage_summary: Optional[ClusterUsageSummary] = Field(default=None, alias="usageSummary")
    current_evc_mode_key: Optional[StrictStr] = Field(default=None, description="The Enhanced VMotion Compatibility mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.  See also *Capability.supportedEVCMode*.  ***Since:*** vSphere API 4.0 ", alias="currentEVCModeKey")
    current_evc_graphics_mode_key: Optional[StrictStr] = Field(default=None, description="The Enhanced VMotion Compatibility Graphics mode that is currently in effect for all hosts in this cluster; unset if no EVC mode is active.  See also *Capability.supportedEVCGraphicsMode*.  ***Since:*** vSphere API 7.0.1.0 ", alias="currentEVCGraphicsModeKey")
    das_data: Optional[ClusterDasData] = Field(default=None, alias="dasData")
    cluster_maintenance_mode_status: Optional[StrictStr] = Field(default=None, description="Configuration pertinent to state of the cluster maintenance mode.  Valid values are enumerated by the *ClusterMaintenanceModeStatus* type.  ***Since:*** vSphere API 7.0.0.2 ", alias="clusterMaintenanceModeStatus")
    vcs_health_status: Optional[StrictStr] = Field(default=None, description="The health status of the vSphere Cluster Services in the cluster.  Supported values are enumerated by the *VcsHealthStatus* type.  ***Since:*** vSphere API 7.0.1.1 ", alias="vcsHealthStatus")
    vcs_slots: Optional[List[ClusterComputeResourceVcsSlots]] = Field(default=None, description="An array of hosts and number of resource slots on the host for vSphere Cluster Services in the cluster.  The number of resource slots on the host includes both following types: 1\\. Number of vCS VMs running on the host (resource reserved and occupied). 2\\. Number of reserved and unoccupied slots (reserved for new vCS VMs).  ***Since:*** vSphere API 7.0.1.1 ", alias="vcsSlots")
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
        """Create an instance of ClusterComputeResourceSummary from a JSON string"""
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
        """Create an instance of ClusterComputeResourceSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


