# ArrayOfFilesystemQuiesceFault

A boxed array of *FilesystemQuiesceFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FilesystemQuiesceFault]**](FilesystemQuiesceFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_filesystem_quiesce_fault import ArrayOfFilesystemQuiesceFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFilesystemQuiesceFault from a JSON string
array_of_filesystem_quiesce_fault_instance = ArrayOfFilesystemQuiesceFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfFilesystemQuiesceFault.to_json()

# convert the object into a dict
array_of_filesystem_quiesce_fault_dict = array_of_filesystem_quiesce_fault_instance.to_dict()
# create an instance of ArrayOfFilesystemQuiesceFault from a dict
array_of_filesystem_quiesce_fault_form_dict = array_of_filesystem_quiesce_fault.from_dict(array_of_filesystem_quiesce_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


