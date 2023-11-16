# DvsUpgradeAvailableEvent

An upgrade for the distributed virtual switch is available.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.dvs_upgrade_available_event import DvsUpgradeAvailableEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsUpgradeAvailableEvent from a JSON string
dvs_upgrade_available_event_instance = DvsUpgradeAvailableEvent.from_json(json)
# print the JSON string representation of the object
print DvsUpgradeAvailableEvent.to_json()

# convert the object into a dict
dvs_upgrade_available_event_dict = dvs_upgrade_available_event_instance.to_dict()
# create an instance of DvsUpgradeAvailableEvent from a dict
dvs_upgrade_available_event_form_dict = dvs_upgrade_available_event.from_dict(dvs_upgrade_available_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


