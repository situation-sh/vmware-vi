# VirtualPrecisionClockSystemClockBackingOption

This data object type describes the options for the *VirtualPrecisionClockSystemClockBackingInfo* VirtualPrecisionClockSystemClockBackingInfo} data object type.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | [**ChoiceOption**](ChoiceOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_precision_clock_system_clock_backing_option import VirtualPrecisionClockSystemClockBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPrecisionClockSystemClockBackingOption from a JSON string
virtual_precision_clock_system_clock_backing_option_instance = VirtualPrecisionClockSystemClockBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualPrecisionClockSystemClockBackingOption.to_json()

# convert the object into a dict
virtual_precision_clock_system_clock_backing_option_dict = virtual_precision_clock_system_clock_backing_option_instance.to_dict()
# create an instance of VirtualPrecisionClockSystemClockBackingOption from a dict
virtual_precision_clock_system_clock_backing_option_form_dict = virtual_precision_clock_system_clock_backing_option.from_dict(virtual_precision_clock_system_clock_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


