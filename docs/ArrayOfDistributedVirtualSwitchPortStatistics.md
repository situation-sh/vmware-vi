# ArrayOfDistributedVirtualSwitchPortStatistics

A boxed array of *DistributedVirtualSwitchPortStatistics*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchPortStatistics]**](DistributedVirtualSwitchPortStatistics.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_port_statistics import ArrayOfDistributedVirtualSwitchPortStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchPortStatistics from a JSON string
array_of_distributed_virtual_switch_port_statistics_instance = ArrayOfDistributedVirtualSwitchPortStatistics.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchPortStatistics.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_port_statistics_dict = array_of_distributed_virtual_switch_port_statistics_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchPortStatistics from a dict
array_of_distributed_virtual_switch_port_statistics_form_dict = array_of_distributed_virtual_switch_port_statistics.from_dict(array_of_distributed_virtual_switch_port_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


