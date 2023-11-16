# UpdateDnsConfigRequestType

The parameters of *HostNetworkSystem.UpdateDnsConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostDnsConfig**](HostDnsConfig.md) |  | 

## Example

```python
from vmware_vi.models.update_dns_config_request_type import UpdateDnsConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDnsConfigRequestType from a JSON string
update_dns_config_request_type_instance = UpdateDnsConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateDnsConfigRequestType.to_json()

# convert the object into a dict
update_dns_config_request_type_dict = update_dns_config_request_type_instance.to_dict()
# create an instance of UpdateDnsConfigRequestType from a dict
update_dns_config_request_type_form_dict = update_dns_config_request_type.from_dict(update_dns_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


