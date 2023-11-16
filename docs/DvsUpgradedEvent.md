# DvsUpgradedEvent

The distributed virtual switch was upgraded.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_info** | [**DistributedVirtualSwitchProductSpec**](DistributedVirtualSwitchProductSpec.md) |  | 

## Example

```python
from vmware_vi.models.dvs_upgraded_event import DvsUpgradedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsUpgradedEvent from a JSON string
dvs_upgraded_event_instance = DvsUpgradedEvent.from_json(json)
# print the JSON string representation of the object
print DvsUpgradedEvent.to_json()

# convert the object into a dict
dvs_upgraded_event_dict = dvs_upgraded_event_instance.to_dict()
# create an instance of DvsUpgradedEvent from a dict
dvs_upgraded_event_form_dict = dvs_upgraded_event.from_dict(dvs_upgraded_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


