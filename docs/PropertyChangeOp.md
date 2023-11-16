# PropertyChangeOp

A boxed *PropertyChangeOp_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**PropertyChangeOpEnum**](PropertyChangeOpEnum.md) |  | 

## Example

```python
from vmware_vi.models.property_change_op import PropertyChangeOp

# TODO update the JSON string below
json = "{}"
# create an instance of PropertyChangeOp from a JSON string
property_change_op_instance = PropertyChangeOp.from_json(json)
# print the JSON string representation of the object
print PropertyChangeOp.to_json()

# convert the object into a dict
property_change_op_dict = property_change_op_instance.to_dict()
# create an instance of PropertyChangeOp from a dict
property_change_op_form_dict = property_change_op.from_dict(property_change_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


