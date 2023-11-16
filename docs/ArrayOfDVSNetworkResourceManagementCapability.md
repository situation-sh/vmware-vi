# ArrayOfDVSNetworkResourceManagementCapability

A boxed array of *DVSNetworkResourceManagementCapability*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSNetworkResourceManagementCapability]**](DVSNetworkResourceManagementCapability.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_network_resource_management_capability import ArrayOfDVSNetworkResourceManagementCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSNetworkResourceManagementCapability from a JSON string
array_of_dvs_network_resource_management_capability_instance = ArrayOfDVSNetworkResourceManagementCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSNetworkResourceManagementCapability.to_json()

# convert the object into a dict
array_of_dvs_network_resource_management_capability_dict = array_of_dvs_network_resource_management_capability_instance.to_dict()
# create an instance of ArrayOfDVSNetworkResourceManagementCapability from a dict
array_of_dvs_network_resource_management_capability_form_dict = array_of_dvs_network_resource_management_capability.from_dict(array_of_dvs_network_resource_management_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


