# SuspendedRelocateNotSupported

Either the source host product or the destination host product does not support relocation of suspended VMs.  It must be supported on both, in order for the relocation to succeed. This fault is only applicable to suspended virtual machines. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.suspended_relocate_not_supported import SuspendedRelocateNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of SuspendedRelocateNotSupported from a JSON string
suspended_relocate_not_supported_instance = SuspendedRelocateNotSupported.from_json(json)
# print the JSON string representation of the object
print SuspendedRelocateNotSupported.to_json()

# convert the object into a dict
suspended_relocate_not_supported_dict = suspended_relocate_not_supported_instance.to_dict()
# create an instance of SuspendedRelocateNotSupported from a dict
suspended_relocate_not_supported_form_dict = suspended_relocate_not_supported.from_dict(suspended_relocate_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


