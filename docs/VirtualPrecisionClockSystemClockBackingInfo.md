# VirtualPrecisionClockSystemClockBackingInfo

The *VirtualPrecisionClockSystemClockBackingInfo* data object contains information about using host system clock as the backing reference clock for this virtual device.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The time synchronization protocol used to discipline system clock.  See *HostDateTimeInfoProtocol_enum* for valid values.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_precision_clock_system_clock_backing_info import VirtualPrecisionClockSystemClockBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPrecisionClockSystemClockBackingInfo from a JSON string
virtual_precision_clock_system_clock_backing_info_instance = VirtualPrecisionClockSystemClockBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualPrecisionClockSystemClockBackingInfo.to_json()

# convert the object into a dict
virtual_precision_clock_system_clock_backing_info_dict = virtual_precision_clock_system_clock_backing_info_instance.to_dict()
# create an instance of VirtualPrecisionClockSystemClockBackingInfo from a dict
virtual_precision_clock_system_clock_backing_info_form_dict = virtual_precision_clock_system_clock_backing_info.from_dict(virtual_precision_clock_system_clock_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


