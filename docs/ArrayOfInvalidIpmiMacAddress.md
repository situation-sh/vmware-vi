# ArrayOfInvalidIpmiMacAddress

A boxed array of *InvalidIpmiMacAddress*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidIpmiMacAddress]**](InvalidIpmiMacAddress.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_ipmi_mac_address import ArrayOfInvalidIpmiMacAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidIpmiMacAddress from a JSON string
array_of_invalid_ipmi_mac_address_instance = ArrayOfInvalidIpmiMacAddress.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidIpmiMacAddress.to_json()

# convert the object into a dict
array_of_invalid_ipmi_mac_address_dict = array_of_invalid_ipmi_mac_address_instance.to_dict()
# create an instance of ArrayOfInvalidIpmiMacAddress from a dict
array_of_invalid_ipmi_mac_address_form_dict = array_of_invalid_ipmi_mac_address.from_dict(array_of_invalid_ipmi_mac_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


