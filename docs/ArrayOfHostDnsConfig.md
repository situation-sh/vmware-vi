# ArrayOfHostDnsConfig

A boxed array of *HostDnsConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDnsConfig]**](HostDnsConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_dns_config import ArrayOfHostDnsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDnsConfig from a JSON string
array_of_host_dns_config_instance = ArrayOfHostDnsConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDnsConfig.to_json()

# convert the object into a dict
array_of_host_dns_config_dict = array_of_host_dns_config_instance.to_dict()
# create an instance of ArrayOfHostDnsConfig from a dict
array_of_host_dns_config_form_dict = array_of_host_dns_config.from_dict(array_of_host_dns_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


