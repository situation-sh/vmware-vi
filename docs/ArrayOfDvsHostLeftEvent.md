# ArrayOfDvsHostLeftEvent

A boxed array of *DvsHostLeftEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsHostLeftEvent]**](DvsHostLeftEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_host_left_event import ArrayOfDvsHostLeftEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsHostLeftEvent from a JSON string
array_of_dvs_host_left_event_instance = ArrayOfDvsHostLeftEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsHostLeftEvent.to_json()

# convert the object into a dict
array_of_dvs_host_left_event_dict = array_of_dvs_host_left_event_instance.to_dict()
# create an instance of ArrayOfDvsHostLeftEvent from a dict
array_of_dvs_host_left_event_form_dict = array_of_dvs_host_left_event.from_dict(array_of_dvs_host_left_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


