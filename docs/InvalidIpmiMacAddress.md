# InvalidIpmiMacAddress

A InvalidIpmiMacAddress fault is thrown when the IPMI mac address provided by the user doesn't match with the observed mac address on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_provided_mac_address** | **str** |  | 
**observed_mac_address** | **str** |  | 

## Example

```python
from vmware_vi.models.invalid_ipmi_mac_address import InvalidIpmiMacAddress

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidIpmiMacAddress from a JSON string
invalid_ipmi_mac_address_instance = InvalidIpmiMacAddress.from_json(json)
# print the JSON string representation of the object
print InvalidIpmiMacAddress.to_json()

# convert the object into a dict
invalid_ipmi_mac_address_dict = invalid_ipmi_mac_address_instance.to_dict()
# create an instance of InvalidIpmiMacAddress from a dict
invalid_ipmi_mac_address_form_dict = invalid_ipmi_mac_address.from_dict(invalid_ipmi_mac_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


