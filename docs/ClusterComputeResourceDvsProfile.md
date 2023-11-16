# ClusterComputeResourceDvsProfile

Describes DVS related information to be configured by calling *ClusterComputeResource.ConfigureHCI_Task* method.  Consists of name of the DVS, the physical adapters to be attached to it and the list of dvportgroups to be created on this DVS.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_name** | **str** | Name of the new *DistributedVirtualSwitch*.  ***Since:*** vSphere API 6.7.1  | [optional] 
**dv_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pnic_devices** | **List[str]** | List of physical Nics to be attached to the DVS.  ***Since:*** vSphere API 6.7.1  | [optional] 
**dv_portgroup_mapping** | [**List[ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping]**](ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_dvs_profile import ClusterComputeResourceDvsProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceDvsProfile from a JSON string
cluster_compute_resource_dvs_profile_instance = ClusterComputeResourceDvsProfile.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceDvsProfile.to_json()

# convert the object into a dict
cluster_compute_resource_dvs_profile_dict = cluster_compute_resource_dvs_profile_instance.to_dict()
# create an instance of ClusterComputeResourceDvsProfile from a dict
cluster_compute_resource_dvs_profile_form_dict = cluster_compute_resource_dvs_profile.from_dict(cluster_compute_resource_dvs_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


