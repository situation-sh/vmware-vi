# TurnDiskLocatorLedOffRequestType

The parameters of *HostStorageSystem.TurnDiskLocatorLedOff_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scsi_disk_uuids** | **List[str]** | The SCSI disk UUIDs for which the disk locator LED should be turned off.  | 

## Example

```python
from vmware_vi.models.turn_disk_locator_led_off_request_type import TurnDiskLocatorLedOffRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of TurnDiskLocatorLedOffRequestType from a JSON string
turn_disk_locator_led_off_request_type_instance = TurnDiskLocatorLedOffRequestType.from_json(json)
# print the JSON string representation of the object
print TurnDiskLocatorLedOffRequestType.to_json()

# convert the object into a dict
turn_disk_locator_led_off_request_type_dict = turn_disk_locator_led_off_request_type_instance.to_dict()
# create an instance of TurnDiskLocatorLedOffRequestType from a dict
turn_disk_locator_led_off_request_type_form_dict = turn_disk_locator_led_off_request_type.from_dict(turn_disk_locator_led_off_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


