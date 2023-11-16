# VirtualPrecisionClock

This data object type represents a virtual clock device providing precision time in a virtual machine.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_precision_clock import VirtualPrecisionClock

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPrecisionClock from a JSON string
virtual_precision_clock_instance = VirtualPrecisionClock.from_json(json)
# print the JSON string representation of the object
print VirtualPrecisionClock.to_json()

# convert the object into a dict
virtual_precision_clock_dict = virtual_precision_clock_instance.to_dict()
# create an instance of VirtualPrecisionClock from a dict
virtual_precision_clock_form_dict = virtual_precision_clock.from_dict(virtual_precision_clock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


