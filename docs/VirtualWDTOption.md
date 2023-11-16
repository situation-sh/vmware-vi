# VirtualWDTOption

This data object type contains the options for the virtual watchdog timer class.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_on_boot** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_wdt_option import VirtualWDTOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualWDTOption from a JSON string
virtual_wdt_option_instance = VirtualWDTOption.from_json(json)
# print the JSON string representation of the object
print VirtualWDTOption.to_json()

# convert the object into a dict
virtual_wdt_option_dict = virtual_wdt_option_instance.to_dict()
# create an instance of VirtualWDTOption from a dict
virtual_wdt_option_form_dict = virtual_wdt_option.from_dict(virtual_wdt_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


