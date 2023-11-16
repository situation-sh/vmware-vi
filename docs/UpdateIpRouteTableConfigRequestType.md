# UpdateIpRouteTableConfigRequestType

The parameters of *HostNetworkSystem.UpdateIpRouteTableConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**HostIpRouteTableConfig**](HostIpRouteTableConfig.md) |  | 

## Example

```python
from vmware_vi.models.update_ip_route_table_config_request_type import UpdateIpRouteTableConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIpRouteTableConfigRequestType from a JSON string
update_ip_route_table_config_request_type_instance = UpdateIpRouteTableConfigRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateIpRouteTableConfigRequestType.to_json()

# convert the object into a dict
update_ip_route_table_config_request_type_dict = update_ip_route_table_config_request_type_instance.to_dict()
# create an instance of UpdateIpRouteTableConfigRequestType from a dict
update_ip_route_table_config_request_type_form_dict = update_ip_route_table_config_request_type.from_dict(update_ip_route_table_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


