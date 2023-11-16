# UpdateVmfsUnmapBandwidthRequestType

The parameters of *HostStorageSystem.UpdateVmfsUnmapBandwidth*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmfs_uuid** | **str** | The VMFS UUID.  | 
**unmap_bandwidth_spec** | [**VmfsUnmapBandwidthSpec**](VmfsUnmapBandwidthSpec.md) |  | 

## Example

```python
from vmware_vi.models.update_vmfs_unmap_bandwidth_request_type import UpdateVmfsUnmapBandwidthRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVmfsUnmapBandwidthRequestType from a JSON string
update_vmfs_unmap_bandwidth_request_type_instance = UpdateVmfsUnmapBandwidthRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateVmfsUnmapBandwidthRequestType.to_json()

# convert the object into a dict
update_vmfs_unmap_bandwidth_request_type_dict = update_vmfs_unmap_bandwidth_request_type_instance.to_dict()
# create an instance of UpdateVmfsUnmapBandwidthRequestType from a dict
update_vmfs_unmap_bandwidth_request_type_form_dict = update_vmfs_unmap_bandwidth_request_type.from_dict(update_vmfs_unmap_bandwidth_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


