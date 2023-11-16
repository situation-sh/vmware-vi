# ArrayUpdateSpec

An ArrayUpdateSpec data object type is a common superclass for supporting incremental updates to arrays.  The common code pattern is:           class MyTypeSpec extrends ArrayUpdateSpec {                MyTypeInfo info;          } The ArrayUpdateSpec contains the following: - **operation**: the type of operation being performed. - **removeKey**: In the case of a remove operation, the   key value that identifies the array to be removed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**ArrayUpdateOperationEnum**](ArrayUpdateOperationEnum.md) |  | 
**remove_key** | [**Any**](Any.md) |  | [optional] 

## Example

```python
from vmware_vi.models.array_update_spec import ArrayUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayUpdateSpec from a JSON string
array_update_spec_instance = ArrayUpdateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayUpdateSpec.to_json()

# convert the object into a dict
array_update_spec_dict = array_update_spec_instance.to_dict()
# create an instance of ArrayUpdateSpec from a dict
array_update_spec_form_dict = array_update_spec.from_dict(array_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


