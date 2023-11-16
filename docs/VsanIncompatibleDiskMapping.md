# VsanIncompatibleDiskMapping

Fault used for the add operation which will result in incompatible disk mappings.  See also *HostVsanSystem.InitializeDisks_Task*.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vsan_incompatible_disk_mapping import VsanIncompatibleDiskMapping

# TODO update the JSON string below
json = "{}"
# create an instance of VsanIncompatibleDiskMapping from a JSON string
vsan_incompatible_disk_mapping_instance = VsanIncompatibleDiskMapping.from_json(json)
# print the JSON string representation of the object
print VsanIncompatibleDiskMapping.to_json()

# convert the object into a dict
vsan_incompatible_disk_mapping_dict = vsan_incompatible_disk_mapping_instance.to_dict()
# create an instance of VsanIncompatibleDiskMapping from a dict
vsan_incompatible_disk_mapping_form_dict = vsan_incompatible_disk_mapping.from_dict(vsan_incompatible_disk_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


