# VirtualE1000Option

The VirtualE1000 option data object type contains the options for the *VirtualE1000* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_e1000_option import VirtualE1000Option

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualE1000Option from a JSON string
virtual_e1000_option_instance = VirtualE1000Option.from_json(json)
# print the JSON string representation of the object
print VirtualE1000Option.to_json()

# convert the object into a dict
virtual_e1000_option_dict = virtual_e1000_option_instance.to_dict()
# create an instance of VirtualE1000Option from a dict
virtual_e1000_option_form_dict = virtual_e1000_option.from_dict(virtual_e1000_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


