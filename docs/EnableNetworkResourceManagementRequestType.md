# EnableNetworkResourceManagementRequestType

The parameters of *DistributedVirtualSwitch.EnableNetworkResourceManagement*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | If true, enables I/O control. If false, disables network I/O control.  | 

## Example

```python
from vmware_vi.models.enable_network_resource_management_request_type import EnableNetworkResourceManagementRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableNetworkResourceManagementRequestType from a JSON string
enable_network_resource_management_request_type_instance = EnableNetworkResourceManagementRequestType.from_json(json)
# print the JSON string representation of the object
print EnableNetworkResourceManagementRequestType.to_json()

# convert the object into a dict
enable_network_resource_management_request_type_dict = enable_network_resource_management_request_type_instance.to_dict()
# create an instance of EnableNetworkResourceManagementRequestType from a dict
enable_network_resource_management_request_type_form_dict = enable_network_resource_management_request_type.from_dict(enable_network_resource_management_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


