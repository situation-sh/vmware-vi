# ArrayOfHostPortGroup

A boxed array of *HostPortGroup*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPortGroup]**](HostPortGroup.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_port_group import ArrayOfHostPortGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPortGroup from a JSON string
array_of_host_port_group_instance = ArrayOfHostPortGroup.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPortGroup.to_json()

# convert the object into a dict
array_of_host_port_group_dict = array_of_host_port_group_instance.to_dict()
# create an instance of ArrayOfHostPortGroup from a dict
array_of_host_port_group_form_dict = array_of_host_port_group.from_dict(array_of_host_port_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


