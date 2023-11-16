# ArrayOfNetIpConfigInfo

A boxed array of *NetIpConfigInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetIpConfigInfo]**](NetIpConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_net_ip_config_info import ArrayOfNetIpConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetIpConfigInfo from a JSON string
array_of_net_ip_config_info_instance = ArrayOfNetIpConfigInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetIpConfigInfo.to_json()

# convert the object into a dict
array_of_net_ip_config_info_dict = array_of_net_ip_config_info_instance.to_dict()
# create an instance of ArrayOfNetIpConfigInfo from a dict
array_of_net_ip_config_info_form_dict = array_of_net_ip_config_info.from_dict(array_of_net_ip_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


