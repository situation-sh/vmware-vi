# ArrayOfHostConnectSpec

A boxed array of *HostConnectSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostConnectSpec]**](HostConnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_connect_spec import ArrayOfHostConnectSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostConnectSpec from a JSON string
array_of_host_connect_spec_instance = ArrayOfHostConnectSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostConnectSpec.to_json()

# convert the object into a dict
array_of_host_connect_spec_dict = array_of_host_connect_spec_instance.to_dict()
# create an instance of ArrayOfHostConnectSpec from a dict
array_of_host_connect_spec_form_dict = array_of_host_connect_spec.from_dict(array_of_host_connect_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


