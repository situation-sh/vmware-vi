# HostUpgradeFailedEvent

This event records a failure to connect to a host due to an installation or upgrade issue. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_upgrade_failed_event import HostUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of HostUpgradeFailedEvent from a JSON string
host_upgrade_failed_event_instance = HostUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print HostUpgradeFailedEvent.to_json()

# convert the object into a dict
host_upgrade_failed_event_dict = host_upgrade_failed_event_instance.to_dict()
# create an instance of HostUpgradeFailedEvent from a dict
host_upgrade_failed_event_form_dict = host_upgrade_failed_event.from_dict(host_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


