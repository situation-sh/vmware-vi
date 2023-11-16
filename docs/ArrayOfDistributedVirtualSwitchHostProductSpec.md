# ArrayOfDistributedVirtualSwitchHostProductSpec

A boxed array of *DistributedVirtualSwitchHostProductSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchHostProductSpec]**](DistributedVirtualSwitchHostProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_host_product_spec import ArrayOfDistributedVirtualSwitchHostProductSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchHostProductSpec from a JSON string
array_of_distributed_virtual_switch_host_product_spec_instance = ArrayOfDistributedVirtualSwitchHostProductSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchHostProductSpec.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_host_product_spec_dict = array_of_distributed_virtual_switch_host_product_spec_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchHostProductSpec from a dict
array_of_distributed_virtual_switch_host_product_spec_form_dict = array_of_distributed_virtual_switch_host_product_spec.from_dict(array_of_distributed_virtual_switch_host_product_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


