# ArrayOfFailoverNodeInfo

A boxed array of *FailoverNodeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FailoverNodeInfo]**](FailoverNodeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_failover_node_info import ArrayOfFailoverNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFailoverNodeInfo from a JSON string
array_of_failover_node_info_instance = ArrayOfFailoverNodeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfFailoverNodeInfo.to_json()

# convert the object into a dict
array_of_failover_node_info_dict = array_of_failover_node_info_instance.to_dict()
# create an instance of ArrayOfFailoverNodeInfo from a dict
array_of_failover_node_info_form_dict = array_of_failover_node_info.from_dict(array_of_failover_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


