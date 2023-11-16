# VirtualPrecisionClockOption

The VirtualPrecisionClockOption data object type describes the options for the *VirtualPrecisionClock* data object type.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_precision_clock_option import VirtualPrecisionClockOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPrecisionClockOption from a JSON string
virtual_precision_clock_option_instance = VirtualPrecisionClockOption.from_json(json)
# print the JSON string representation of the object
print VirtualPrecisionClockOption.to_json()

# convert the object into a dict
virtual_precision_clock_option_dict = virtual_precision_clock_option_instance.to_dict()
# create an instance of VirtualPrecisionClockOption from a dict
virtual_precision_clock_option_form_dict = virtual_precision_clock_option.from_dict(virtual_precision_clock_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


