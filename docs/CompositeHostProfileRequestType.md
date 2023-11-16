# CompositeHostProfileRequestType

The parameters of *HostProfileManager.CompositeHostProfile_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**targets** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) |  | [optional] 
**to_be_merged** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_replaced_with** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**to_be_deleted** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 
**enable_status_to_be_copied** | [**HostApplyProfile**](HostApplyProfile.md) |  | [optional] 

## Example

```python
from vmware_vi.models.composite_host_profile_request_type import CompositeHostProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CompositeHostProfileRequestType from a JSON string
composite_host_profile_request_type_instance = CompositeHostProfileRequestType.from_json(json)
# print the JSON string representation of the object
print CompositeHostProfileRequestType.to_json()

# convert the object into a dict
composite_host_profile_request_type_dict = composite_host_profile_request_type_instance.to_dict()
# create an instance of CompositeHostProfileRequestType from a dict
composite_host_profile_request_type_form_dict = composite_host_profile_request_type.from_dict(composite_host_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


