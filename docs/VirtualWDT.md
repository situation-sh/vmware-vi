# VirtualWDT

This data object type represents a watchdog timer in a virtual machine.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_on_boot** | **bool** | Flag to indicate if the virtual watchdog timer device should be initialized as the Enabled/Stopped or Enabled/Running sub-state.  If not set, the device will default to being initialized as the Enabled/Stopped sub-state.  ***Since:*** vSphere API 7.0  | 
**running** | **bool** | Flag to indicate if the virtual watchdog timer device is currently in the Enabled/Running state.  The guest can cause state changes, which will result in this flag being either set or cleared.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.virtual_wdt import VirtualWDT

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualWDT from a JSON string
virtual_wdt_instance = VirtualWDT.from_json(json)
# print the JSON string representation of the object
print VirtualWDT.to_json()

# convert the object into a dict
virtual_wdt_dict = virtual_wdt_instance.to_dict()
# create an instance of VirtualWDT from a dict
virtual_wdt_form_dict = virtual_wdt.from_dict(virtual_wdt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


