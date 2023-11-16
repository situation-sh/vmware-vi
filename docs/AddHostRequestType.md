# AddHostRequestType

The parameters of *ClusterComputeResource.AddHost_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | 
**as_connected** | **bool** | Flag to specify whether or not the host should be connected immediately after it is added. The host will not be added if a connection attempt is made and fails.  | 
**resource_pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**license** | **str** | Provide a licenseKey or licenseKeyType. See *LicenseManager*  | [optional] 

## Example

```python
from vmware_vi.models.add_host_request_type import AddHostRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddHostRequestType from a JSON string
add_host_request_type_instance = AddHostRequestType.from_json(json)
# print the JSON string representation of the object
print AddHostRequestType.to_json()

# convert the object into a dict
add_host_request_type_dict = add_host_request_type_instance.to_dict()
# create an instance of AddHostRequestType from a dict
add_host_request_type_form_dict = add_host_request_type.from_dict(add_host_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


