# ArrayOfDistributedVirtualSwitchPortCriteria

A boxed array of *DistributedVirtualSwitchPortCriteria*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchPortCriteria]**](DistributedVirtualSwitchPortCriteria.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_port_criteria import ArrayOfDistributedVirtualSwitchPortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchPortCriteria from a JSON string
array_of_distributed_virtual_switch_port_criteria_instance = ArrayOfDistributedVirtualSwitchPortCriteria.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchPortCriteria.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_port_criteria_dict = array_of_distributed_virtual_switch_port_criteria_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchPortCriteria from a dict
array_of_distributed_virtual_switch_port_criteria_form_dict = array_of_distributed_virtual_switch_port_criteria.from_dict(array_of_distributed_virtual_switch_port_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


