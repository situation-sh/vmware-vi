# DvsMergedEvent

Two distributed virtual switches was merged.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_dvs** | [**DvsEventArgument**](DvsEventArgument.md) |  | 
**destination_dvs** | [**DvsEventArgument**](DvsEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.dvs_merged_event import DvsMergedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsMergedEvent from a JSON string
dvs_merged_event_instance = DvsMergedEvent.from_json(json)
# print the JSON string representation of the object
print DvsMergedEvent.to_json()

# convert the object into a dict
dvs_merged_event_dict = dvs_merged_event_instance.to_dict()
# create an instance of DvsMergedEvent from a dict
dvs_merged_event_form_dict = dvs_merged_event.from_dict(dvs_merged_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


