# IpAddress

This is the abstract base class for IP address.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ip_address import IpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddress from a JSON string
ip_address_instance = IpAddress.from_json(json)
# print the JSON string representation of the object
print IpAddress.to_json()

# convert the object into a dict
ip_address_dict = ip_address_instance.to_dict()
# create an instance of IpAddress from a dict
ip_address_form_dict = ip_address.from_dict(ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


