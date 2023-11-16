# ArrayOfVimFault

A boxed array of *VimFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VimFault]**](VimFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vim_fault import ArrayOfVimFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVimFault from a JSON string
array_of_vim_fault_instance = ArrayOfVimFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfVimFault.to_json()

# convert the object into a dict
array_of_vim_fault_dict = array_of_vim_fault_instance.to_dict()
# create an instance of ArrayOfVimFault from a dict
array_of_vim_fault_form_dict = array_of_vim_fault.from_dict(array_of_vim_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


