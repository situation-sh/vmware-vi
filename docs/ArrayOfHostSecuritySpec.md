# ArrayOfHostSecuritySpec

A boxed array of *HostSecuritySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSecuritySpec]**](HostSecuritySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_security_spec import ArrayOfHostSecuritySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSecuritySpec from a JSON string
array_of_host_security_spec_instance = ArrayOfHostSecuritySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSecuritySpec.to_json()

# convert the object into a dict
array_of_host_security_spec_dict = array_of_host_security_spec_instance.to_dict()
# create an instance of ArrayOfHostSecuritySpec from a dict
array_of_host_security_spec_form_dict = array_of_host_security_spec.from_dict(array_of_host_security_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


