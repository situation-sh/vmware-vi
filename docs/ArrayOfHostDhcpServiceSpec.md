# ArrayOfHostDhcpServiceSpec

A boxed array of *HostDhcpServiceSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDhcpServiceSpec]**](HostDhcpServiceSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_dhcp_service_spec import ArrayOfHostDhcpServiceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDhcpServiceSpec from a JSON string
array_of_host_dhcp_service_spec_instance = ArrayOfHostDhcpServiceSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDhcpServiceSpec.to_json()

# convert the object into a dict
array_of_host_dhcp_service_spec_dict = array_of_host_dhcp_service_spec_instance.to_dict()
# create an instance of ArrayOfHostDhcpServiceSpec from a dict
array_of_host_dhcp_service_spec_form_dict = array_of_host_dhcp_service_spec.from_dict(array_of_host_dhcp_service_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


