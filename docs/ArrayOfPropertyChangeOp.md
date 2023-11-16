# ArrayOfPropertyChangeOp

A boxed array of *PropertyChangeOp_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PropertyChangeOpEnum]**](PropertyChangeOpEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_property_change_op import ArrayOfPropertyChangeOp

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPropertyChangeOp from a JSON string
array_of_property_change_op_instance = ArrayOfPropertyChangeOp.from_json(json)
# print the JSON string representation of the object
print ArrayOfPropertyChangeOp.to_json()

# convert the object into a dict
array_of_property_change_op_dict = array_of_property_change_op_instance.to_dict()
# create an instance of ArrayOfPropertyChangeOp from a dict
array_of_property_change_op_form_dict = array_of_property_change_op.from_dict(array_of_property_change_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


