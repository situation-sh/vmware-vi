# ArrayOfIpAddressProfile

A boxed array of *IpAddressProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpAddressProfile]**](IpAddressProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_address_profile import ArrayOfIpAddressProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpAddressProfile from a JSON string
array_of_ip_address_profile_instance = ArrayOfIpAddressProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpAddressProfile.to_json()

# convert the object into a dict
array_of_ip_address_profile_dict = array_of_ip_address_profile_instance.to_dict()
# create an instance of ArrayOfIpAddressProfile from a dict
array_of_ip_address_profile_form_dict = array_of_ip_address_profile.from_dict(array_of_ip_address_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


