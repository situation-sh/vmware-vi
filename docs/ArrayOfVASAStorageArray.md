# ArrayOfVASAStorageArray

A boxed array of *VASAStorageArray*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VASAStorageArray]**](VASAStorageArray.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vasa_storage_array import ArrayOfVASAStorageArray

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVASAStorageArray from a JSON string
array_of_vasa_storage_array_instance = ArrayOfVASAStorageArray.from_json(json)
# print the JSON string representation of the object
print ArrayOfVASAStorageArray.to_json()

# convert the object into a dict
array_of_vasa_storage_array_dict = array_of_vasa_storage_array_instance.to_dict()
# create an instance of ArrayOfVASAStorageArray from a dict
array_of_vasa_storage_array_form_dict = array_of_vasa_storage_array.from_dict(array_of_vasa_storage_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


