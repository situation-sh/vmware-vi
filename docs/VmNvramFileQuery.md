# VmNvramFileQuery

This data object type describes the query specification for a non-volatile memory file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_nvram_file_query import VmNvramFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VmNvramFileQuery from a JSON string
vm_nvram_file_query_instance = VmNvramFileQuery.from_json(json)
# print the JSON string representation of the object
print VmNvramFileQuery.to_json()

# convert the object into a dict
vm_nvram_file_query_dict = vm_nvram_file_query_instance.to_dict()
# create an instance of VmNvramFileQuery from a dict
vm_nvram_file_query_form_dict = vm_nvram_file_query.from_dict(vm_nvram_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


