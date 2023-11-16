# IpAddressProfile

The *IpAddressProfile* represents the Virtual NIC IP address.  The *ApplyProfile.policy* property contains the configuration data values for the IP address.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ip_address_profile import IpAddressProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressProfile from a JSON string
ip_address_profile_instance = IpAddressProfile.from_json(json)
# print the JSON string representation of the object
print IpAddressProfile.to_json()

# convert the object into a dict
ip_address_profile_dict = ip_address_profile_instance.to_dict()
# create an instance of IpAddressProfile from a dict
ip_address_profile_form_dict = ip_address_profile.from_dict(ip_address_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


