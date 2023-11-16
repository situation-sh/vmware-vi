# VimFault

The common base type for all virtual infrastructure management exceptions. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vim_fault import VimFault

# TODO update the JSON string below
json = "{}"
# create an instance of VimFault from a JSON string
vim_fault_instance = VimFault.from_json(json)
# print the JSON string representation of the object
print VimFault.to_json()

# convert the object into a dict
vim_fault_dict = vim_fault_instance.to_dict()
# create an instance of VimFault from a dict
vim_fault_form_dict = vim_fault.from_dict(vim_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


