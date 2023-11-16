# MemoryHotPlugNotSupported

Thrown when memory cannot be hot-added or hot-removed from the virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.memory_hot_plug_not_supported import MemoryHotPlugNotSupported

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryHotPlugNotSupported from a JSON string
memory_hot_plug_not_supported_instance = MemoryHotPlugNotSupported.from_json(json)
# print the JSON string representation of the object
print MemoryHotPlugNotSupported.to_json()

# convert the object into a dict
memory_hot_plug_not_supported_dict = memory_hot_plug_not_supported_instance.to_dict()
# create an instance of MemoryHotPlugNotSupported from a dict
memory_hot_plug_not_supported_form_dict = memory_hot_plug_not_supported.from_dict(memory_hot_plug_not_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


