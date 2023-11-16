# ArrayOfVmNvramFileQuery

A boxed array of *VmNvramFileQuery*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmNvramFileQuery]**](VmNvramFileQuery.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_nvram_file_query import ArrayOfVmNvramFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmNvramFileQuery from a JSON string
array_of_vm_nvram_file_query_instance = ArrayOfVmNvramFileQuery.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmNvramFileQuery.to_json()

# convert the object into a dict
array_of_vm_nvram_file_query_dict = array_of_vm_nvram_file_query_instance.to_dict()
# create an instance of ArrayOfVmNvramFileQuery from a dict
array_of_vm_nvram_file_query_form_dict = array_of_vm_nvram_file_query.from_dict(array_of_vm_nvram_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


