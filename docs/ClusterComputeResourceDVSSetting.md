# ClusterComputeResourceDVSSetting

Contains reference to the DVS, list of physical nics attached to it, and list of dvportgroups created on it while initially configuring a cluster by calling the *ClusterComputeResource.ConfigureHCI_Task* method.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dv_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**pnic_devices** | **List[str]** | List of physical nics attached to the DVS.  ***Since:*** vSphere API 6.7.1  | [optional] 
**dv_portgroup_setting** | [**List[ClusterComputeResourceDVSSettingDVPortgroupToServiceMapping]**](ClusterComputeResourceDVSSettingDVPortgroupToServiceMapping.md) | Describes dvportgroups on the DVS and services residing on each one.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_dvs_setting import ClusterComputeResourceDVSSetting

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceDVSSetting from a JSON string
cluster_compute_resource_dvs_setting_instance = ClusterComputeResourceDVSSetting.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceDVSSetting.to_json()

# convert the object into a dict
cluster_compute_resource_dvs_setting_dict = cluster_compute_resource_dvs_setting_instance.to_dict()
# create an instance of ClusterComputeResourceDVSSetting from a dict
cluster_compute_resource_dvs_setting_form_dict = cluster_compute_resource_dvs_setting.from_dict(cluster_compute_resource_dvs_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


