# VirtualE1000e

The VirtualE1000e data object type represents an instance of the E1000e virtual Ethernet adapter attached to a virtual machine.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_e1000e import VirtualE1000e

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualE1000e from a JSON string
virtual_e1000e_instance = VirtualE1000e.from_json(json)
# print the JSON string representation of the object
print VirtualE1000e.to_json()

# convert the object into a dict
virtual_e1000e_dict = virtual_e1000e_instance.to_dict()
# create an instance of VirtualE1000e from a dict
virtual_e1000e_form_dict = virtual_e1000e.from_dict(virtual_e1000e_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


