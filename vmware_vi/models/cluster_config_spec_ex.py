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
from pydantic import StrictBool
from pydantic import Field
from vmware_vi.models.cluster_crypto_config_info import ClusterCryptoConfigInfo
from vmware_vi.models.cluster_das_config_info import ClusterDasConfigInfo
from vmware_vi.models.cluster_das_vm_config_spec import ClusterDasVmConfigSpec
from vmware_vi.models.cluster_dpm_config_info import ClusterDpmConfigInfo
from vmware_vi.models.cluster_dpm_host_config_spec import ClusterDpmHostConfigSpec
from vmware_vi.models.cluster_drs_config_info import ClusterDrsConfigInfo
from vmware_vi.models.cluster_drs_vm_config_spec import ClusterDrsVmConfigSpec
from vmware_vi.models.cluster_group_spec import ClusterGroupSpec
from vmware_vi.models.cluster_infra_update_ha_config_info import ClusterInfraUpdateHaConfigInfo
from vmware_vi.models.cluster_orchestration_info import ClusterOrchestrationInfo
from vmware_vi.models.cluster_proactive_drs_config_info import ClusterProactiveDrsConfigInfo
from vmware_vi.models.cluster_rule_spec import ClusterRuleSpec
from vmware_vi.models.cluster_system_vms_config_spec import ClusterSystemVMsConfigSpec
from vmware_vi.models.cluster_vm_orchestration_spec import ClusterVmOrchestrationSpec
from vmware_vi.models.compute_resource_config_spec import ComputeResourceConfigSpec
from vmware_vi.models.vsan_cluster_config_info import VsanClusterConfigInfo
from vmware_vi.models.vsan_host_config_info import VsanHostConfigInfo
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ClusterConfigSpecEx(ComputeResourceConfigSpec):
    """
    The *ClusterConfigSpecEx* data object provides a set of update specifications for complete cluster configuration.  You can configure a cluster when you create a new cluster (the *Folder.CreateClusterEx* method) or when you reconfigure an existing cluster (the *ComputeResource.ReconfigureComputeResource_Task* method).  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied.  Use the properties defined for this object to configure the following services: - HA (High Availability) -   provides failover protection for virtual machines   running in a cluster of ESX Server hosts.   The virtual machines are located in a *Datastore*, which   provides shared storage for the cluster.   When a failure occurs that affects a protected virtual machine,   HA will restart the virtual machine on another host.   When HA detects a host failure, either the host has failed or it may be   isolated from the network. The HA agent on an isolated host will power off   or shutdown the virtual machines running on that host so that they   can be restarted elsewhere.   See *ClusterDasVmSettingsIsolationResponse_enum* for information   about how a host handles network isolation.      When it chooses a failover host, HA selects a host that is compatible   with the virtual machine and that can support resource allocation for   that virtual machine so that service level guarantees remain intact.   HA does not consider hosts that are in maintenance mode, standby mode,   or which are disconnected from the vCenter Server. When a host powers   on or becomes available again, HA is reenabled on that host,   so it becomes available for failover again.   VMware recommends that you configure hosts and virtual machines   so that all virtual machines can run on all hosts in the cluster.   This will maximize the chances of restarting a VM after a failure.      HA also restarts a virtual machine after a guest operating system failure.   In this case, the virtual machine health monitoring service detects   the guest failure, and HA restarts the virtual machine on the same host.   The service monitors heartbeats from the VmTools service and optionally   heartbeats that are generated by a third-party application monitor.   See *ClusterVmToolsMonitoringSettings* and   *ClusterDasConfigInfo*.*ClusterDasConfigInfo.vmMonitoring*.      To enable HA for a cluster, set the   *ClusterDasConfigInfo*.*ClusterDasConfigInfo.enabled*   property to <code>true</code> and the   *ClusterDasConfigInfo*.*ClusterDasConfigInfo.hostMonitoring*   property to *enabled*.   (The vSphere API uses the substring \"das\" in object, property,   and method names for HA.<sup>1</sup>) - DRS (Distributed Resource Scheduling) - provides automatic initial   virtual machine placement on any of the hosts in the cluster. DRS   also makes automatic resource relocation and optimization decisions   as hosts or virtual machines are added or removed from the cluster.   You can also configure DRS for manual control, so that it only makes   recommendations that you can review and carry out.      To enable DRS for a cluster, set the   *ClusterDrsConfigInfo*.*ClusterDrsConfigInfo.enabled*   property to <code>true</code>. - DPM (Distributed Power Management) - supports optimized power   consumption on the cluster. When virtual machines in a DRS   cluster require fewer resources, DPM consolidates workloads   onto fewer servers while maintaining quality of service guarantees   and powers off the rest to reduce power consumption.   When more resources are required, DPM brings the powered-down hosts online.      To enable DPM for a cluster, set the   *ClusterDpmConfigInfo*.*ClusterDpmConfigInfo.enabled*   property to <code>true</code>. - VSAN - aggregrates hosts' local disks to present a single   shared datastore to the cluster.      To enable VSAN for a cluster, set the   *VsanClusterConfigInfo.enabled* property to   <code>true</code> for *ClusterConfigSpecEx.vsanConfig*. - InfraUpdateHA (Infrastructure update HA) - supports automatic   migration of virtual machines to hosts with low risk of a   catastrophic failure. Similar to DRS, you can also configure   InfraUpdateHA for manual control to only makes recommendations that   you can review and carry out. The health state of the hosts are   propagated to HA to enable restarting of virtual machines in healthy   hosts as possible.      To enable InfraUpdateHA for a cluster, set the   *ClusterInfraUpdateHaConfigInfo*.*ClusterInfraUpdateHaConfigInfo.enabled* property to   <code>true</code>. - ProactiveDRS (Proactive Distributed Resources Scheduling) - supports   virtual machine load balancing decisions that take predicted   resource demand information into account.      To enable ProactiveDRS for a cluster, set the   *ClusterProactiveDrsConfigInfo*.*ClusterProactiveDrsConfigInfo.enabled* property to   <code>true</code>.    The HA, DRS, and DPM services are integrated with the FT (Fault Tolerance) and EVC (Enhanced vMotion Compatibility) services. Use the *VirtualMachine.CreateSecondaryVM_Task* method to establish fault tolerance for a virtual machine. Use the vSphere Client to configure EVC. The HA, DRS, DPM, FT, and EVC services interact under the following circumstances. - To determine initial placement of a virtual machine, DRS   checks to see if the HA admission control policy on a   potential host supports the addition of the powered on   virtual machine. With the default setting, DRS will not   power on more than four FT virtual machines per host.   You can use the configuration editor in the vSphere Client   to set the HA advanced option <code>das.maxFtVmsPerHost</code>   to the desired number or to zero to disable. - When a host fails, HA determines placement within   the cluster when it restarts the virtual machines.   If there is insufficient capacity, and DPM has put one or more   compatible hosts into standby, HA relies on DPM to bring more   capacity online. - To use FT in a cluster, the cluster must be HA-enabled. - You can disable HA in a cluster while there are FT virtual   machines registered on hosts in the cluster.   While HA is disabled, powered on FT virtual machines will continue   to run, but HA will not restart any virtual machines after a failure.   When HA is disabled, you cannot use the following FT operations:   - Turn on FT (*VirtualMachine.CreateSecondaryVM_Task*)   - Enable FT (*VirtualMachine.EnableSecondaryVM_Task*)   - Power on an FT virtual machine     (*VirtualMachine.PowerOnVM_Task*)   - Test failover and test secondary restart     (*VirtualMachine.TerminateFaultTolerantVM_Task*) - In a cluster using DRS and HA with admission control turned on   (*ClusterDasConfigInfo*.*ClusterDasConfigInfo.admissionControlEnabled*),   the vCenter Server might not migrate virtual machines from hosts   entering maintenance mode. This is because resources are reserved   to maintain the failover level. You must use vMotion to manually   migrate the virtual machines off the hosts.      When admission control is disabled, failover resource constraints   are not passed on to DRS and DPM. The constraints are not enforced.   - DRS determines virtual machine placement and status     (maintenance mode, standby mode) regardless of the impact     this might have on failover requirements.   - DPM powers off hosts (places them in standby mode)     even if doing so violates failover requirements.     If there is insufficient capacity when a failover     occurs, DPM will attempt to bring more capacity online     in order to correct the situation. - You must enable EVC in a cluster to enable DRS to manage FT primary   and secondary virtual machine pairs in the cluster.   For information about EVC clusters, see *EVCMode*.      If EVC is disabled, vCenter automatically creates overrides   to disable DRS for FT primary/secondary pairs in the cluster.   vCenter will still use DRS to place a secondary virtual machine   when it powers on.   Attempts to remove the overrides or to enable DRS operations   will fail. - EVC clusters support load balancing of powered on FT primary   and secondary virtual machines. DRS behavior   is governed by the overrides defined for the primary virtual   machine. The secondary inherits DRS behavior from its primary.   If you do not configure a DRS override for an FT virtual   machine, DRS uses the cluster default   (*ClusterDrsConfigInfo.defaultVmBehavior*).    <sup>1</sup>High Availability was previously called Distributed Availability Services.  ***Since:*** VI API 2.5 
    """ # noqa: E501
    system_vms_config: Optional[ClusterSystemVMsConfigSpec] = Field(default=None, alias="systemVMsConfig")
    das_config: Optional[ClusterDasConfigInfo] = Field(default=None, alias="dasConfig")
    das_vm_config_spec: Optional[List[ClusterDasVmConfigSpec]] = Field(default=None, description="HA configuration for individual virtual machines.  The entries in this array override the cluster default settings (*ClusterDasConfigInfo*.*ClusterDasConfigInfo.defaultVmSettings*). You cannot specify an HA override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever settings apply to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault *CannotChangeHaSettingsForFtSecondary*.  ***Since:*** VI API 2.5 ", alias="dasVmConfigSpec")
    drs_config: Optional[ClusterDrsConfigInfo] = Field(default=None, alias="drsConfig")
    drs_vm_config_spec: Optional[List[ClusterDrsVmConfigSpec]] = Field(default=None, description="DRS configuration for individual virtual machines.  The entries in this array override the cluster default settings (*ClusterDrsConfigInfo*.*ClusterDrsConfigInfo.defaultVmBehavior*). You cannot specify a DRS override for a secondary FT virtual machine. The secondary virtual machine will inherit whatever setting applies to its primary virtual machine. If you include an entry for a secondary, the reconfigure method will throw the fault *CannotChangeDrsBehaviorForFtSecondary*.  ***Since:*** VI API 2.5 ", alias="drsVmConfigSpec")
    rules_spec: Optional[List[ClusterRuleSpec]] = Field(default=None, description="Cluster affinity and anti-affinity rule configuration.  ***Since:*** VI API 2.5 ", alias="rulesSpec")
    orchestration: Optional[ClusterOrchestrationInfo] = None
    vm_orchestration_spec: Optional[List[ClusterVmOrchestrationSpec]] = Field(default=None, description="List of specific VM configurations that apply during cluster wide VM orchestration.  Each entry applies to one virtual machine, and overrides the cluster default settings.  ***Since:*** vSphere API 6.5 ", alias="vmOrchestrationSpec")
    dpm_config: Optional[ClusterDpmConfigInfo] = Field(default=None, alias="dpmConfig")
    dpm_host_config_spec: Optional[List[ClusterDpmHostConfigSpec]] = Field(default=None, description="DPM configuration for individual hosts.  The entries in this array override the cluster default settings (*ClusterDpmConfigInfo*.*ClusterDpmConfigInfo.defaultDpmBehavior*).  ***Since:*** VI API 2.5 ", alias="dpmHostConfigSpec")
    vsan_config: Optional[VsanClusterConfigInfo] = Field(default=None, alias="vsanConfig")
    vsan_host_config_spec: Optional[List[VsanHostConfigInfo]] = Field(default=None, description="VSAN configuration for individual hosts.  The entries in this array override the cluster default settings as specified in *VsanClusterConfigInfo*.  ***Since:*** vSphere API 5.5 ", alias="vsanHostConfigSpec")
    group_spec: Optional[List[ClusterGroupSpec]] = Field(default=None, description="Cluster-wide group configuration.  The array contains one or more group specification objects. A group specification object contains a virtual machine group (*ClusterVmGroup*) or a host group (*ClusterHostGroup*). Groups can be related; see *ClusterVmHostRuleInfo*.  ***Since:*** vSphere API 4.1 ", alias="groupSpec")
    infra_update_ha_config: Optional[ClusterInfraUpdateHaConfigInfo] = Field(default=None, alias="infraUpdateHaConfig")
    proactive_drs_config: Optional[ClusterProactiveDrsConfigInfo] = Field(default=None, alias="proactiveDrsConfig")
    in_hci_workflow: Optional[StrictBool] = Field(default=None, description="Flag to place the cluster in the HCI workflow during cluster creation.  This flag is specified only at the time of cluster creation. A cluster cannot be reconfigured to place it in the HCI workflow.  ***Since:*** vSphere API 6.7.1 ", alias="inHciWorkflow")
    crypto_config: Optional[ClusterCryptoConfigInfo] = Field(default=None, alias="cryptoConfig")
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
        """Create an instance of ClusterConfigSpecEx from a JSON string"""
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
        """Create an instance of ClusterConfigSpecEx from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_typeName": obj.get("_typeName")
        })
        return _obj


