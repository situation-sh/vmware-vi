# ProfileSerializedCreateSpec

The *ProfileSerializedCreateSpec* data object defines a string that contains a serialized representation of a host profile.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_config_string** | **str** | Representation of the profile in the string form.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.profile_serialized_create_spec import ProfileSerializedCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileSerializedCreateSpec from a JSON string
profile_serialized_create_spec_instance = ProfileSerializedCreateSpec.from_json(json)
# print the JSON string representation of the object
print ProfileSerializedCreateSpec.to_json()

# convert the object into a dict
profile_serialized_create_spec_dict = profile_serialized_create_spec_instance.to_dict()
# create an instance of ProfileSerializedCreateSpec from a dict
profile_serialized_create_spec_form_dict = profile_serialized_create_spec.from_dict(profile_serialized_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


