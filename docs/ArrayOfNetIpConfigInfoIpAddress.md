# ArrayOfNetIpConfigInfoIpAddress

A boxed array of *NetIpConfigInfoIpAddress*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpConfigInfoIpAddress]**](NetIpConfigInfoIpAddress.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_config_info_ip_address import ArrayOfNetIpConfigInfoIpAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpConfigInfoIpAddress from a JSON string
array_of_net_ip_config_info_ip_address_instance = ArrayOfNetIpConfigInfoIpAddress.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpConfigInfoIpAddress.to_json()

# convert the object into a dict
array_of_net_ip_config_info_ip_address_dict = array_of_net_ip_config_info_ip_address_instance.to_dict()
# create an instance of ArrayOfNetIpConfigInfoIpAddress from a dict
array_of_net_ip_config_info_ip_address_form_dict = array_of_net_ip_config_info_ip_address.from_dict(array_of_net_ip_config_info_ip_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


