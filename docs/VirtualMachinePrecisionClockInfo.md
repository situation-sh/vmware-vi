# VirtualMachinePrecisionClockInfo

The PrecisionClockInfo data object type describes available host clock resources, which can be used as backing reference for virtual precision clock devices.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_clock_protocol** | **str** | The currrent host system clock synchronization protocol.  Used for specifying protocol in *VirtualPrecisionClockSystemClockBackingInfo*.  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_precision_clock_info import VirtualMachinePrecisionClockInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachinePrecisionClockInfo from a JSON string
virtual_machine_precision_clock_info_instance = VirtualMachinePrecisionClockInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachinePrecisionClockInfo.to_json()

# convert the object into a dict
virtual_machine_precision_clock_info_dict = virtual_machine_precision_clock_info_instance.to_dict()
# create an instance of VirtualMachinePrecisionClockInfo from a dict
virtual_machine_precision_clock_info_form_dict = virtual_machine_precision_clock_info.from_dict(virtual_machine_precision_clock_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


