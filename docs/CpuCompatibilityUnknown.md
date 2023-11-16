# CpuCompatibilityUnknown

Deprecated as of VI API 2.5, use *CpuIncompatible* and its other subclasses, not this one.  Compatibility between the virtual machine's host and its CPU feature requirements cannot be determined, because not enough information is available about the CPU features of the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cpu_compatibility_unknown import CpuCompatibilityUnknown

# TODO update the JSON string below
json = "{}"
# create an instance of CpuCompatibilityUnknown from a JSON string
cpu_compatibility_unknown_instance = CpuCompatibilityUnknown.from_json(json)
# print the JSON string representation of the object
print CpuCompatibilityUnknown.to_json()

# convert the object into a dict
cpu_compatibility_unknown_dict = cpu_compatibility_unknown_instance.to_dict()
# create an instance of CpuCompatibilityUnknown from a dict
cpu_compatibility_unknown_form_dict = cpu_compatibility_unknown.from_dict(cpu_compatibility_unknown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


