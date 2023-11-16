# ArrayOfHostNumaNode

A boxed array of *HostNumaNode*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNumaNode]**](HostNumaNode.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_numa_node import ArrayOfHostNumaNode

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNumaNode from a JSON string
array_of_host_numa_node_instance = ArrayOfHostNumaNode.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNumaNode.to_json()

# convert the object into a dict
array_of_host_numa_node_dict = array_of_host_numa_node_instance.to_dict()
# create an instance of ArrayOfHostNumaNode from a dict
array_of_host_numa_node_form_dict = array_of_host_numa_node.from_dict(array_of_host_numa_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


