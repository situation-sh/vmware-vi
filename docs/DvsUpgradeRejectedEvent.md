# DvsUpgradeRejectedEvent

An upgrade for the distributed virtual switch is rejected.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.dvs_upgrade_rejected_event import DvsUpgradeRejectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsUpgradeRejectedEvent from a JSON string
dvs_upgrade_rejected_event_instance = DvsUpgradeRejectedEvent.from_json(json)
# print the JSON string representation of the object
print DvsUpgradeRejectedEvent.to_json()

# convert the object into a dict
dvs_upgrade_rejected_event_dict = dvs_upgrade_rejected_event_instance.to_dict()
# create an instance of DvsUpgradeRejectedEvent from a dict
dvs_upgrade_rejected_event_form_dict = dvs_upgrade_rejected_event.from_dict(dvs_upgrade_rejected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


