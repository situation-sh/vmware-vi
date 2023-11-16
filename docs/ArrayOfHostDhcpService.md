# ArrayOfHostDhcpService

A boxed array of *HostDhcpService*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDhcpService]**](HostDhcpService.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_dhcp_service import ArrayOfHostDhcpService

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDhcpService from a JSON string
array_of_host_dhcp_service_instance = ArrayOfHostDhcpService.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDhcpService.to_json()

# convert the object into a dict
array_of_host_dhcp_service_dict = array_of_host_dhcp_service_instance.to_dict()
# create an instance of ArrayOfHostDhcpService from a dict
array_of_host_dhcp_service_form_dict = array_of_host_dhcp_service.from_dict(array_of_host_dhcp_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


