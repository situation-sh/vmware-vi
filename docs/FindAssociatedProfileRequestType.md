# FindAssociatedProfileRequestType

The parameters of *ProfileManager.FindAssociatedProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.find_associated_profile_request_type import FindAssociatedProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindAssociatedProfileRequestType from a JSON string
find_associated_profile_request_type_instance = FindAssociatedProfileRequestType.from_json(json)
# print the JSON string representation of the object
print FindAssociatedProfileRequestType.to_json()

# convert the object into a dict
find_associated_profile_request_type_dict = find_associated_profile_request_type_instance.to_dict()
# create an instance of FindAssociatedProfileRequestType from a dict
find_associated_profile_request_type_form_dict = find_associated_profile_request_type.from_dict(find_associated_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


