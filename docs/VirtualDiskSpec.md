# VirtualDiskSpec

Specification used to create or clone a virtual disk  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_type** | **str** | The type of the new virtual disk.  See also *VirtualDiskType_enum*.  ***Since:*** VI API 2.5  | 
**adapter_type** | **str** | The type of the virtual disk adapter for the new virtual disk.  See also *VirtualDiskAdapterType_enum*.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.virtual_disk_spec import VirtualDiskSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskSpec from a JSON string
virtual_disk_spec_instance = VirtualDiskSpec.from_json(json)
# print the JSON string representation of the object
print VirtualDiskSpec.to_json()

# convert the object into a dict
virtual_disk_spec_dict = virtual_disk_spec_instance.to_dict()
# create an instance of VirtualDiskSpec from a dict
virtual_disk_spec_form_dict = virtual_disk_spec.from_dict(virtual_disk_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


