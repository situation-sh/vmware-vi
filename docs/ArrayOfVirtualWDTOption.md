# ArrayOfVirtualWDTOption

A boxed array of *VirtualWDTOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualWDTOption]**](VirtualWDTOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_wdt_option import ArrayOfVirtualWDTOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualWDTOption from a JSON string
array_of_virtual_wdt_option_instance = ArrayOfVirtualWDTOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualWDTOption.to_json()

# convert the object into a dict
array_of_virtual_wdt_option_dict = array_of_virtual_wdt_option_instance.to_dict()
# create an instance of ArrayOfVirtualWDTOption from a dict
array_of_virtual_wdt_option_form_dict = array_of_virtual_wdt_option.from_dict(array_of_virtual_wdt_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


