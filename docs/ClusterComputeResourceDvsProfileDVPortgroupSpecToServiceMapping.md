# ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dv_portgroup_spec** | [**DVPortgroupConfigSpec**](DVPortgroupConfigSpec.md) |  | [optional] 
**dv_portgroup** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**service** | **str** | Service to be configured on the virtual nics attached to this dvportgroup.  See *HostVirtualNicManagerNicType_enum* for supported values.  ***Since:*** vSphere API 6.7.1  | 

## Example

```python
from vmware_vi.models.cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping import ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping from a JSON string
cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping_instance = ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping.to_json()

# convert the object into a dict
cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping_dict = cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping_instance.to_dict()
# create an instance of ClusterComputeResourceDvsProfileDVPortgroupSpecToServiceMapping from a dict
cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping_form_dict = cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping.from_dict(cluster_compute_resource_dvs_profile_dv_portgroup_spec_to_service_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


