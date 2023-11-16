# ArrayOfVirtualMachinePropertyRelation

A boxed array of *VirtualMachinePropertyRelation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachinePropertyRelation]**](VirtualMachinePropertyRelation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_property_relation import ArrayOfVirtualMachinePropertyRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachinePropertyRelation from a JSON string
array_of_virtual_machine_property_relation_instance = ArrayOfVirtualMachinePropertyRelation.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachinePropertyRelation.to_json()

# convert the object into a dict
array_of_virtual_machine_property_relation_dict = array_of_virtual_machine_property_relation_instance.to_dict()
# create an instance of ArrayOfVirtualMachinePropertyRelation from a dict
array_of_virtual_machine_property_relation_form_dict = array_of_virtual_machine_property_relation.from_dict(array_of_virtual_machine_property_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


