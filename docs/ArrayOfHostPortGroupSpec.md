# ArrayOfHostPortGroupSpec

A boxed array of *HostPortGroupSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPortGroupSpec]**](HostPortGroupSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_port_group_spec import ArrayOfHostPortGroupSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPortGroupSpec from a JSON string
array_of_host_port_group_spec_instance = ArrayOfHostPortGroupSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPortGroupSpec.to_json()

# convert the object into a dict
array_of_host_port_group_spec_dict = array_of_host_port_group_spec_instance.to_dict()
# create an instance of ArrayOfHostPortGroupSpec from a dict
array_of_host_port_group_spec_form_dict = array_of_host_port_group_spec.from_dict(array_of_host_port_group_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


