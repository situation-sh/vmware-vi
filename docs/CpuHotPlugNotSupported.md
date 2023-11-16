# CpuHotPlugNotSupported

Thrown when virtual CPUs cannot be hot-added or hot-removed from the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cpu_hot_plug_not_supported import CpuHotPlugNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of CpuHotPlugNotSupported from a JSON string
cpu_hot_plug_not_supported_instance = CpuHotPlugNotSupported.from_json(json)
# print the JSON string representation of the object
print CpuHotPlugNotSupported.to_json()

# convert the object into a dict
cpu_hot_plug_not_supported_dict = cpu_hot_plug_not_supported_instance.to_dict()
# create an instance of CpuHotPlugNotSupported from a dict
cpu_hot_plug_not_supported_form_dict = cpu_hot_plug_not_supported.from_dict(cpu_hot_plug_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


