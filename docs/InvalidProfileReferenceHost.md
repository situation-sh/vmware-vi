# InvalidProfileReferenceHost

A InvalidProfileReferenceHost fault is thrown when a valid host is not associated with a profile in the Virtual Center inventory.  This could be because there is no host assciated with the profile or because the associated host is incompatible with the profile.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the invalid reference host if known.  ***Since:*** vSphere API 5.0  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**profile** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**profile_name** | **str** | The profile name: the replacement of the member above.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.invalid_profile_reference_host import InvalidProfileReferenceHost

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidProfileReferenceHost from a JSON string
invalid_profile_reference_host_instance = InvalidProfileReferenceHost.from_json(json)
# print the JSON string representation of the object
print InvalidProfileReferenceHost.to_json()

# convert the object into a dict
invalid_profile_reference_host_dict = invalid_profile_reference_host_instance.to_dict()
# create an instance of InvalidProfileReferenceHost from a dict
invalid_profile_reference_host_form_dict = invalid_profile_reference_host.from_dict(invalid_profile_reference_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


