# FileFault

The common base type for all file-related exceptions. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | The file in question.  | 

## Example

```python
from vmware_vi.models.file_fault import FileFault

# TODO update the JSON string below
json = "{}"
# create an instance of FileFault from a JSON string
file_fault_instance = FileFault.from_json(json)
# print the JSON string representation of the object
print FileFault.to_json()

# convert the object into a dict
file_fault_dict = file_fault_instance.to_dict()
# create an instance of FileFault from a dict
file_fault_form_dict = file_fault.from_dict(file_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


