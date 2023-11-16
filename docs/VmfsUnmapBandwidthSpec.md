# VmfsUnmapBandwidthSpec

VMFS unmap reclaims unused storage space.  This data object type describes the specification of VMFS unmap bandwidth.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | **str** | This property determines the unmap bandwidth policy.  See *HostVmfsVolumeUnmapBandwidthPolicy_enum* for supported values. If not specified, the default value is *fixed*, which means unmap is processed at a fixed rate.  ***Since:*** vSphere API 6.7  | 
**fixed_value** | **int** | This property determines the bandwidth under the fixed policy.  ***Since:*** vSphere API 6.7  | 
**dynamic_min** | **int** | This property determines the lower limits of the unmap bandwidth under the dynamic policy.  ***Since:*** vSphere API 6.7  | 
**dynamic_max** | **int** | This property determines the upper limits of the unmap bandwidth under the dynamic policy.  ***Since:*** vSphere API 6.7  | 

## Example

```python
from vmware_vi.models.vmfs_unmap_bandwidth_spec import VmfsUnmapBandwidthSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmfsUnmapBandwidthSpec from a JSON string
vmfs_unmap_bandwidth_spec_instance = VmfsUnmapBandwidthSpec.from_json(json)
# print the JSON string representation of the object
print VmfsUnmapBandwidthSpec.to_json()

# convert the object into a dict
vmfs_unmap_bandwidth_spec_dict = vmfs_unmap_bandwidth_spec_instance.to_dict()
# create an instance of VmfsUnmapBandwidthSpec from a dict
vmfs_unmap_bandwidth_spec_form_dict = vmfs_unmap_bandwidth_spec.from_dict(vmfs_unmap_bandwidth_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


