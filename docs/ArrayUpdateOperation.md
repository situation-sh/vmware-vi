# ArrayUpdateOperation

A boxed *ArrayUpdateOperation_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ArrayUpdateOperationEnum**](ArrayUpdateOperationEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_update_operation import ArrayUpdateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayUpdateOperation from a JSON string
array_update_operation_instance = ArrayUpdateOperation.from_json(json)
# print the JSON string representation of the object
print ArrayUpdateOperation.to_json()

# convert the object into a dict
array_update_operation_dict = array_update_operation_instance.to_dict()
# create an instance of ArrayUpdateOperation from a dict
array_update_operation_form_dict = array_update_operation.from_dict(array_update_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


