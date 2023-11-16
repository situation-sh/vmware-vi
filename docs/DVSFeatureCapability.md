# DVSFeatureCapability

The *DVSFeatureCapability* data object represents the capabilities supported by a *DistributedVirtualSwitch*.  These properties are read-only with the exception of *DVSFeatureCapability.vmDirectPathGen2Supported*.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_resource_management_supported** | **bool** | Deprecated as of vSphere API 5.0, use &lt;code&gt;networkResourceManagementCapability&lt;/code&gt;.*DVSNetworkResourceManagementCapability.networkResourceManagementSupported*.  Indicates whether network I/O control is supported on the vSphere Distributed Switch.  ***Since:*** vSphere API 4.1  | 
**vm_direct_path_gen2_supported** | **bool** | Deprecated as of vSphere API 8.0. VMDirectPath Gen 2 is no longer supported and there is no replacement.  Indicates whether VMDirectPath Gen 2 is supported on the distributed virtual switch.  See *HostCapability*.*HostCapability.vmDirectPathGen2Supported* and *PhysicalNic*.*PhysicalNic.vmDirectPathGen2Supported*.  For a third-party distributed switch implementation, you can specify this property during switch creation or when you call the *DistributedVirtualSwitch.UpdateDvsCapability* method.  VMDirectPath Gen 2 is supported in vSphere Distributed Switch Version 4.1 or later.  ***Since:*** vSphere API 4.1  | [optional] 
**nic_teaming_policy** | **List[str]** | The available teaming modes for the vSphere Distributed Switch.  The value can be one or more of *DistributedVirtualSwitchNicTeamingPolicyMode_enum*.  ***Since:*** vSphere API 4.1  | [optional] 
**network_resource_pool_high_share_value** | **int** | Deprecated as of vSphere API 5.0, use &lt;code&gt;networkResourceManagementCapability&lt;/code&gt;.*DVSNetworkResourceManagementCapability.networkResourcePoolHighShareValue*.  This is the value for *high* in *DVSNetworkResourcePoolAllocationInfo.shares*.  This implicitly defines the legal range of share values to be between 1 and this. This also defines values for other level types, such as *normal* being one half of this value and *low* being one fourth of this value.  ***Since:*** vSphere API 4.1  | [optional] 
**network_resource_management_capability** | [**DVSNetworkResourceManagementCapability**](DVSNetworkResourceManagementCapability.md) |  | [optional] 
**health_check_capability** | [**DVSHealthCheckCapability**](DVSHealthCheckCapability.md) |  | [optional] 
**rollback_capability** | [**DVSRollbackCapability**](DVSRollbackCapability.md) |  | [optional] 
**backup_restore_capability** | [**DVSBackupRestoreCapability**](DVSBackupRestoreCapability.md) |  | [optional] 
**network_filter_supported** | **bool** | Indicates whether Network Filter feature is supported in vSphere Distributed Switch.  ***Since:*** vSphere API 5.5  | [optional] 
**mac_learning_supported** | **bool** | Indicates whether MAC learning feature is supported in vSphere Distributed Switch.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.dvs_feature_capability import DVSFeatureCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSFeatureCapability from a JSON string
dvs_feature_capability_instance = DVSFeatureCapability.from_json(json)
# print the JSON string representation of the object
print DVSFeatureCapability.to_json()

# convert the object into a dict
dvs_feature_capability_dict = dvs_feature_capability_instance.to_dict()
# create an instance of DVSFeatureCapability from a dict
dvs_feature_capability_form_dict = dvs_feature_capability.from_dict(dvs_feature_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


