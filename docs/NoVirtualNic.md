# NoVirtualNic

This error occurs when an operation fails because of no virtual NIC available. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.no_virtual_nic import NoVirtualNic

# TODO update the JSON string below
json = "{}"
# create an instance of NoVirtualNic from a JSON string
no_virtual_nic_instance = NoVirtualNic.from_json(json)
# print the JSON string representation of the object
print NoVirtualNic.to_json()

# convert the object into a dict
no_virtual_nic_dict = no_virtual_nic_instance.to_dict()
# create an instance of NoVirtualNic from a dict
no_virtual_nic_form_dict = no_virtual_nic.from_dict(no_virtual_nic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


