# ArrayOfIpAddress

A boxed array of *IpAddress*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpAddress]**](IpAddress.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_address import ArrayOfIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpAddress from a JSON string
array_of_ip_address_instance = ArrayOfIpAddress.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpAddress.to_json()

# convert the object into a dict
array_of_ip_address_dict = array_of_ip_address_instance.to_dict()
# create an instance of ArrayOfIpAddress from a dict
array_of_ip_address_form_dict = array_of_ip_address.from_dict(array_of_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


