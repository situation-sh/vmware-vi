# ArrayOfHostPosixAccountSpec

A boxed array of *HostPosixAccountSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPosixAccountSpec]**](HostPosixAccountSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_posix_account_spec import ArrayOfHostPosixAccountSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPosixAccountSpec from a JSON string
array_of_host_posix_account_spec_instance = ArrayOfHostPosixAccountSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPosixAccountSpec.to_json()

# convert the object into a dict
array_of_host_posix_account_spec_dict = array_of_host_posix_account_spec_instance.to_dict()
# create an instance of ArrayOfHostPosixAccountSpec from a dict
array_of_host_posix_account_spec_form_dict = array_of_host_posix_account_spec.from_dict(array_of_host_posix_account_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


