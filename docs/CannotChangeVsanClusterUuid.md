# CannotChangeVsanClusterUuid

Fault thrown for cases that a VSAN cluster UUID may not be changed.  For example, the VSAN cluster UUID for a host may not be changed so long as that host is enabled for VSAN. The VSAN cluster UUID for a given *ClusterComputeResource* may not be changed so long as that vim.ClusterComputeResource is enabled for VSAN.  See also *HostVsanSystem.UpdateVsan_Task*, *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_change_vsan_cluster_uuid import CannotChangeVsanClusterUuid

# TODO update the JSON string below
json = "{}"
# create an instance of CannotChangeVsanClusterUuid from a JSON string
cannot_change_vsan_cluster_uuid_instance = CannotChangeVsanClusterUuid.from_json(json)
# print the JSON string representation of the object
print CannotChangeVsanClusterUuid.to_json()

# convert the object into a dict
cannot_change_vsan_cluster_uuid_dict = cannot_change_vsan_cluster_uuid_instance.to_dict()
# create an instance of CannotChangeVsanClusterUuid from a dict
cannot_change_vsan_cluster_uuid_form_dict = cannot_change_vsan_cluster_uuid.from_dict(cannot_change_vsan_cluster_uuid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


