# UpdateNetworkConfigRequestType

The parameters of *HostNetworkSystem.UpdateNetworkConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostNetworkConfig**](HostNetworkConfig.md) |  | 
**change_mode** | **str** |  | 

## Example

```python
from vmware_vi.models.update_network_config_request_type import UpdateNetworkConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkConfigRequestType from a JSON string
update_network_config_request_type_instance = UpdateNetworkConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateNetworkConfigRequestType.to_json()

# convert the object into a dict
update_network_config_request_type_dict = update_network_config_request_type_instance.to_dict()
# create an instance of UpdateNetworkConfigRequestType from a dict
update_network_config_request_type_form_dict = update_network_config_request_type.from_dict(update_network_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


