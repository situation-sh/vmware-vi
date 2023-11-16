# ArrayOfHostProfileSerializedHostProfileSpec

A boxed array of *HostProfileSerializedHostProfileSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProfileSerializedHostProfileSpec]**](HostProfileSerializedHostProfileSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_profile_serialized_host_profile_spec import ArrayOfHostProfileSerializedHostProfileSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProfileSerializedHostProfileSpec from a JSON string
array_of_host_profile_serialized_host_profile_spec_instance = ArrayOfHostProfileSerializedHostProfileSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProfileSerializedHostProfileSpec.to_json()

# convert the object into a dict
array_of_host_profile_serialized_host_profile_spec_dict = array_of_host_profile_serialized_host_profile_spec_instance.to_dict()
# create an instance of ArrayOfHostProfileSerializedHostProfileSpec from a dict
array_of_host_profile_serialized_host_profile_spec_form_dict = array_of_host_profile_serialized_host_profile_spec.from_dict(array_of_host_profile_serialized_host_profile_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


