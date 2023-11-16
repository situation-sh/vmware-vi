# VirtualE1000eOption

The VirtualE1000e option data object type contains the options for the *VirtualE1000e* data object type.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_e1000e_option import VirtualE1000eOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualE1000eOption from a JSON string
virtual_e1000e_option_instance = VirtualE1000eOption.from_json(json)
# print the JSON string representation of the object
print VirtualE1000eOption.to_json()

# convert the object into a dict
virtual_e1000e_option_dict = virtual_e1000e_option_instance.to_dict()
# create an instance of VirtualE1000eOption from a dict
virtual_e1000e_option_form_dict = virtual_e1000e_option.from_dict(virtual_e1000e_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


