# VirtualMachinePropertyRelation

Data object which represents relations between a property and its target value and the required values of any other properties in the vm configuration so that the target value can be set.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**DynamicProperty**](DynamicProperty.md) |  | 
**relations** | [**List[DynamicProperty]**](DynamicProperty.md) | The related properties and their values  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_property_relation import VirtualMachinePropertyRelation

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachinePropertyRelation from a JSON string
virtual_machine_property_relation_instance = VirtualMachinePropertyRelation.from_json(json)
# print the JSON string representation of the object
print VirtualMachinePropertyRelation.to_json()

# convert the object into a dict
virtual_machine_property_relation_dict = virtual_machine_property_relation_instance.to_dict()
# create an instance of VirtualMachinePropertyRelation from a dict
virtual_machine_property_relation_form_dict = virtual_machine_property_relation.from_dict(virtual_machine_property_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


