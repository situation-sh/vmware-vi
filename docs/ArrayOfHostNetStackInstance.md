# ArrayOfHostNetStackInstance

A boxed array of *HostNetStackInstance*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetStackInstance]**](HostNetStackInstance.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_net_stack_instance import ArrayOfHostNetStackInstance

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetStackInstance from a JSON string
array_of_host_net_stack_instance_instance = ArrayOfHostNetStackInstance.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetStackInstance.to_json()

# convert the object into a dict
array_of_host_net_stack_instance_dict = array_of_host_net_stack_instance_instance.to_dict()
# create an instance of ArrayOfHostNetStackInstance from a dict
array_of_host_net_stack_instance_form_dict = array_of_host_net_stack_instance.from_dict(array_of_host_net_stack_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


