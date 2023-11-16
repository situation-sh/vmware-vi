# ArrayOfHostIpRouteEntry

A boxed array of *HostIpRouteEntry*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostIpRouteEntry]**](HostIpRouteEntry.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_ip_route_entry import ArrayOfHostIpRouteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostIpRouteEntry from a JSON string
array_of_host_ip_route_entry_instance = ArrayOfHostIpRouteEntry.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostIpRouteEntry.to_json()

# convert the object into a dict
array_of_host_ip_route_entry_dict = array_of_host_ip_route_entry_instance.to_dict()
# create an instance of ArrayOfHostIpRouteEntry from a dict
array_of_host_ip_route_entry_form_dict = array_of_host_ip_route_entry.from_dict(array_of_host_ip_route_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


