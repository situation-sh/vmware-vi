# VsanClusterUuidMismatch

Fault thrown for the case that an attempt is made to move a host which is enabled for VSAN into a *ClusterComputeResource* whose VSAN cluster UUID does not match.  See also *CannotMoveVsanEnabledHost*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_cluster_uuid** | **str** | The VSAN cluster UUID in use by the host at hand.  ***Since:*** vSphere API 5.5  | 
**destination_cluster_uuid** | **str** | The VSAN cluster UUID in use by the destination *ClusterComputeResource*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_cluster_uuid_mismatch import VsanClusterUuidMismatch

# TODO update the JSON string below
json = "{}"
# create an instance of VsanClusterUuidMismatch from a JSON string
vsan_cluster_uuid_mismatch_instance = VsanClusterUuidMismatch.from_json(json)
# print the JSON string representation of the object
print VsanClusterUuidMismatch.to_json()

# convert the object into a dict
vsan_cluster_uuid_mismatch_dict = vsan_cluster_uuid_mismatch_instance.to_dict()
# create an instance of VsanClusterUuidMismatch from a dict
vsan_cluster_uuid_mismatch_form_dict = vsan_cluster_uuid_mismatch.from_dict(vsan_cluster_uuid_mismatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


