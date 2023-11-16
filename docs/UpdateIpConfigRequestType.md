# UpdateIpConfigRequestType

The parameters of *HostVMotionSystem.UpdateIpConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_config** | [**HostIpConfig**](HostIpConfig.md) |  | 

## Example

```python
from vmware_vi.models.update_ip_config_request_type import UpdateIpConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpConfigRequestType from a JSON string
update_ip_config_request_type_instance = UpdateIpConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateIpConfigRequestType.to_json()

# convert the object into a dict
update_ip_config_request_type_dict = update_ip_config_request_type_instance.to_dict()
# create an instance of UpdateIpConfigRequestType from a dict
update_ip_config_request_type_form_dict = update_ip_config_request_type.from_dict(update_ip_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


