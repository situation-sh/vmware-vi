# ArrayOfVirtualCdromOption

A boxed array of *VirtualCdromOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualCdromOption]**](VirtualCdromOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_cdrom_option import ArrayOfVirtualCdromOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualCdromOption from a JSON string
array_of_virtual_cdrom_option_instance = ArrayOfVirtualCdromOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualCdromOption.to_json()

# convert the object into a dict
array_of_virtual_cdrom_option_dict = array_of_virtual_cdrom_option_instance.to_dict()
# create an instance of ArrayOfVirtualCdromOption from a dict
array_of_virtual_cdrom_option_form_dict = array_of_virtual_cdrom_option.from_dict(array_of_virtual_cdrom_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


