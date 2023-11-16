# VirtualEnsoniq1371

The VirtualEnsoniq1371 data object type represents an Ensoniq 1371 sound card in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ensoniq1371 import VirtualEnsoniq1371

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualEnsoniq1371 from a JSON string
virtual_ensoniq1371_instance = VirtualEnsoniq1371.from_json(json)
# print the JSON string representation of the object
print VirtualEnsoniq1371.to_json()

# convert the object into a dict
virtual_ensoniq1371_dict = virtual_ensoniq1371_instance.to_dict()
# create an instance of VirtualEnsoniq1371 from a dict
virtual_ensoniq1371_form_dict = virtual_ensoniq1371.from_dict(virtual_ensoniq1371_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


