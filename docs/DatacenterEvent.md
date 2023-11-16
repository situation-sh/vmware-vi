# DatacenterEvent

These are datacenter events.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.datacenter_event import DatacenterEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterEvent from a JSON string
datacenter_event_instance = DatacenterEvent.from_json(json)
# print the JSON string representation of the object
print DatacenterEvent.to_json()

# convert the object into a dict
datacenter_event_dict = datacenter_event_instance.to_dict()
# create an instance of DatacenterEvent from a dict
datacenter_event_form_dict = datacenter_event.from_dict(datacenter_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


