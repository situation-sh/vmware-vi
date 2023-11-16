# ArrayOfHostIpRouteTableInfo

A boxed array of *HostIpRouteTableInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpRouteTableInfo]**](HostIpRouteTableInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_route_table_info import ArrayOfHostIpRouteTableInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpRouteTableInfo from a JSON string
array_of_host_ip_route_table_info_instance = ArrayOfHostIpRouteTableInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpRouteTableInfo.to_json()

# convert the object into a dict
array_of_host_ip_route_table_info_dict = array_of_host_ip_route_table_info_instance.to_dict()
# create an instance of ArrayOfHostIpRouteTableInfo from a dict
array_of_host_ip_route_table_info_form_dict = array_of_host_ip_route_table_info.from_dict(array_of_host_ip_route_table_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


