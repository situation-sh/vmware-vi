# TurnDiskLocatorLedOnRequestType

The parameters of *HostStorageSystem.TurnDiskLocatorLedOn_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scsi_disk_uuids** | **List[str]** | The SCSI disk UUIDs for which the disk locator LED should be turned on.  | 

## Example

```python
from vmware_vi.models.turn_disk_locator_led_on_request_type import TurnDiskLocatorLedOnRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of TurnDiskLocatorLedOnRequestType from a JSON string
turn_disk_locator_led_on_request_type_instance = TurnDiskLocatorLedOnRequestType.from_json(json)
# print the JSON string representation of the object
print TurnDiskLocatorLedOnRequestType.to_json()

# convert the object into a dict
turn_disk_locator_led_on_request_type_dict = turn_disk_locator_led_on_request_type_instance.to_dict()
# create an instance of TurnDiskLocatorLedOnRequestType from a dict
turn_disk_locator_led_on_request_type_form_dict = turn_disk_locator_led_on_request_type.from_dict(turn_disk_locator_led_on_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


