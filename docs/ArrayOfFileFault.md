# ArrayOfFileFault

A boxed array of *FileFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FileFault]**](FileFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_file_fault import ArrayOfFileFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFileFault from a JSON string
array_of_file_fault_instance = ArrayOfFileFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfFileFault.to_json()

# convert the object into a dict
array_of_file_fault_dict = array_of_file_fault_instance.to_dict()
# create an instance of ArrayOfFileFault from a dict
array_of_file_fault_form_dict = array_of_file_fault.from_dict(array_of_file_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


