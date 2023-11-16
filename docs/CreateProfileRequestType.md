# CreateProfileRequestType

The parameters of *ProfileManager.CreateProfile*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_spec** | [**ProfileCreateSpec**](ProfileCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_profile_request_type import CreateProfileRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileRequestType from a JSON string
create_profile_request_type_instance = CreateProfileRequestType.from_json(json)
# print the JSON string representation of the object
print CreateProfileRequestType.to_json()

# convert the object into a dict
create_profile_request_type_dict = create_profile_request_type_instance.to_dict()
# create an instance of CreateProfileRequestType from a dict
create_profile_request_type_form_dict = create_profile_request_type.from_dict(create_profile_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


