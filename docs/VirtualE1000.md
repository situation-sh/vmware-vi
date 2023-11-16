# VirtualE1000

The VirtualE1000 data object type represents an instance of the E1000 virtual Ethernet adapter attached to a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_e1000 import VirtualE1000

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualE1000 from a JSON string
virtual_e1000_instance = VirtualE1000.from_json(json)
# print the JSON string representation of the object
print VirtualE1000.to_json()

# convert the object into a dict
virtual_e1000_dict = virtual_e1000_instance.to_dict()
# create an instance of VirtualE1000 from a dict
virtual_e1000_form_dict = virtual_e1000.from_dict(virtual_e1000_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


